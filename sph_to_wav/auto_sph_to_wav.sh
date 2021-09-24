#!/bin/sh
MAIN_ROOT=$PWD
export PATH=$MAIN_ROOT:$PATH
inputs=$PWD/test
echo "$inputs"
outputs=$PWD/output
echo "$outputs"
make_list_for_sph_to_wav.py --in_dir "$inputs" --out_path "$outputs"
filename='/root/utils/make_sph2pipe_file.txt'
while read line
do
  echo $line
  $line
done < $filename
