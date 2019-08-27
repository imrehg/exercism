/**
 * Find resistor value by color code, as per
 * https://en.wikipedia.org/wiki/Electronic_color_code
 * @param {string[n]} colorBands - The array of color bands to look up (lowercase).
 * @return {integer} The corresponding resistance value.
 * @throws Will throw an error if any of the color codes are unknown (through colorCode)
 */
export const value = colorBands => {
  let totalResistorValue = 0;
  let band;
  for (band of colorBands) {
    // Shift order of magnitude by each band processed
    totalResistorValue *= 10;
    // Calculate value of current band
    totalResistorValue += colorCode(band);
  }
  return totalResistorValue;
};

/**
 * Find resistor value by color code, as per
 * https://en.wikipedia.org/wiki/Electronic_color_code
 * @param {string} color - The color to look up (lowercase).
 * @return {integer} The corresponding resistance value.
 * @throws Will throw an error if color code is unknown.
 */
export const colorCode = color => {
  let resistorValue = COLORS.indexOf(color);
  if (resistorValue === -1) {
    throw new Error(`Unknown resistor color: ${color}`);
  }
  return resistorValue;
};

/** The list of colors in order of increasing value */
export const COLORS = [
  "black",
  "brown",
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "violet",
  "grey",
  "white"
];
