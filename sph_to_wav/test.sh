#!/bin/sh
filename='/root/utils/make_sph2pipe_file.txt'
while read line
do
  echo $line
  $line
done < $filename
