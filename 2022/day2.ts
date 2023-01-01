import { readData } from "./helper";

(async () => {
  const rounds = await readData(2);
  let score = 0;
  const scores = new Map<string, number>();

  scores.set("A X", 1 + 3);
  scores.set("A Y", 2 + 6);
  scores.set("A Z", 3 + 0);
  scores.set("B X", 1 + 0);
  scores.set("B Y", 2 + 3);
  scores.set("B Z", 3 + 6);
  scores.set("C X", 1 + 6);
  scores.set("C Y", 2 + 0);
  scores.set("C Z", 3 + 3);
  for (const round of rounds) {
    score += scores.get(round) as number;
  }

  const part1 = score;
  console.log(`Part 1: ${part1}`);

  score = 0;
  scores.set("A X", 3 + 0);
  scores.set("A Y", 1 + 3);
  scores.set("A Z", 2 + 6);
  scores.set("B X", 1 + 0);
  scores.set("B Y", 2 + 3);
  scores.set("B Z", 3 + 6);
  scores.set("C X", 2 + 0);
  scores.set("C Y", 3 + 3);
  scores.set("C Z", 1 + 6);
  for (const round of rounds) {
    score += scores.get(round) as number;
  }
  const part2 = score;
  console.log(`Part 2: ${part2}`);
})();
