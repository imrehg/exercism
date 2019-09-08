#!/usr/bin/env bash

#######################################
# Calculate if a number is an Armstrong Number
# Arguments:
#   candidate: the candidate number
# Returns:
#   boolean for the Armstrong Number check
#######################################
main () {
    local candidate=$1
    local -i iterator
    local -i accumulator=0
    local -i num_digits=${#candidate}
    for (( iterator = 0; iterator < num_digits; iterator++ )); do
        accumulator+=$((${candidate:iterator:1}**num_digits))
    done
    if [[ "${candidate}" == "${accumulator}" ]]; then
        echo "true"
    else
        echo "false"
    fi
}

main "$@"
