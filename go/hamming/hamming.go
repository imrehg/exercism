// This package provides Hamming distance calculation
package hamming

import (
	"errors"
)

// Distance calculates the Hamming distance of two strings
func Distance(a, b string) (int, error) {
	a_len := len(a)
	b_len := len(b)
	if a_len != b_len {
		return 0, errors.New("The inputs are not equal length!")
	} else {
		distance := 0
		for i := 0; i < a_len; i++ {
			if a[i] != b[i] {
				distance++
			}
		}
		return distance, nil
	}
}
