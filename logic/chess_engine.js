function create_board (name) {
	let data = {'a1': 'rw', 'a2': 'pw', 'b1': 'nw', 'b2': 'pw', 'c1': 'bw', 'c2': 'pw', 'd1': 'qw', 'd2': 'pw', 'e1': 'kw', 'e2': 'pw', 'f1': 'bw', 'f2': 'pw', 'g1': 'nw', 'g2': 'pw', 'h1': 'rw', 'h2': 'pw', 'a8': 'rb', 'a7': 'pb', 'b8': 'nb', 'b7': 'pb', 'c8': 'bb', 'c7': 'pb', 'd8': 'qb', 'd7': 'pb', 'e8': 'kb', 'e7': 'pb', 'f8': 'bb', 'f7': 'pb', 'g8': 'nb', 'g7': 'pb', 'h8': 'rb', 'h7': 'pb'};
	localStorage.setItem(name, JSON.stringify(data));
};

function write_turn(a, b, name, tcol) {
  let tuple = to_tuple(a);
  let a1 = tuple[0];
  let a2 = tuple[1];
  tuple = to_tuple(b);
  let b1 = tuple[0];
  let b2 = tuple[1];
  let x = b1 - a1;
  let y = b2 - a2;
  if ((a1 < 0) || (a1 > 7) || (a2 < 0) || (a2 > 7) || (b1 < 0) || (b1 > 7) || (b2 < 0) || (b2 > 7)) {
    return false;
  }
  var cur_board = JSON.parse(localStorage.getItem(name));
  if (!(a in cur_board)) {
    return false;
  }

  let turn = check_turn(cur_board, a, b);
  let color = cur_board[a][1];
  if (tcol != color) return false;
  if (cur_board[a][0] == 'k' && turn!=3) {

    let l = get_king_turns(a1, a2).filter(function(x){
      return !(check_checkmate(cur_board, x, color))
    });
    if (b in l){
      let temp = cur_board[a];
      delete cur_board[a];
      cur_board[b] = temp;
    }
  } else {
    let kp = king_pos(cur_board, color);

    if (check_checkmate(cur_board, kp, color)) {
      let temp = cur_board[a];
      delete cur_board[a];
      cur_board[b] = temp;
      if (check_checkmate(cur_board, kp, color)) {
        return false;
      }
    } else {
        if (turn == 1) {
          let temp = cur_board[a];
          delete cur_board[a];
          cur_board[b] = temp;
        } else if (turn == 2) {
          let ind = from_tuple(a1 + x, a2);
          let en = cur_board[ind];
          if (en[0] == cur_board[a][0] && en[1] != cur_board[a][1]) {
            let temp = cur_board[a];
            delete cur_board[a];
            delete cur_board[ind];
            cur_board[b] = temp;
          }
        } else if (turn == 3) {
          if (cur_board[a][1] == 'w') {
            if (x > 0) {
              a1 = 'h1';
              a2 = 'f1';
            } else {
              a1 = 'a1';
              a2 = 'd1';
            }
          } else {
            if (x > 0) {
              a1 = 'h8';
              a2 = 'f8';
            } else {
              a1 = 'a8';
              a2 = 'd8';
            }
          }

          let temp = cur_board[a1];
          delete cur_board[a1];
          cur_board[a2] = temp;

          temp = cur_board[a];
          delete cur_board[a];
          cur_board[b] = temp;
          if (check_checkmate(cur_board, b, color)) return false;
        } else {
          return false;
        }
      }
    }

  localStorage.setItem(name, JSON.stringify(cur_board));
  return true;
}

function get_king_turns(x, y) {
  let t = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x - 1, y], [x + 1, y], [x - 1, y + 1], [x, y + 1], [x + 1, y + 1]];
  let nt = t.filter(function(i) {return (i[0] < 7 && i[0] >= 0 && i[1] < 7 && i[1] >= 0);});

  return t.map(function(i) {return from_tuple(i[0], i[1]);});
}

function to_tuple(pos) {
  return [pos[0].charCodeAt(0) - 97, Number(pos[1])-1];
}

function from_tuple(a, b) {
  return String.fromCharCode(a+97) + String(b + 1);
}

function king_pos(board, color) {
  let pos = 0;
  let col = 'k' + color;
  for (let key in board) {
    if (board[key] == col) pos = key;
  }
  return pos;
}

function check_checkmate(board, pos, col) {
  for (let i in board) {
    if (board[i][1] != col && check_turn(board, i, pos)) return true;
  }
  return false;
}

