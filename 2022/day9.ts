import { readData } from "./helper";

(async () => {
  const lines = await readData(9);

  const moves: string[] = [];
  for (const line of lines) {
    const [dir, numStr] = line.split(" ");
    const num = Number(numStr);
    moves.push(...new Array(num).fill(dir));
  }

  const positions = new Set<string>();

  let hx = 0;
  let hy = 0;
  let tx = 0;
  let ty = 0;
  let dx;
  let dy;
  positions.add(`${tx},${ty}`);
  for (const dir of moves) {
    dx = 0;
    dy = 0;
    if (dir.includes("U")) {
      dy = 1;
    } else if (dir.includes("D")) {
      dy = -1;
    }
    if (dir.includes("R")) {
      dx = 1;
    } else if (dir.includes("L")) {
      dx = -1;
    }

    const hxNew = hx + dx;
    const hyNew = hy + dy;
    const xDist = Math.abs(hxNew - tx);
    const yDist = Math.abs(hyNew - ty);
    if (xDist === 2 && yDist === 0) {
      tx += dx;
    } else if (xDist === 0 && yDist === 2) {
      ty += dy;
    } else if ((xDist >= 2 || yDist >= 2) && hxNew != tx && hyNew != ty) {
      tx = hx;
      ty = hy;
    }

    positions.add(`${tx},${ty}`);

    // move head
    hx = hxNew;
    hy = hyNew;
  }

  const part1 = positions.size;
  console.log(`Part 1: ${part1}`);

  const moveKnot = (moves: string[], positions?: Set<string>): string[] => {
    let hx = 0;
    let hy = 0;
    let tx = 0;
    let ty = 0;
    let dx;
    let dy;
    if (positions !== undefined) {
      positions.add(`${tx},${ty}`);
    }
    const nextMoves: string[] = [];
    for (const dir of moves) {
      dx = 0;
      dy = 0;
      if (dir.includes("U")) {
        dy = 1;
      } else if (dir.includes("D")) {
        dy = -1;
      }
      if (dir.includes("R")) {
        dx = 1;
      } else if (dir.includes("L")) {
        dx = -1;
      }

      const hxNew = hx + dx;
      const hyNew = hy + dy;
      const xDist = Math.abs(hxNew - tx);
      const yDist = Math.abs(hyNew - ty);
      if (xDist === 2 && yDist === 0) {
        tx += dx;
        nextMoves.push(dx === 1 ? "R" : "L");
      } else if (xDist === 0 && yDist === 2) {
        ty += dy;
        nextMoves.push(dy === 1 ? "U" : "D");
      } else if ((xDist >= 2 || yDist >= 2) && hxNew != tx && hyNew != ty) {
        nextMoves.push(`${hyNew > ty ? "U" : "D"}${hxNew > tx ? "R" : "L"}`);
        tx += hxNew > tx ? 1 : -1;
        ty += hyNew > ty ? 1 : -1;
      }

      if (positions !== undefined) {
        positions.add(`${tx},${ty}`);
      }

      // move head
      hx = hxNew;
      hy = hyNew;
    }
    return nextMoves;
  };

  const knot1Moves = moves.slice();
  const knot2Moves = moveKnot(knot1Moves);
  const knot3Moves = moveKnot(knot2Moves);
  const knot4Moves = moveKnot(knot3Moves);
  const knot5Moves = moveKnot(knot4Moves);
  const knot6Moves = moveKnot(knot5Moves);
  const knot7Moves = moveKnot(knot6Moves);
  const knot8Moves = moveKnot(knot7Moves);
  const knot9Moves = moveKnot(knot8Moves);
  positions.clear();
  moveKnot(knot9Moves, positions);

  const part2 = positions.size;
  console.log(`Part 2: ${part2}`);
})();
