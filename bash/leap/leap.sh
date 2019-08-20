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
    if [ $# -ne "$ARGS" ]; then
        usage
    fi
    case ${year} in
        ''|*[!0-9]*)
            usage
            ;;
    esac

    local remainder4=$(( year % 4 ))
    local remainder100=$(( year % 100 ))
    local remainder400=$(( year % 400 ))

    if { [ ${remainder4} -eq 0 ] && [ ${remainder100} -ne 0 ]; } || [ ${remainder400} -eq 0 ]; then
        isLeap="true"
    fi

    echo "${isLeap}"
}

main "$@"
