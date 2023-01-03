import { readData } from "./helper";

(async () => {
  const lines = await readData(8);
  // convert each char into a number
  const rows = lines.slice().map((row) => [...row].map(Number));
  const height = rows.length;
  const width = rows[0]?.length as number;

  // create list of columns by pulling the same index from all rows
  const cols = new Array(width)
    .fill(0)
    .map((_, idx) => rows.map((row) => row[idx]));

  let total = 0;

  // loop through the inner spots
  for (let y = 1; y < height - 1; y++) {
    for (let x = 1; x < width - 1; x++) {
      const row = rows[y] as number[];
      const col = cols[x] as number[];
      const tree = Number(row?.[x]);
      const shorter = (val: number) => val < tree;
      // grab the row and column sections before & after the selected cell
      // order doesn't matter here because we need to check every cell being shorter
      const left = row.slice(0, x);
      const right = row.slice(x + 1);
      const up = col.slice(0, y);
      const down = col.slice(y + 1);
      if (
        left.every(shorter) ||
        right.every(shorter) ||
        up.every(shorter) ||
        down.every(shorter)
      ) {
        total += 1;
      }
    }
  }
  // add the borders
  total += width + width + (height - 2) + (height - 2);
  const part1 = total;
  console.log(`Part 1: ${part1}`);

  const getDistance = (trees: number[], height: number): number => {
    // iterate through all trees in order, stopping when we hit a tree of same or greater height
    for (let i = 0; i < trees.length; i++) {
      if ((trees[i] as number) >= height) {
        return i + 1;
      }
    }
    return trees.length;
  };

  let maxScore = 0;

  // loop through the inner spots again
  for (let y = 1; y < height - 1; y++) {
    for (let x = 1; x < width - 1; x++) {
      const row = rows[y] as number[];
      const col = cols[x] as number[];
      const tree = Number(row?.[x]);
      // grab the row and column sections before & after the selected cell
      // order does matter here because we are counting distance from the selected cell
      // so left and up lists need to be reversed
      const left = row.slice(0, x);
      left.reverse();
      const leftDist = getDistance(left, tree);

      const right = row.slice(x + 1);
      const rightDist = getDistance(right, tree);

      const up = col.slice(0, y);
      up.reverse();
      const upDist = getDistance(up, tree);

      const down = col.slice(y + 1);
      const downDist = getDistance(down, tree);

      const score = leftDist * rightDist * upDist * downDist;
      maxScore = Math.max(maxScore, score);
    }
  }
  const part2 = maxScore;
  console.log(`Part 2: ${part2}`);
})();
