#!/usr/bin/env bash

main () {
    local inString=$1
    local outString=""
    local letter
    while (( ${#inString} > 0 )); do
        letter="${inString:${#inString}-1:1}"
        outString="${outString}${letter}"
        inString="${inString%${letter}}"
    done
    echo "$outString"
}

main "$@"
