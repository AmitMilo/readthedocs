import pathlib
import os

from joblib import Parallel, delayed

import subprocess

N_JOBS_FOR_SEARCH = 10


class Directory:
    def __init__(self, path_under_root: pathlib.Path, python_files, dirs):
        self._path_under_root = path_under_root
        self._files = python_files
        self._dirs = dirs

    def document(self, docs_path):
        """
        Make rst hierarchy for all python files in the directory (recursively).
        Args:
            docs_path: Path of the 'docs' directory.
        """
        # Calculate the path represents current directory under the 'docs' directory (where to put the rst files).
        directory_docs_path = docs_path / self._path_under_root

        if not directory_docs_path.exists():
            directory_docs_path.mkdir()

            with open(docs_path/"conf.py", 'a') as config_file:
                # Add the directory to the configuration file.
                config_file.write(f"sys.path.insert(0, os.path.abspath('../{self._path_under_root}'))\n")

        # Create modules files + rst file per each python file.
        subprocess.run(["sphinx-apidoc", "-o", str(directory_docs_path), str(self._path_under_root), "--force"])

        # Create index file of the subdirectory.
        with open(directory_docs_path/"index.rst", "w") as index_file:
            index_file.write(".. toctree::\n\t:maxdepth: 2\n\t:caption: Contents:\n\n\tmodules\n\n")

            for sub_dir in self._dirs:
                index_file.write(f"\t{sub_dir}/index\n")
                sub_dir.document(docs_path)

    @staticmethod
    def make_html(docs_path):
        """
        Create readthedocs website based on the previously created rst files.
        Args:
            docs_path: Path of the 'docs' directory.
        """
        subprocess.run(["make", "-C", str(docs_path), "html"])

    def __str__(self):
        return str(self._path_under_root)


def walk_level(some_dir: pathlib.Path):
    """
    Scan the first level of a directory.
    """
    assert some_dir.is_dir(), f"{some_dir} is not a directory."
    root_dir, dirs, files = next(os.walk(some_dir, topdown=True))

    files = list(map(pathlib.Path, files))

    return root_dir, dirs, files


def excluded(directory: str):
    """
    Define excluded directories.
    """
    return directory == "datascience" or directory == "__pycache__" or directory == "docs" or directory.startswith(".")


def not_excluded(directory: str):
    """
    Define not excluded directories.
    """
    return not excluded(directory)


def find_files(root_dir: pathlib.Path):
    """
    Search for all the files in the tree structured from the root directory.
    """

    result_files = list()

    # Current level directories and files.
    _, dirs, files = walk_level(root_dir)

    # Iterate over not excluded directories and continue recursively.
    dirs = list(filter(not_excluded, dirs))

    # Document python files only.
    files = list(filter(is_python, files))

    # Iterate over files in the current level and select the jupyter notebooks.
    for f in files:
        result_files.append(root_dir / f)

    # Continue searching recursively in a parallelized way.
    subdirs = Parallel(n_jobs=N_JOBS_FOR_SEARCH)(delayed(find_files)(root_dir / d) for d in dirs)

    return Directory(root_dir, result_files, subdirs)


def is_python(file: pathlib.Path):
    """
    Return whether a file is a python file or not.
    """
    return file.suffix == ".py"


if __name__ == '__main__':
    root_dir = find_files(pathlib.Path("."))

    docs_path = pathlib.Path("docs")
    root_dir.document(docs_path)
    Directory.make_html(docs_path)
