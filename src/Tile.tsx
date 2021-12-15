import './ChessBoard.css';

interface IProps {
  number: number;
  image?: string;
}

export default function Tile({ number, image }: IProps) {
  if (number % 2 === 0) {
    return <div className="tile black-tile"></div>;
  } else {
    return <div className="tile white-tile"></div>;
  }
}
