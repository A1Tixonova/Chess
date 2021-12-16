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
        if ((i === 0 && j === 7) || (i === 7 && j === 7)) {
          board.push(<Tile number={num} image="../assets/r_b.png" />);
        } else if ((i === 1 && j === 7) || (i === 6 && j === 7)) {
          board.push(<Tile number={num} image="../assets/n_b.png" />);
        } else if ((i === 2 && j === 7) || (i === 5 && j === 7)) {
          board.push(<Tile number={num} image="../assets/b_b.png" />);
        } else if (i === 4 && j === 7) {
          board.push(<Tile number={num} image="../assets/k_b.png" />);
        } else if (i === 3 && j === 7) {
          board.push(<Tile number={num} image="../assets/q_b.png" />);
        } else if ((i === 0 && j === 0) || (i === 7 && j === 0)) {
          board.push(<Tile number={num} image="../assets/r_w.png" />);
        } else if ((i === 1 && j === 0) || (i === 6 && j === 0)) {
          board.push(<Tile number={num} image="../assets/n_w.png" />);
        } else if ((i === 2 && j === 0) || (i === 5 && j === 0)) {
          board.push(<Tile number={num} image="../assets/b_w.png" />);
        } else if (i === 3 && j === 0) {
          board.push(<Tile number={num} image="../assets/q_w.png" />);
        } else if (i === 4 && j === 0) {
          board.push(<Tile number={num} image="../assets/k_w.png" />);
        } else {
          board.push(<Tile number={num} image={image} />);
        }
      } else {
        board.push(<Tile number={num} image={image} />);
      }
    }
  }
  console.log({ ...board });
  return <div id="chessboard">{board}</div>;
};

export default ChessBoard;
