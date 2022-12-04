const fs = require("fs");
const lines = fs.readFileSync("./input.txt", "utf-8").split("\n");

function overlaps(first, second) {
  // Contained just means one range is wholely inside another's range.
  const contained = (first.min <= second.min && first.max >= second.max) || (second.min <= first.min && second.max >= first.max);

  // Overlapped means just one end is inside the other's range, and vice versa.
  const overlapped = (first.min <= second.max && first.min >= second.min) || (first.max <= second.max && first.max >= second.min)
    || (second.min <= first.max && second.min >= first.min) || (second.max <= first.max && second.max >= first.min);

  return [contained, overlapped];
}

let fullyContainedPairs = 0;
let overlappedPairs = 0;

for (const line of lines) {
  const [first, second] = line.split(",");
  const [firstMin, firstMax] = first.split("-").map(s => parseInt(s));
  const [secondMin, secondMax] = second.split("-").map(s => parseInt(s));

  const firstObj = { min: firstMin, max: firstMax };
  const secondObj = { min: secondMin, max: secondMax };
  const [contained, overlapped] = overlaps(firstObj, secondObj);

  if (contained)
    fullyContainedPairs++;

  if (overlapped)
    overlappedPairs++;
}

console.log(fullyContainedPairs);
console.log(overlappedPairs);
