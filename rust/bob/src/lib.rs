#[macro_use]
extern crate lazy_static;
use regex::Regex;

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
        // Matching when we are yelled at (at least one capital letter, and the rest is not lowercase)
        static ref YELL: Regex = Regex::new(r"^\s*[^a-z]*[A-Z]+[^a-z]*\s*$").unwrap();
        // Mathing a question (any word caracters and last punctuation is a question mark)
        static ref QUESTION: Regex = Regex::new(r"^.*\w?.*\?\s*$").unwrap();
        // Matching a question that was yelled at us (there are some letters and all are capitals, finished witn a question mark)
        static ref YELL_QUESTION: Regex = Regex::new(r"^\s*[^a-z]*[A-Z]+[^a-z]*\?\s*$").unwrap();
        // Matching when there's nothing being said
        static ref NOTHING: Regex = Regex::new(r"^\s*$").unwrap();
    }
    if YELL_QUESTION.is_match(message) {
        return "Calm down, I know what I'm doing!";
    } else if QUESTION.is_match(message) {
        return "Sure.";
    } else if NOTHING.is_match(message) {
        return "Fine. Be that way!";
    } else if YELL.is_match(message) {
        return "Whoa, chill out!";
    } else {
        return "Whatever.";
    }
}
