#!/usr/bin/env bash

# The letters of the alphabet
LETTERS="abcdefghijklmnopqrstuvwxyz"

#######################################
# Pangram test of a string
# Arguments:
#   candidate: the canidate string
# Returns:
#   true/false check result
#######################################
main () {
    # Get input variable and convert to lowercase
    local candidate=${1,,}
    local -i iterator
    for (( iterator=0; iterator < ${#LETTERS}; iterator++ )); do
        if [[ $candidate != *"${LETTERS:iterator:1}"* ]]; then
            # As soon as there's a letter that we couldn't find in the input,
            # the we can bail
            echo "false"
            return
        fi
    done
    echo "true"
}

main "$@"
