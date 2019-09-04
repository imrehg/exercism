/**
 * Claculate if a year is a leap year.
 *
 * @param year - The year to check
 * @returns Whether or not the year is a leap
 */
function isLeapYear(year: number): boolean {
  return (year % 100 !== 0 && year % 4 === 0) || year % 400 === 0;
}

export default isLeapYear;
