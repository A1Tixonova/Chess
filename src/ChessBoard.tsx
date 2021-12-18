import React from 'react';
import Tile from './Tile';
import './ChessBoard.css';

const verticalAxis: string[] = ['1', '2', '3', '4', '5', '6', '7', '8'];
const horizontalAxis: string[] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];

const figures = require('./firstboard.json');
//type Position = { x: number, y: number }

function grabPiece(e: React.MouseEvent) {
  console.log(e.target);
}

const ChessBoard = () => {
  let board = [];
  let image = undefined;
  for (let j = verticalAxis.length - 1; j >= 0; j--) {
    for (let i = 0; i < horizontalAxis.length; i++) {
      let num = j + i + 2;
      let res = horizontalAxis[i] + verticalAxis[j];
      if (res in figures) {
        let t = figures[res];
        let name = `../assets/${t[0]}_${t[1]}.png`;
        board.push(<Tile number={num} image={name} />);
      } else {
        board.push(<Tile number={num} image={image} />);
      }
    }
  }

  return (
    <div onMouseDown={(e) => grabPiece(e)} id="chessboard">
      {board}
    </div>
  );
};

export default ChessBoard;
