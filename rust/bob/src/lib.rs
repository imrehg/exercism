#[macro_use]
extern crate lazy_static;
use regex::RegexSet;

/// Chatting with Bob
///
/// # Examples
///
/// A question:
/// ```
/// let question = "Cuppa tea?";
/// assert_eq!(bob::reply(question), "Sure.");
/// ```
///
/// A yelled question:
/// ```
/// let yelled_question = "SIX SPOONS OF SUGAR?";
/// assert_eq!(bob::reply(yelled_question), "Calm down, I know what I'm doing!");
/// ```
///
/// Yelling at Bob:
/// ```
/// let yell = "ENOUGH!";
/// assert_eq!(bob::reply(yell), "Whoa, chill out!");
/// ```
///
/// The silent treatment:
/// ```
/// let silent = "     ";
/// assert_eq!(bob::reply(silent), "Fine. Be that way!");
/// ```
////
/// Everything else:
/// ```
/// let normal_line = "I'd prefer coffee instead.";
/// assert_eq!(bob::reply(normal_line), "Whatever.");
/// ```
pub fn reply(message: &str) -> &str {
    lazy_static! {
        static ref SET: RegexSet = RegexSet::new(&[
        // Matching a question that was yelled at us (there are some letters and all are capitals, finished witn a question mark)
        r"^\s*[^a-z]*[A-Z]+[^a-z]*\?\s*$",
        // Matching when we are yelled at (at least one capital letter, and the rest is not lowercase)
        r"^\s*[^a-z]*[A-Z]+[^a-z]*\s*$",
        // Mathing a question (any word caracters and last punctuation is a question mark)
        r"^.*\w?.*\?\s*$",
        // Matching when there's nothing being said
        r"^\s*$",
        ]).unwrap();
    }
    let _patterns: Vec<_> = SET.matches(message).into_iter().collect();
    match _patterns.first() {
        Some(0) => { "Calm down, I know what I'm doing!" }
        Some(1) => { "Whoa, chill out!" }
        Some(2) => { "Sure." }
        Some(3) => { "Fine. Be that way!" }
        _ => { "Whatever." }
    }
}
