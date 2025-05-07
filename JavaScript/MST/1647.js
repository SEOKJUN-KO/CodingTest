class Queue {
    constructor() {
        this.dict = {}
        this.front = 0
        this.rear = 0
    }
    
    append(val) {
        this.dict[this.rear] = val
        this.rear += 1
        return 
    }

    popfront() {
        if (this.front === this.rear) {
            return [undefined, undefined]
        }
        const val = this.dict[this.front]
        delete(this.dict[this.front])
        this.front += 1
        return val
    }

    isEmpty() {
        if (this.front === this.rear) {
            return true
        }
        return false
    }
}

let N = 7;
const arr = [
    [1, 2, 3],
    [1, 3, 2],
    [3, 2, 1],
    [2, 5, 2],
    [3, 4, 4],
    [7, 3, 6],
    [5, 1, 5],
    [1, 6, 2],
    [6, 4, 1],
    [6, 5, 3],
    [4, 5, 3],
    [6, 7, 4]
];

const board = Array.from({length: N+1}, () => Array(N+1).fill(Infinity))

for( let [a, b, c] of arr ){
    if (board[a][b] > c) {
        board[a][b] = c
        board[b][a] = c
    }
}
const visited = Array.from( {length: N}, ()=> Infinity )
visited[1] = 0

const que = new Queue()
que.append([1, 0])
console.log(visited)
while(!que.isEmpty()) {
    const [node, weight] = que.popfront()
    if (weight > visited[node]) {
        continue
    }
    for(let i = 1; i < N+1; i++) {
        const w = board[node][i]
        if ( visited[i] >= w+weight ) {
            visited[i] = w+weight
            que.append([i, visited[i]])
        }
    }
}
console.log(visited)
