import { readData } from "./helper";

class File {
  name: string;
  size: number;
  parent: Directory | null;
  constructor(name: string, size: number = 0, parent: Directory | null) {
    this.name = name;
    this.size = size;
    this.parent = parent;
  }
}
class Directory extends File {
  children: Map<string, File | Directory> = new Map();
  createSubDirectory(name: string) {
    if (!this.children.has(name)) {
      // create subdir if it isn't already present
      this.children.set(name, new Directory(name, 0, this));
    }
  }
  addFile(name: string, size: number) {
    if (!this.children.has(name)) {
      // create file if it isn't already present
      this.children.set(name, new File(name, size, this));
    }
  }
  calcSize(): number {
    let size = 0;
    for (const el of this.children.values()) {
      if (el instanceof Directory) {
        el.calcSize();
        size += el.size;
      } else {
        size += el.size;
      }
    }
    this.size = size;
    return size;
  }
}

function findDirectories(
  test: (dir: Directory) => boolean,
  start: Directory,
  list: Array<Directory>
) {
  // test start dir and add to list if true
  if (test(start)) {
    list.push(start);
  }
  // recurse through children
  start.children.forEach((val) => {
    if (val instanceof Directory) {
      findDirectories(test, val, list);
    }
  });
  return list;
}

(async () => {
  const lines = await readData(7);

  const rootDir = new Directory("/", 0, null);
  let currentDir: Directory = rootDir;
  for (const line of lines) {
    if (line.startsWith("$")) {
      // This line is a command and `cmd` should equal `ls` or `cd` and `target` should be undefined or dirname, respectively
      const [_, cmd, target] = line.split(" ");
      const targetDir = target as string;
      if (cmd === "cd") {
        if (targetDir === "/") {
          currentDir = rootDir;
        } else if (targetDir === "..") {
          currentDir = currentDir.parent as Directory;
        } else {
          currentDir.createSubDirectory(targetDir);
          currentDir = currentDir.children.get(targetDir) as Directory;
        }
      }
      // if cmd === `ls`, then we should just associate the following items with currentDir anyway
    } else {
      const [sizeOrDir, name] = line.split(" ");
      const fileName = name as string;
      if (sizeOrDir === "dir") {
        currentDir.createSubDirectory(fileName);
      } else {
        const size = Number(sizeOrDir);
        currentDir.addFile(fileName, size);
      }
    }
  }
  // calculate all directory sizes
  rootDir.calcSize();

  // find all directories with size at most 100,000
  const dirs = findDirectories((dir) => dir.size <= 100000, rootDir, []);
  const part1 = dirs.map((dir) => dir.size).reduce((acc, val) => acc + val);
  console.log(`Part 1: ${part1}`);

  const max = 70000000;
  const minFree = 30000000;
  const currFree = max - rootDir.size;
  const needFree = minFree - currFree;
  // find all directories that are at least as big as our needed free space
  const bigEnough = findDirectories((dir) => dir.size >= needFree, rootDir, []);
  bigEnough.sort((a, b) => a.size - b.size); // sort by size ascending
  const dir = bigEnough[0] as Directory;
  const part2 = dir.size; // first item is smallest
  console.log(`Part 2: ${part2}`);
})();
