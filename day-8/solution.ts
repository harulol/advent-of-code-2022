import fs from "fs";
const lines: string[] = fs.readFileSync("./input.txt", "utf-8").split("\r\n");

const gridWidth = lines[0].length;
const gridHeight = lines.length;

let visibleTrees = 0;
let highestScenic = 0;

function check(x: number, y: number): boolean {
  const height = parseInt(lines[y][x]);
  let left = true, right = true, top = true, bottom = true;

  // Check same row from the left.
  for (let i = 0; i < x; i++)
    if (parseInt(lines[y][i]) >= height) {
      left = false;
      break;
    }

  // Check same row from the right.
  for (let i = x + 1; i < gridWidth; i++)
    if (parseInt(lines[y][i]) >= height) {
      right = false;
      break;
    }

  // Check same column from the top.
  for (let i = 0; i < y; i++)
    if (parseInt(lines[i][x]) >= height) {
      top = false;
      break;
    }

  // Check same column from the bottom.
  for (let i = y + 1; i < gridHeight; i++)
    if (parseInt(lines[i][x]) >= height) {
      bottom = false;
      break;
    }

  return left || right || top || bottom;
}

function calculateScenic(x: number, y: number): number {
  let top = 0, bottom = 0, left = 0, right = 0;
  const height = parseInt(lines[y][x]);

  // Count looking up.
  for (let i = y - 1; i >= 0; i--) {
    top++;
    if (parseInt(lines[i][x]) >= height)
      break;
  }

  // Count looking down.
  for (let i = y + 1; i < gridHeight; i++) {
    bottom++;
    if (parseInt(lines[i][x]) >= height)
      break;
  }

  // Count looking left.
  for (let i = x - 1; i >= 0; i--) {
    left++;
    if (parseInt(lines[y][i]) >= height)
      break;
  }

  // Count looking right.
  for (let i = x + 1; i < gridWidth; i++) {
    right++;
    if (parseInt(lines[y][i]) >= height)
      break;
  }

  return top * bottom * left * right;
}

for (let y = 0; y < gridHeight; y++) {
  for (let x = 0; x < gridWidth; x++) {
    if (y == 0 || y == gridHeight - 1 || x == 0 || x == gridWidth - 1 || check(x, y))
      visibleTrees++;

    highestScenic = Math.max(highestScenic, calculateScenic(x, y));
  }
}

console.log(visibleTrees);
console.log(highestScenic);
