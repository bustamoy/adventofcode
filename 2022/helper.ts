import * as fs from "fs/promises";

export async function readData(
  day: number,
  sep: string = "\n"
): Promise<string[]> {
  const data = await fs.readFile(`day${day}.data`, { encoding: "utf8" });
  return data.split(sep);
}
