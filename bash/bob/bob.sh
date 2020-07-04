#!/usr/bin/env bash

main () {
    local message=$1
    # Remove leading and trailing spaces from message
    shopt -s extglob
    message="${message%%*([[:space:]])}"
    message="${message##*([[:space:]])}"
    shopt -u extglob
    shout_pattern='^[^[:lower:]]*[[:upper:]][^[:lower:]]*'

    if [[ $message =~ $shout_pattern\?$ ]]; then
        echo "Calm down, I know what I'm doing!"
    elif [[ $message =~ $shout_pattern$ ]]; then
        echo "Whoa, chill out!"
    elif [[ $message =~ ^.*[^[:space:]].*\?$ ]]; then
        echo "Sure."
    elif [[ "$message" == "" ]]; then
        echo "Fine. Be that way!"
    else
        echo "Whatever."
    fi
}

main "$@"
