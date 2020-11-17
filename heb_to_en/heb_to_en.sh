clipboard=`pbpaste`
if test -f "$clipboard"; then
  res="$(python3 ~/readthedocs/heb_to_en/heb_to_en.py)"
  echo "$res" | pbcopy
fi
