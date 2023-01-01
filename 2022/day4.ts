import { readData } from "./helper";

function getSections(assignment: string): number[] {
  const limits = assignment.split("-").map(Number);
  const min = limits[0] as number;
  const max = limits[1] as number;
  if (min === max) {
    return [min];
  } else {
    return new Array(max - min + 1).fill(0).map((_, idx) => idx + min);
  }
}

(async () => {
  const pairs = await readData(4);

  let total = 0;
  for (const pair of pairs) {
    const assignments = pair.split(",");
    const section1 = getSections(assignments[0] as string);
    const section1Set = new Set(section1);
    const section2 = getSections(assignments[1] as string);
    const section2Set = new Set(section2);
    if (
      section1.every((val) => {
        return section2Set.has(val);
      }) ||
      section2.every((val) => {
        return section1Set.has(val);
      })
    ) {
      total += 1;
    }
  }

  const part1 = total;
  console.log(`Part 1: ${part1}`);

  total = 0;
  for (const pair of pairs) {
    const assignments = pair.split(",");
    const section1 = getSections(assignments[0] as string);
    const section1Set = new Set(section1);
    const section2 = getSections(assignments[1] as string);
    const section2Set = new Set(section2);
    if (
      section1.some((val) => {
        return section2Set.has(val);
      }) ||
      section2.some((val) => {
        return section1Set.has(val);
      })
    ) {
      total += 1;
    }
  }
  const part2 = total;
  console.log(`Part 2: ${part2}`);
})();
