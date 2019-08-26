#!/usr/bin/env bash

main () {
    local number=$1
    local drops=""
    if ((number % 3 == 0)); then
        drops="${drops}Pling"
    fi
    if ((number % 5 == 0)); then
        drops="${drops}Plang"
    fi
    if ((number % 7 == 0)); then
        drops="${drops}Plong"
    fi
    echo "${drops:=${number}}"
}

main "$@"
