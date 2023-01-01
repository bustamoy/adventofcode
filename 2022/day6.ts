import { readData } from "./helper";

(async () => {
  const lines = await readData(6);
  const data = lines[0] as string;
  const window: string[] = [];
  let part1;
  for (const [i, c] of [...data].entries()) {
    window.push(c);
    if (window.length === 4) {
      if (new Set(window).size === window.length) {
        part1 = i + 1;
        break;
      } else {
        window.shift();
      }
    }
  }
  console.log(`Part 1: ${part1}`);

  let part2;
  for (const [i, c] of [...data].entries()) {
    window.push(c);
    if (window.length === 14) {
      if (new Set(window).size === window.length) {
        part2 = i + 1;
        break;
      } else {
        window.shift();
      }
    }
  }
  console.log(`Part 2: ${part2}`);
})();
