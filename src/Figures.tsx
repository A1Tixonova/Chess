import React from 'react';

interface IPieces {
  image: string;
  x: number;
  y: number;
}

let pieces: IPieces[] = [];

for (let i = 0; i < 8; i++) {
  pieces.push({ image: 'figgures/pawn.png', x: i, y: i });
}
console.log(pieces);

const Figures = () => {
  return <div></div>;
};

export default Figures;
