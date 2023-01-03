import { readData } from "./helper";

(async () => {
  const lines = await readData(9);

  const moves: string[] = [];
  for (const line of lines) {
    const [dir, numStr] = line.split(" ");
    const num = Number(numStr);
    moves.push(...new Array(num).fill(dir));
  }

  let hx = 0;
  let hy = 0;
  let tx = 0;
  let ty = 0;
  let dx;
  let dy;
  const positions = new Set();
  positions.add(`${tx},${ty}`);

  for (const dir of moves) {
    dx = 0;
    dy = 0;
    if (dir === "U") {
      dy = 1;
    } else if (dir === "R") {
      dx = 1;
    } else if (dir === "D") {
      dy = -1;
    } else {
      dx = -1;
    }

    if ((hx - tx === dx && dx != 0) || (hy - ty === dy && dy != 0)) {
      // head is moving further away from tail
      if (Math.abs(hx - tx) + Math.abs(hy - ty) === 1) {
        // tail & head are orthogonal so move in same direction
        tx += dx;
        ty += dy;
      } else {
        // tail & head are diagonal so move into previous head location
        tx = hx;
        ty = hy;
      }
    }

    positions.add(`${tx},${ty}`);

    // move head
    hx += dx;
    hy += dy;
  }

  const part1 = positions.size;
  console.log(`Part 1: ${part1}`);

  const part2 = undefined;
  console.log(`Part 2: ${part2}`);
})();
