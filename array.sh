#1/bin/bash

#deklarasi array
distrolinux=("mint" "ubuntu" "kali" "arch" "debian")

#random distro
let pilih=$RANDOM%5

#eksekusi
echo "saya memilih distro $pilih, ${distroLinux[pilih]} !"
