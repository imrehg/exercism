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
    return input.chars().rev().collect::<String>();
}
