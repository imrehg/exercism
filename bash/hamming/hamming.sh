#!/usr/bin/env bash
#
# Perform Hamming distance computation of two strings

#######################################
# Print script usage
# Arguments:
#   None
# Returns:
#   None
#######################################
usage () {
    echo "Usage: hamming.sh <string1> <string2>"
}

#######################################
# Calculate Hamming distance
# Arguments:
#   left: left string
#   right: right string
# Returns:
#   Distance (number)
#######################################
hamming () {
    local left=$1
    local right=$2
    local distance=0

    while ((${#left} > 0)); do
        # Compare the first characters
        if [[ "${left:0:1}" != "${right:0:1}" ]]; then
            (( distance++ ))
        fi
        # Remove the first characters before next loop
        left=${left:1}
        right=${right:1}
    done
    echo "${distance}"
}

#######################################
# Main function, arguments validation and
# calling the actual calculation
# Arguments:
#   left: left string
#   right: right string
# Returns:
#   None
#######################################
main () {
    local left=$1
    local right=$2

    if (( $# != 2)); then
        usage
        exit 1
    fi

    if [[ -z "${left}" && -n "${right}" ]]; then
        echo "left strand must not be empty"
        exit 1
    elif [[ -n "${left}" && -z "${right}" ]]; then
        echo "right strand must not be empty"
        exit 1
    elif (( ${#left} != ${#right} )); then
        echo "left and right strands must be of equal length"
        exit 1
    else
        hamming "$left" "$right"
    fi
}

main "$@"
