const inD = new Map()
const outD = new Map()

function getInfo(input, M) {
    for(let i = 1; i < 1+M; i++) {
        const [A, B] = input[i].split(" ").map(n => Number(n))
        if ( outD.get(A) == undefined ) {
            outD.set(A, new Map())
        }
        outD.set(A, outD.get(A).set(B, true) )
        if ( inD.get(B) == undefined ) {
            inD.set(B, new Map())
        }
        inD.set(B, inD.get(B).set(A, true))
    }
    // console.log(inD)
    // console.log(outD)
}

class MinHeap {
    constructor() {
        this.store = [null]
    }
    isEmpty() {
        return this.store.length === 1
    }

    push(v) {
        this.store.push(v)
        let idx = this.store.length-1
        let pidx = Math.floor(idx/2)
        while( this.store[pidx] !== null ) {
            if ( this.store[idx] < this.store[pidx] ) {
                [this.store[pidx], this.store[idx]] = [this.store[idx], this.store[pidx]]
                idx = pidx
                pidx = Math.floor(idx/2)
                continue
            }
            break
        }
    }

    pop() {
        if (this.isEmpty()) { return null }
        if (this.store.length === 2) { return this.store.pop() }
        const out = this.store[1]
        this.store[1] = this.store.pop()

        let idx = 1
        while(2*idx < this.store.length) {
            let tmp = idx
            let [left, right] = [idx*2, idx*2 + 1]
            if ( this.store[tmp] > this.store[left] ) { tmp = left }
            if ( this.store[tmp] > this.store[right] ) { tmp = right }
            if ( tmp === idx ) { break }
            [ this.store[tmp], this.store[idx] ] = [ this.store[idx], this.store[tmp] ]
            idx = tmp
        }
        return out
    }
}

const ans = []
function findFirstNode(heap, N) {
    for(let i = 1; i <= N; i++) {
        if ( inD.get(i) == undefined ) {
            heap.push(i)
        }
    }
}

function calculate(N) {
    const heap = new MinHeap()
    findFirstNode(heap, N)
    while( !heap.isEmpty() ) {
        const key = heap.pop()
        ans.push(""+key)
        if (outD.get(key) != undefined ) {
            for ( const [k, v] of outD.get(key).entries() ) {
                inD.get(k).delete(key)
                if( inD.get(k).size === 0 ) { 
                    inD.delete(k)
                    heap.push(k)
                }
                outD.delete(key)
            }
        }
    }
}

function main() {
    const fs = require('fs')
    const input = fs.readFileSync('input.txt', 'utf-8').split("\n")
    const [N, M] = input[0].split(" ").map(n => Number(n))
    getInfo(input, M)
    calculate(N)
    console.log(ans.join(" "))
}

main()