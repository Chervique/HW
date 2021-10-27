#!/bin/bash

printf "\n"
read -p "# of characters: " pass_length
printf "\n"


for i in {1..5}; do (tr -cd '[:alnum:]' < /dev/urandom | fold -w${pass_lenght} | head -n 1); done
printf "$pass_output\n"

