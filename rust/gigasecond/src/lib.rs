use chrono::{DateTime, Duration, Utc};

/// Returns a Utc DateTime one billion seconds after start.
///
/// # Examples
///
/// ```
/// use chrono::prelude::*;
/// let start_date = Utc.ymd(2011, 4, 25).and_hms(0, 0, 0);
///
/// assert_eq!(
///     gigasecond::after(start_date),
///     Utc.ymd(2043, 1, 1).and_hms(1, 46, 40)
/// );
/// ```
pub fn after(start: DateTime<Utc>) -> DateTime<Utc> {
    start + Duration::seconds(1_000_000_000)
}
