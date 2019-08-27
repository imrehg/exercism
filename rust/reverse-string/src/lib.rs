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
    UnicodeSegmentation::graphemes(input, true).rev().collect::<String>()
}
