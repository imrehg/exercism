/**
 * Given a moment, determine the moment that would be
 * after a gigasecond has passed.
 * @param {Date} start - The starting time
 * @return {Date} The date 1 giga-second after start
 */
export const gigasecond = start => {
  return new Date(start.getTime() + 1e12); // the delta is in ms
};
