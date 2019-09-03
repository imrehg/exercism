// Provide the `graphemes` method for unicode cases
use unicode_segmentation::UnicodeSegmentation;

/// Reverses a string
///
/// # Examples
///
/// ```
/// let hello = "hello";
///
/// assert_eq!(reverse_string::reverse(hello), "olleh");
/// ```
pub fn reverse(input: &str) -> String {
    input.graphemes(true).rev().collect::<String>()
}
