import './ChessBoard.css';

interface IProps {
  number: number;
  image?: string;
}

export default function Tile({ number, image }: IProps) {
  if (number % 2 === 0) {
    return (
      <div className="tile black-tile figuresCt">
        {image && (
          <div
            style={{ backgroundImage: `url(${image})` }}
            className="cPiece"
          ></div>
        )}
      </div>
    );
  } else {
    return (
      <div className="tile white-tile figuresCt">
        {image && (
          <div
            style={{ backgroundImage: `url(${image})` }}
            className="cPiece"
          ></div>
        )}
      </div>
    );
  }
}
