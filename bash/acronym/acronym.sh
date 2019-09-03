#!/usr/bin/env bash
#
# Acronym calculation

#######################################
# Calculate acronym from an input string
# Arguments:
#   input: an input string
# Returns:
#   string of upper case acronym
#######################################
main () {
    local input=$1
    local result=""
    local newword="true"
    local char
    local -i iterator
    for (( iterator = 0; iterator < ${#input}; iterator++ )); do
        # Look at the next character
        char="${input:$iterator:1}"
        # If we are at a beginning of a word, look for a letter
        if [[ "${newword}" = "true" ]] ; then
            case "${char}" in
                [a-zA-Z])
                    newword=false
                    # Found a new character for our acronym,
                    # add it uppercase to future return value
                    result+="${char^}"
            esac
        else
            # Check if we can start looking for a new initial
            case "${char}" in
                ' '|'-')
                    newword=true
            esac
        fi
    done
    echo "${result}"
}

# call main with all of the positional arguments
main "$@"
