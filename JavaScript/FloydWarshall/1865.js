// TC = 5
// N (지점), M(도로), W(웜홀) [500, 2500, 200]
// S, E, T  - M개
// S, E, T  - W개

let board = []

function makeBoard(N) {
    board = []
    for(let i=0; i<=N; i++) {
        let tmp = []
        for(let j=0; j<=N; j++) {
            tmp.push(Number.MAX_VALUE)
        }
        board.push(tmp)
    }
}

function setStreetEdge(S, E, T) {
    board[S][E] = Math.min(T, board[S][E])
    board[E][S] = Math.min(T, board[E][S])
}

function setHoleEdge(S, E, T) {
    board[S][E] = Math.min(-T, board[S][E])
}

function floydWarshall(N) {
    for(let k = 1; k <= N; k++) {
        for(let i = 1; i <= N; i++) {
            for(let j = 1; j <= N; j++) {
                if ( board[i][k] !== Number.MAX_VALUE && board[k][j] !== Number.MAX_VALUE && board[i][k]+board[k][j] < board[i][j] ) {
                    board[i][j] = board[i][k]+board[k][j]
                }
            }
        }
    }

    for(let n = 1; n <= N; n++) {
        if ( board[n][n] < 0 ) { return true; }
    }
    return false
}

function main() {
    const fs = require("fs");
    const input = fs.readFileSync("input.txt", "utf8").trim().split("\n");

    const TC = Number(input[0])
    let lineC = 0
    for( let i = 1; i <= TC; i++ ) {
        lineC += 1
        const [N, M, W] = input[lineC].split(" ").map(d => Number(d))
        makeBoard(N)

        for( let m = 1; m <= M; m++) {
            lineC += 1
            const [S, E, T] = input[lineC].split(" ").map(d => Number(d))
            setStreetEdge(S, E, T)
        }
        for( let w = 1; w <= W; w++) {
            lineC += 1
            const [S, E, T] = input[lineC].split(" ").map(d => Number(d))
            setHoleEdge(S, E, T)
        }

        if (floydWarshall(N)) {console.log("YES")}
        else {console.log("NO")}
    }
}
main()