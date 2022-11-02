#!/bin/bash

#Mendeklarasikan fungsi
nama() {
    echo "siapa namamu?"
    read nama
}
npm() {
    echo "sebutkan npmmu"
    read npm
    echo -e "hai $nama dengan npm $npm, selamat datang \n di praktikum sistem operasi yang seru ini ya!"
}

#memanggil fungsi
nama 
npm