function check_turn(board, a, b) {
  let tuple = to_tuple(a);
  let a1 = tuple[0];
  let a2 = tuple[1];
  tuple = to_tuple(b);
  let b1 = tuple[0];
  let b2 = tuple[1];
  let x = b1 - a1;
  let y = b2 - a2;
  let fig = board[a];

  if (b in board && board[b][1] == fig[1]) return 0;

  if (fig == 'pw') {
		if (y == 1 && x == 0 && !(b in board)) {
			return 1;
		}
		if (y == 2 && x == 0 && a2 == 1 && !(b in board)) {
			return 1;
		}
		if (y == 1 && (x == -1 || x == 1) && (b in board) && board[b][1] == 'b') {
			return 1;
		}
		if (y == 1 && (x == 1 || x == -1) && board[from_tuple(b1, b2 - 1)] == 'pb') {
			return 2;
		}
	}

  if (fig == 'pb') {
		if (y == -1 && x == 0 && !(b in board)) {
			return 1;
		}
		if (y == -2 && x == 0 && a2 == 6 && !(b in board)) {
			return 1;
		}
		if (y == -1 && (x == -1 || x == 1) && (b in board) && board[b][1] == 'w') {
			return 1;
		}
		if (y == -1 && (x == 1 || x == -1) && board[from_tuple(b1, b2 + 1)] == 'pw') {
			return 2;
		}
	}

  	if (fig == 'rb' || fig == 'rw' || fig == 'qw' || fig == 'qb') {
      let t1 = all(range(min(a1, b1)+1, max(a1, b1)).map(function(t) {
        return !(from_tuple(t, a2) in board);}));
      let t2 = all(range(min(a2, b2)+1, max(a2, b2)).map(function(t) {
        return !(from_tuple(a1, t) in board);}));
  		if (y == 0 && t1 || x == 0 && t2) {
        return 1;
      }
  	}

  if (fig == 'bb' || fig == 'bw' || fig == 'qw' || fig == 'qb') {
    let t1 = all(range(1, x).map(function(t) {
        return !(from_tuple(a1 + t, a2 + t) in board);}));
    let t2 = all(range(1, -x).map(function(t) {
        return !(from_tuple(a1 - t, a2 - t) in board);}));
    let t3 = all(range(1, x).map(function(t) {
        return !(from_tuple(a1 + t, a2 - t) in board);}));
    let t4 = all(range(1, -x).map(function(t) {
        return !(from_tuple(a1 - t, a2 + t) in board);}));
    if (x==y && x > 0 && t1 || x==y && x < 0 && t2 || x==-y && x > 0 && t3 || x==-y && x > 0 && t4) {
      return 1;
    }
  }

  if (fig == 'nb' || fig == 'nw') {
		if (abs(x) == 2 && abs(y) == 1 || abs(x) == 1 && abs(y) == 2) {
			return 1;
		}
	}

	if (fig == 'kw' || fig == 'kb') {
		if (abs (x) <= 1 && abs (y) <= 1) {
			return 1;
		}
	}

  if (fig == 'kw') {
    if (abs(x)==2 && y==0 && a2 == 0) {
      let t = min(a1, b1), d = max(a1, b1);
      a1 = t;
      b1 = d;
      if (!(from_tuple(0, a1+1) in board) && !(from_tuple(0, a1+2) in board)) {
        if (x>0 && ('h1' in board) && board['h1']=='rw' || x<0 && ('a1' in board) && board['a1']=='rw') return 3;
      }
    }
  }

  if (fig == 'kb') {
    if (abs(x)==2 && y==0 && a2 == 7) {
      let t = min(a1, b1), d = max(a1, b1);
      a1 = t;
      b1 = d;
      if (!(from_tuple(7, a1+1) in board) && !(from_tuple(7, a1+2) in board)) {
        if (x>0 && ('h8' in board) && board['h8']=='rb' || x<0 && ('a8' in board) && board['a8']=='rb') return 3;
      }
    }
  }

  return 0;
}

function all(a) {
  if (a.length == 0) {
    return false;
  }
  return a.reduce(function(p,n) {return p && n;});
}

function abs(a) {
  return a > 0 ? a : -a;
}

function min(a, b) {
  return a < b ? a : b;
}

function max(a, b) {
  return a < b ? b : a;
}

function range(a, b) {
  let arr = [];
  for (let i = a; i < b; ++i) arr.push(i);
  return arr;
}

function print_board(name) {
  let board = JSON.parse(localStorage.getItem(name));
  for (let i = 0; i < 8; i++) {
    let ar = '';
    for (let j = 0; j < 8; ++j) {
      let t = from_tuple(j, 7 - i);
      if (t in board) ar += board[t]+' ';
      else ar += '** '
    }
    console.log(ar);
  }

}

// localStorage.setItem(name, JSON.stringify(cur_board));
// let obj1 = JSON.parse(localStorage.getItem('myStorage'));

//let name = 'firstboard';
//create_board(name);
//write_turn('b1', 'c3', name, 'w');
//print_board(name);