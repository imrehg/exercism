#!/usr/bin/env bash

main() {
    local name=$1
    echo "One for ${name:-you}, one for me."
}

main "$@"