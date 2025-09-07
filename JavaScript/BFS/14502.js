let board = []

function makeBoard(input) {
    board = input.slice(1).map(arr => arr.split(" ").map(n => Number(n)))
}

const positionM = new Map()

function allCase(N, M, level) {
    if (level >= 4) {
        calculate(N, M)
        return
    }

    for (let y = 0; y < N; y++) {
        for (let x = 0; x < M; x++) {
            const key = y + " " + x

            if ( board[y][x] === 0 && positionM.get(key) == undefined ) {
                positionM.set(key, true)
                allCase(N, M, level+1)
                positionM.delete(key)
            }
        }
    }
}


const originVirus = []

function findVirus(que, N, M) {
    if (originVirus.length > 0) {
        originVirus.forEach( data => {
            que.push(data)
        })
        return 
    }
    
    for (let y = 0; y < N; y++) {
        for (let x = 0; x < M; x++) {
            if ( board[y][x] === 2 ) {
                originVirus.push([y, x])
                que.push([y, x])
            }
        }
    }
}

function putWall(tmpB) {
    for( const[k, v] of positionM.entries() ) {
        const [y, x] = k.split(" ").map( n => Number(n) )
        tmpB[y][x] = 1
    }
}

function spreadVirus(tmpB, N, M, que) {
    let idx = 0
    
    while( idx < que.length ) {
        const [y, x] = que[idx]
        for ( let [dy, dx] of [[-1, 0], [1, 0], [0, -1], [0, 1]] ) {
            const [Y, X] = [y+dy, x+dx]
            if ( 0 <= Y && Y < N && 0 <= X && X < M && tmpB[Y][X] === 0) {
                que.push([Y, X])
                tmpB[Y][X] = 2
            }
        }
        idx++
    }
}

let ans = 0
function countSafe(tmpB, N, M) {
    let cnt = 0
    for (let y = 0; y < N; y++) {
        for (let x = 0; x < M; x++) {
            if ( tmpB[y][x] === 0 ) { cnt++ }
        }
    }
    if ( ans < cnt ) { ans = cnt }
}


function calculate(N, M) {
    let que = []
    
    findVirus(que, N, M)
    
    const tmpB = []
    board.forEach(arr => { tmpB.push([...arr]) })
    putWall(tmpB)
    
    spreadVirus(tmpB, N, M, que)
    countSafe(tmpB, N, M)
}

function main() {
    const fs = require('fs');
    const input = fs.readFileSync(0, "utf-8").trim().split("\n");

    const [N, M] = input[0].split(" ").map(n => Number(n))
    makeBoard(input)
    allCase(N, M, 1)
    console.log(ans)
}
main()