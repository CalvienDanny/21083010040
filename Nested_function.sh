#!/bin/bash

nama() {
    echo "siapa namamu"
    read nama
    npm 
}
npm() {
    echo "npmmu?"
    read npm
    echo -e "hai $nama dengan npm $npm, selamat datang di kelas sistem operasi a"
}

nama

