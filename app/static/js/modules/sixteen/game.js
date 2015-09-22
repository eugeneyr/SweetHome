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


Board.prototype.mushRight = function () {
    for (var j = 0; j < this.height; j++) {
        var empty = 3;
        while (empty >= 0) {
            while (empty >= 0 && !this.board[empty][j]) {
                empty--;
            }
            if (empty > 0) {
                var filled = empty - 1;
                // drag it to the left
                this.board[empty][j] = this.board[filled][j];
                this.board[filled][j] = null;
            }
        }
    }
};

Board.prototype.mushLeft = function () {
    for (var j = 0; j < this.height; j++) {
        var empty = 0;
        while (empty < 4) {
            while (empty < 4 && !this.board[empty][j]) {
                empty++;
            }
            if (empty < 3) {
                var filled = empty + 1;
                // drag it to the left
                this.board[empty][j] = this.board[filled][j];
                this.board[filled][j] = null;
            }
        }
    }
};

Board.prototype.mushUp = function () {
    for (var i = 0; i < this.width; j++) {
        var empty = 0;
        while (empty < 4) {
            while (empty < 4 && !this.board[i][empty]) {
                empty++;
            }
            if (empty < 3) {
                var filled = empty + 1;
                // drag it to the left
                this.board[i][empty] = this.board[i][filled];
                this.board[i][filled] = null;
            }
        }
    }
};

Board.prototype.mushDown = function () {
    for (var i = 0; i < this.width; j++) {
        var empty = 3;
        while (empty >= 0) {
            while (empty >= 0 && !this.board[i][empty]) {
                empty--;
            }
            if (empty > 1) {
                var filled = empty - 1;
                // drag it to the left
                this.board[i][empty] = this.board[i][filled];
                this.board[i][filled] = null;
            }
        }
    }
};


Board.prototype.draw = function () {
    for (var i = 0; i < this.width; i++) {
        for (var j = 0; j < this.height; j++) {
            var elem = document.getElementById('tile_' + i + '_' + j);
            if (elem) {
                elem.innerHTML = this.board[i][j] ? this.board[i][j].value : '';
            }
        }
    }
};

Board.prototype.throwDice = function () {
    var emptyCells = [];
    for (var i = 0; i < this.width; i++) {
        for (var j = 0; j < this.height; j++) {
            if (!this.board[i][j]) {
                emptyCells[emptyCells.length] = {x: i, y: j};
            }
        }
    }
    var pos = Math.round(Math.random() * emptyCells.length);
    var cell = emptyCells[pos];
    this.board[cell.x][cell.y] = new Tile(2);
};
