import React from 'react';
import Tile from './Tile';
import './ChessBoard.css';

const verticalAxis: any = ['1', '2', '3', '4', '5', '6', '7', '8'];
const horizontalAxis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];

const figures = require('./firstboard.json');

const ChessBoard = () => {
  let board = [];
  let image = undefined;
  for (let j = verticalAxis.length - 1; j >= 0; j--) {
    for (let i = 0; i < horizontalAxis.length; i++) {
      let num = j + i + 2;
      let res = horizontalAxis[i] + verticalAxis[j];
      if (horizontalAxis[i] + verticalAxis[j] in figures) {
        board.push(<Tile number={num} image="../assets/p_w.png" />);
      } else {
        board.push(<Tile number={num} image={image} />);
      }
    }
  }

  return <div id="chessboard">{board}</div>;
};

export default ChessBoard;
