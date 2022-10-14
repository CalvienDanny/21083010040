#!/bin/bash

declare -a jumlahIPS
read -p "Masukkan jumlah ipsmu: " jumlahIPS

declare -a nilaiIPS
read -p "Masukkan nilai ipsmu: " nilaiIPS

for i in ${nilaiIPS[@]}
do
        echo $i
        if [ $i -ge 0 ]
        then
                ((jmlhIPS=$jumlahIPS))
                ((totIPS=$totIPS + $i))
        fi
        ((IPK=$totIPS/$jumlahIPS))

done
echo "IPK mhs= $totIPS/$jumlahIPS"
echo "IPK mhs= $IPK"
