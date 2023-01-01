import { readData } from "./helper";

(async () => {
  const elves = await readData(1, "\n\n");
  const elfCals = elves.map((elf) =>
    elf
      .split("\n")
      .map(Number)
      .reduce((sum, v) => sum + v)
  );
  elfCals.sort();
  const part1 = elfCals.slice(-1).pop();
  console.log(`Part 1: ${part1}`);
  const part2 = elfCals.slice(-3).reduce((sum, v) => sum + v);
  console.log(`Part 2: ${part2}`);
})();
