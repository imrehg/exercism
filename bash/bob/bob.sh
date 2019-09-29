#!/usr/bin/env bash

main () {
    local message=$1
    if [[ $message =~ ^[[:space:]]*[^[:lower:]]*[[:upper:]][^[:lower:]]*\?[[:space:]]*$ ]]; then
        echo "Calm down, I know what I'm doing!"
    elif [[ $message =~ ^[[:space:]]*[^[:lower:]]*[[:upper:]][^[:lower:]]*[[:space:]]*$ ]]; then
        echo "Whoa, chill out!"
    elif [[ $message =~ ^.*[^[:space:]].*\?[[:space:]]*$ ]]; then
        echo "Sure."
    elif [[ "$message" =~ ^[[:space:]]*$ ]]; then
        echo "Fine. Be that way!"
    else
        echo "Whatever."
    fi
}

main "$@"
