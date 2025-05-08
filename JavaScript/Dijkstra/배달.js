class MinHeap {
    constructor() {
       this.heap = [null]
    }
    
    peek() {
        if (this.heap.length >= 1) return this.heap[1]
        return null
    }
    
    isEmpty() {
      return this.heap.length === 1;
    }
    
    append(value) {
        this.heap.push(value)
        let idx = this.heap.length - 1
        while(Math.floor(idx/2) >= 1) {
            const parent = Math.floor(idx/2)
            if(this.heap[parent][0] > this.heap[idx][0]) {
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]]
                idx = parent
                continue
            }
            break
        }
    }
    
    pop() {
        if(this.heap.length === 1) return null
        if(this.heap.length === 2) return this.heap.pop()
        const out = this.heap[1]        
        this.heap[1] = this.heap.pop()
        let idx = 1
        while( 2*idx < this.heap.length ) {
            let tmp = idx
            const [left, right] = [2*idx, 2*idx+1]
            if (this.heap[tmp][0] > this.heap[left][0]) tmp = left
            if (this.heap.length > right && this.heap[tmp][0] > this.heap[right][0]) tmp = right
            if (idx === tmp) break
            [this.heap[idx], this.heap[tmp]] = [this.heap[tmp], this.heap[idx]]
            idx = tmp
        }
        return out
    }
}

function solution(N, road, K) {
    let ans = 0;
    const heap = new MinHeap()
    const board = Array.from({length: N+1}, () => new Array(N+1).fill(Infinity))
    for (let [a, b, c] of road) {
        if (board[a][b] > c) {
            board[a][b] = c
            board[b][a] = c
        }
    }
    const visited = new Array(N+1).fill(Infinity)
    visited[1] = 0
    heap.append([0, 1])
    while(!heap.isEmpty()) {
        const [w, now] = heap.pop()
        if (visited[now] != w ) continue
        for (let i = 1; i <= N; i++) {
            if(w+board[now][i] < visited[i]) {
                visited[i] = w+board[now][i]
                heap.append([w+board[now][i], i])
            }
        }
    }
    for (let i = 1; i <= N; i++) {
        if (visited[i] <= K) ans += 1
    }
    return ans;
}