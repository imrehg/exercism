// Package twofer provides a nice way of sharing.
package twofer

import "fmt"

// ShareWith provides you with a handy feedback on how to share.
func ShareWith(name string) string {
	if name == "" {
		name = "you"
	}
	return fmt.Sprintf("One for %s, one for me.", name)
}
