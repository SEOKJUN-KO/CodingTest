class MinHeap {
    constructor() {
        this.h = ["root"]
    }

    getSize() {
        return this.h.length - 1
    }

    append(value) {
        this.h.push(value)
        let idx = this.h.length - 1

        while( idx > 1 ) {
            let pidx = Math.floor(idx/2)
            if (this.h[pidx][0] > this.h[idx][0]) {
                [this.h[pidx], this.h[idx]] = [this.h[idx], this.h[pidx]]
            }
            else {
                break
            }
            idx = pidx
        }
    }

    // 사용 시, getSize와 연동 필요
    pop() {
        if ( this.h.length === 2 ) { return this.h.pop() }
        const out = this.h[1]

        this.h[1] = this.h.pop()
        let idx = 1
        while(idx < this.h.length) {
            let tmp = idx
            const [left, right] = [2*idx, 2*idx+1]
            if ( left < this.h.length && this.h[left][0] < this.h[tmp][0] ) {
                tmp = left
            }
            if ( right < this.h.length && this.h[right][0] < this.h[tmp][0] ) {
                tmp = right
            }
            if (tmp === idx) { break }
            [this.h[tmp], this.h[idx]] = [this.h[idx], this.h[tmp]]
            idx = tmp
        }
        return out
    }
}

const heap = new MinHeap()

function addEdges(input, E) {
    for( let i = 0; i < E; i++ ) {
        const [A, B, C] = input[i].trim().split(" ").map(Number)
        heap.append([C, A, B])
    }
}

const P = []
function getParent(x) {
    if (P[x] === x) return x;
    P[x] = getParent(P[x]); // 경로 압축
    return P[x];
}


function connect(x, y) {
    const X = getParent(x)
    const Y = getParent(y)

    if (X === Y) { return false }
    if ( X < Y ) {
        P[Y] = X
        P[y] = X
    }
    else {
        P[X] = Y
        P[x] = Y
    }

    return true
}

function calculate(N) {
    let ans = 0
    for( let i = 0; i <= N; i++) {
        P.push(i)
    }

    while(heap.getSize() > 0) { // 10^5
        const [C, A, B] = heap.pop()

        if ( connect(A, B) ) { 
            ans += C
        }
    }
    console.log(ans)
}

function solution() {
    const fs = require('fs')
    const input = fs.readFileSync('input.txt', 'utf-8').trim().split("\n");
    const [V, E] = input[0].trim().split(" ").map(Number)
    addEdges(input.slice(1), E)
    calculate(V)
}
solution()