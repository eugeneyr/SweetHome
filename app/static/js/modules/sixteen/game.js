var Direction = {
    RIGHT: 'right',
    LEFT: 'left',
    UP: 'up',
    DOWN: 'down'
};

function Tile(value, x, y) {
    this.value = value;
    this.x = 0;
    this.y = 0;
}

Tile.prototype.merge = function (otherTile) {
    if (otherTile && otherTile.value == this.value) {
        otherTile.value = 0;
        this.value *= 2;
    }
};

Tile.prototype.canMergeWith = function (otherTile) {
    if (otherTile && otherTile.value == this.value) {
        otherTile.value = 0;
        this.value *= 2;
    }
};

function Board() {
    this.width = 4;
    this.height = 4;
    this.board = [
        [null, null, null, null],
        [null, null, null, null],
        [null, null, null, null],
        [null, null, null, null]
    ];
    return this;
}


Board.prototype.clear = function () {
    this.board = [
        [null, null, null, null],
        [null, null, null, null],
        [null, null, null, null],
        [null, null, null, null]
    ];
};

Board.prototype.mush = function (direction) {
    switch (direction) {
        case Direction.RIGHT:
            this.mushRight();
            break;
        case Direction.LEFT:
            this.mushLeft();
            break;
        case Direction.UP:
            this.mushUp();
            break;
        case Direction.DOWN:
            this.mushDown();
            break;
    }
};


Board.prototype.mushDown = function () {
    for (var i = 0; i < this.width; i++) {
        var empty = 3;
        while (1) {
            while (empty >= 0) {
                if (!this.board[i][empty]) {
                    break;
                }
                empty--;
            }
            if (empty > 0) {
                var filled = empty - 1;
                while (filled >= 0) {
                    if (this.board[i][filled]) {
                        break;
                    }
                    filled--;
                }
                if (filled >= 0) {
                    this.board[i][empty] = this.board[i][filled];
                    this.board[i][filled] = null;
                }
                empty--;
            }
            if (empty <= 0) {
                break;
            }
        }
    }
};

Board.prototype.mushLeft = function () {
    for (var j = 0; j < this.height; j++) {
        var empty = 0;
        while (1) {
            while (empty < 4) {
                if (!this.board[empty][j]) {
                    break;
                }
                empty++;
            }
            if (empty < 4) {
                var filled = empty + 1;
                while (filled < 4) {
                    if (this.board[filled][j]) {
                        break;
                    }
                    filled++;
                }
                if (filled < 4) {
                    this.board[empty][j] = this.board[filled][j];
                    this.board[filled][j] = null;
                }
                empty++;
            }
            if (empty > 3) {
                break;
            }
            console.log('empty:', empty);
        }
    }
};

Board.prototype.mushUp = function () {
    for (var i = 0; i < this.width; i++) {
        var empty = 0;
        while (1) {
            while (empty < 4) {
                if (!this.board[i][empty]) {
                    break;
                }
                empty++;
            }
            if (empty < 4) {
                var filled = empty + 1;
                while (filled < 4) {
                    if (this.board[i][filled]) {
                        break;
                    }
                    filled++;
                }
                if (filled < 4) {
                    // drag it to the left
                    this.board[i][empty] = this.board[i][filled];
                    this.board[i][filled] = null;
                }
                empty++;
            }
            if (empty > 3) {
                break;
            }
            console.log('empty:', empty);
        }
    }
};

Board.prototype.mushRight = function () {
    for (var j = 0; j < this.height; j++) {
        var empty = 3;
        while (1) {
            while (empty >= 0) {
                if (!this.board[empty][j]) {
                    break;
                }
                empty--;
            }
            if (empty > 0) {
                var filled = empty - 1;
                while (filled >= 0) {
                    if (this.board[filled][j]) {
                        break;
                    }
                    filled--;
                }
                if (filled >= 0) {
                    // drag it to the left
                    this.board[empty][j] = this.board[filled][j];
                    this.board[filled][j] = null;
                }
                empty--;
            }
            if (empty <= 0) {
                break;
            }
        }
    }
};


Board.prototype.draw = function () {
    for (var i = 0; i < this.width; i++) {
        for (var j = 0; j < this.height; j++) {
            var elem = document.getElementById('tile_' + i + '_' + j);
            if (elem) {
                elem.innerHTML = this.board[j][i] ? this.board[j][i].value : '&nbsp;';
            }
        }
    }
};

Board.prototype.rollDice = function () {
    var emptyCells = [];
    for (var i = 0; i < this.width; i++) {
        for (var j = 0; j < this.height; j++) {
            if (!this.board[j][i]) {
                emptyCells[emptyCells.length] = {x: i, y: j};
            }
        }
    }
    console.log(emptyCells);
    var pos = Math.floor(Math.random() * emptyCells.length);
    var cell = emptyCells[pos];
    this.board[cell.y][cell.x] = new Tile(2);
};
