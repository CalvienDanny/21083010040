#!/bin/bash

function nama {
    echo "siapa namamu?"
    read nama
}
function npm {
    echo "sebutkan npmmu"
    read npm
    echo -e "hai $nama dengan npm $npm, selamat datang \n di praktikum sistem operasi kelas a"
}

nama
npm
