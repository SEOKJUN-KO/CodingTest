class MinHeap {
    constructor() {
        this.h = ['root']
    }

    append(val) {
        this.h.push(val)
        let idx = this.h.length - 1
        while(idx > 1) {
            let p_id = Math.floor(idx/2)
            for ( let i = 0; i < this.h[idx].length; i++ ) {
                if(this.h[p_id][i] < this.h[idx][i]) break
                if(this.h[p_id][i] > this.h[idx][i]) {
                    [ this.h[p_id], this.h[idx] ] = [ this.h[idx], this.h[p_id] ]
                    idx = p_id
                    break
                }
            }
            if (idx !== p_id) break 
        }
    }

    pop() {
        if ( this.h.length === 1) { return null }
        if ( this.h.length === 2 ) { return this.h.pop() }
        
        const ret = this.h[1]
        this.h[1] = this.h.pop()
        let idx = 1
        while( idx < this.h.length ) {
            let tmp = idx
            let [left, right] = [2*idx, 2*idx+1]
            if (left < this.h.length){
                for ( let i = 0; i < this.h[left].length; i++ ) {
                    if ( this.h[tmp][i] < this.h[left][i] ) break
                    if ( this.h[tmp][i] > this.h[left][i] ) {
                        tmp = left
                        break
                    }
                }
            }
            if (right < this.h.length){
                for ( let i = 0; i < this.h[right].length; i++ ) {
                    if ( this.h[tmp][i] < this.h[right][i] ) break
                    if ( this.h[tmp][i] > this.h[right][i] ) {
                        tmp = right
                        break
                    }
                }
            }
            if (idx === tmp) break
            [ this.h[tmp], this.h[idx] ] = [ this.h[idx], this.h[tmp] ]
            idx = tmp
        }

        return ret
    }

    getSize() {
        return this.h.length-1
    }
}

function setHeap(input, K) {
    const heap = new MinHeap()
    for ( let i = 1; i <= K; i++ ) {
        let [priority, alchol] = input[i].split(" ").map(Number)
        heap.append([alchol, priority])
    }
    return heap
}

function calculate(heap, N, M) {
    const minH = new MinHeap()
    let maxA = 0
    let cnt = 0
    while(heap.getSize() >= 1) {
        let [a, p] = heap.pop()
        if (maxA < a) maxA = a
        minH.append([p])
        cnt += p
        if ( minH.getSize() > N ) {
            pop_p = minH.pop()
            cnt -= pop_p
        }
        if ( minH.getSize() === N && cnt >= M ) {
            return maxA
        }
    }
    
    return -1
}

function solution() {
    const fs = require('fs')
    input = fs.readFileSync('input.txt', 'utf-8').trim().split("\n")
    const [N, M, K] = input[0].split(" ").map(Number)
    const heap = setHeap(input, K)
    console.log(calculate(heap, N, M))
}

solution()