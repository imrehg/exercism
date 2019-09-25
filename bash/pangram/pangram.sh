#!/usr/bin/env bash

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
    for letter in {a..z}; do
        if [[ $candidate != *${letter}* ]]; then
            # As soon as there's a letter that we couldn't find in the input,
            # the we can bail
            echo "false"
            return
        fi
    done
    echo "true"
}

main "$@"
