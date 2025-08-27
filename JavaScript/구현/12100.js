let board = []
let ans = 0

function doUp() {
    for ( let x = 0; x < board.length; x++ ) {
        let y = 0
        let store = []
        while(y < board.length) {
            if(board[y][x] !== 0) {
                store.push(board[y][x])
            }
            y++
        }
        for(let y = 0; y < board.length; y++) {
            if( y < store.length ) { board[y][x] = store[y] }
            else { board[y][x] = 0 }
        }
        
        
        store = []
        y = 0
        while(y+1 < board.length) {
            if( board[y][x] === board[y+1][x] ) {
                store.push(board[y][x]*2)
                y += 2
            }
            else {
                if (board[y][x] !== 0) { store.push(board[y][x]) }
                y += 1
            }
        }

        if( y === board.length - 1 && board[y][x] !== 0) {
            store.push(board[y][x])
        }
        
        for(let y = 0; y < board.length; y++) {
            if( y < store.length ) { board[y][x] = store[y] }
            else { board[y][x] = 0 }
        }

    }
}

function doDown() {
    for ( let x = 0; x < board[0].length; x++ ) {
        let y = board.length-1
        let store = []
        while(y >= 0) {
            if(board[y][x] !== 0) {
                store.push(board[y][x])
            }
            y--
        }
        for(let y = board.length-1; y >= 0; y--) {
            const sI = board.length -1 -y;
            if( sI < store.length  ) { board[y][x] = store[sI] }
            else { board[y][x] = 0 }
        }
        
        
        store = []
        y = board.length-1
        while(y-1 >= 0) {
            if( board[y][x] === board[y-1][x] ) {
                store.push(board[y][x]*2)
                y -= 2
            }
            else {
                if (board[y][x] !== 0) { store.push(board[y][x]) }
                y--
            }
        }

        if( y === 0 && board[y][x] !== 0) {
            store.push(board[y][x])
        }
        
        for(let y = board.length-1; y >= 0; y--) {
            const sI = board.length -1 -y;
            if( sI < store.length  ) { board[y][x] = store[sI] }
            else { board[y][x] = 0 }
        }
    }
}

function doLeft() {
   for ( let y = 0; y < board.length; y++ ) {
        let x = 0
        let store = []
        while(x < board.length) {
            if(board[y][x] !== 0) {
                store.push(board[y][x])
            }
            x++
        }
        for(let x = 0; x < board[0].length; x++) {
            if( x < store.length ) { board[y][x] = store[x] }
            else { board[y][x] = 0 }
        }
        x = 0
        store = []
        while(x+1 < board[0].length) {
            if( board[y][x] === board[y][x+1] ) {
                store.push(board[y][x]*2)
                x += 2
            }
            else {
                if (board[y][x] !== 0) { store.push(board[y][x]) }
                x += 1
            }
        }

        if( x === board.length - 1 && board[y][x] !== 0) {
            store.push(board[y][x])
        }
        
        for(let x = 0; x < board[0].length; x++) {
            if( x < store.length ) { board[y][x] = store[x] }
            else { board[y][x] = 0 }
        }
    }
}

function doRight() {
   for ( let y = 0; y < board.length; y++ ) {
        
        let x = board.length-1
        let store = []
        while(x >= 0) {
            if(board[y][x] !== 0) {
                store.push(board[y][x])
            }
            x--
        }
        for(let x = board[0].length-1; x >= 0; x--) {
            const sI = board.length - 1 - x;
            if( sI < store.length ) { board[y][x] = store[sI] }
            else { board[y][x] = 0 }
        }
        x = board.length-1
        store = []

        while(x-1 >= 0) {
            if( board[y][x] === board[y][x-1] ) {
                store.push(board[y][x]*2)
                x -= 2
            }
            else {
                if (board[y][x] !== 0) { store.push(board[y][x]) }
                x -= 1
            }
        }

        if( x === 0 && board[y][x] !== 0) {
            store.push(board[y][x])
        }
        
        for(let x = board[0].length-1; x >= 0; x--) {
            const sI = board.length - 1 - x;
            if( sI < store.length ) { board[y][x] = store[sI] }
            else { board[y][x] = 0 }
        }
    }
}

function doDirection(level) {
    if ( level >= 6 ) {
        board.forEach(y => {
            ans = Math.max(...y, ans)
        })
        return 
    }

    let copy1 = board.map(row => row.slice());
    let copy2 = board.map(row => row.slice());
    let copy3 = board.map(row => row.slice());
    let copy4 = board.map(row => row.slice());
    doUp()
    doDirection(level+1)
    board = copy1
    
    doDown()
    doDirection(level+1)
    board = copy2
    
    doLeft()
    doDirection(level+1)
    board = copy3

    doRight()
    doDirection(level+1)
    board = copy4
}


function main() {
    const fs = require("fs");
    const input = fs.readFileSync("input.txt", "utf-8").trim().split("\n");

    const N = Number(input[0]);

    board = input.slice(1).map(line => line.split(" ").map(Number));
    doDirection(1)
    console.log(ans)
}

main()