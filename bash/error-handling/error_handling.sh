#!/usr/bin/env bash

usage () {
    echo "Usage: ./error_handling <greetee>"
    exit 1
}

main () {
    # Check for the right number of arguments.
    if [ $# -ne 1 ]; then
        usage
    fi
    echo "Hello, $1"
}

main "$@"
