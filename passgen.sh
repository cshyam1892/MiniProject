#!/bin/bash

case $1 in 
    12)
        date +%s | sha256sum | base64 | head -c 12 ; echo
        ;;

    16)
        date +%s | sha256sum | base64 | head -c 16; echo
        ;;

    32)
        date +%s | sha256sum | base64 | head -c 32; echo
        ;;
    *)
        date +%s | sha256sum | base64 | head -c $1; echo
        ;;
esac



