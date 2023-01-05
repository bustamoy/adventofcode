import { readData } from "./helper";

readData(10).then((lines) => {
  (() => {
    const signals: number[] = [];
    let x = 1;
    for (const line of lines) {
      const [cmd, valStr] = line.split(" ");
      const val = Number(valStr);
      signals.push(x * (signals.length + 1));
      if (cmd === "addx") {
        signals.push(x * (signals.length + 1));
        x += val;
      }
    }
    const part1: number =
      (signals[19] as number) +
      (signals[59] as number) +
      (signals[99] as number) +
      (signals[139] as number) +
      (signals[179] as number) +
      (signals[219] as number);
    console.log(`Part 1: ${part1}`);
  })();

  (() => {
    const signals: number[] = [];
    let x = 1;
    for (const line of lines) {
      const [cmd, valStr] = line.split(" ");
      const val = Number(valStr);
      signals.push(x);
      if (cmd === "addx") {
        signals.push(x);
        x += val;
      }
    }

    let output = "";
    for (const [pos, x] of signals.entries()) {
      const linepos = pos % 40;
      if (Math.abs(x - linepos) <= 1) {
        output += "#";
      } else {
        output += ".";
      }
    }

    console.log(`Part 2:`);
    console.log(output.slice(0, 40));
    console.log(output.slice(40, 80));
    console.log(output.slice(80, 120));
    console.log(output.slice(120, 160));
    console.log(output.slice(160, 200));
    console.log(output.slice(200, 240));
  })();
});
