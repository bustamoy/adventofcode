import { readData } from "./helper";

function getPriority(item: string) {
  const priority = item.charCodeAt(0);
  if (priority >= "a".charCodeAt(0)) {
    return priority - 96;
  } else {
    return priority - 38;
  }
}

(async () => {
  const sacks = await readData(3);

  let total = 0;
  for (const sack of sacks) {
    const comp1 = new Set(sack.slice(0, sack.length / 2));
    const comp2 = new Set(sack.slice(-sack.length / 2));
    const overlap = new Set([...comp1].filter((i) => comp2.has(i)));
    const overlaps = [...overlap]
      .map(getPriority)
      .reduce((acc, val) => acc + val);
    total += overlaps;
  }

  const part1 = total;
  console.log(`Part 1: ${part1}`);

  total = 0;
  const sacksCopy = sacks.slice();
  while (sacksCopy.length > 0) {
    const comp1 = new Set(sacksCopy.pop());
    const comp2 = new Set(sacksCopy.pop());
    const comp3 = new Set(sacksCopy.pop());
    const overlap12 = new Set([...comp1].filter((i) => comp2.has(i)));
    const overlap = new Set([...overlap12].filter((i) => comp3.has(i)));
    const overlaps = [...overlap]
      .map(getPriority)
      .reduce((acc, val) => acc + val);
    total += overlaps;
  }

  const part2 = total;
  console.log(`Part 2: ${part2}`);
})();
