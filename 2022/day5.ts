import { readData } from "./helper";

(async () => {
  const lines = await readData(5);
  const origStacks: string[][] = new Array(9).fill(null).map((_) => []);
  const boxes = lines.slice(0, 8).reverse();
  for (const row of boxes) {
    for (const [i, stack] of origStacks.entries()) {
      const box = row[i * 4 + 1] as string;
      if (!"[] ".includes(box)) {
        stack.push(box);
      }
    }
  }

  let stacks: string[][] = JSON.parse(JSON.stringify(origStacks));
  const commands = lines.slice(10);
  for (const command of commands) {
    const [_, numStr, __, fromStr, ___, toStr] = command.split(" ") as string[];
    const num = Number(numStr);
    const from = Number(fromStr) - 1;
    const to = Number(toStr) - 1;
    const crane = stacks[from]?.splice(-num).reverse() as string[];
    stacks[to]?.push(...crane);
  }
  const part1 = stacks.map((v) => v.pop()).join("");
  console.log(`Part 1: ${part1}`);

  stacks = JSON.parse(JSON.stringify(origStacks));
  for (const command of commands) {
    const [_, numStr, __, fromStr, ___, toStr] = command.split(" ") as string[];
    const num = Number(numStr);
    const from = Number(fromStr) - 1;
    const to = Number(toStr) - 1;
    const crane = stacks[from]?.splice(-num) as string[];
    stacks[to]?.push(...crane);
  }
  const part2 = stacks.map((v) => v.pop()).join("");
  console.log(`Part 2: ${part2}`);
})();
