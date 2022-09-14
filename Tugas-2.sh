#!/bin/bash

a=1
b=2
let c=$a+$b
let d=$a-$b

if [ $c == $d ]
then
  echo "kedua contoh jumlahnya sama"
elif [ $c -gt $d ]
then
  echo "d lebih kecil dari c"
elif [ $c -lt $ d ]
then
  echo "d lebih besar dari c"
else
  echo "error"
fi
