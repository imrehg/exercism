#!/usr/bin/env bash

ARGS=1

usage () {
    echo "Usage: leap.sh <year>"
    exit 1
}

main () {
    local year=$1
    local isLeap="false"

    # Input checks
    if (( $# != ARGS )); then
        usage
    fi
    case ${year} in
        ''|*[!0-9]*)
            usage
            ;;
    esac

    if (( year % 4 == 0 && year % 100 != 0)) || (( year % 400 == 0 )); then
        isLeap="true"
    fi

    echo "${isLeap}"
}

main "$@"
