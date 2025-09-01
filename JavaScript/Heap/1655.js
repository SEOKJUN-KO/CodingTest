class MinHeap {
    constructor() {
        this.store = [null];
    }

    size() {
        return this.store.length-1
    }

    push(val) {
        this.store.push(val);
        let idx = this.store.length - 1;

        while (idx > 1) {
            const pidx = Math.floor(idx / 2);
            if (this.store[pidx] > this.store[idx]) {
                [this.store[pidx], this.store[idx]] = [this.store[idx], this.store[pidx]];
                idx = pidx;
            } else {
                break;
            }
        }
    }

    pop() {
        if (this.store.length === 1) return undefined;
        if (this.store.length === 2) return this.store.pop();

        const out = this.store[1];
        this.store[1] = this.store.pop();

        let idx = 1;
        while (true) {
            let tmp = idx;
            const left = idx * 2;
            const right = idx * 2 + 1;

            if (left < this.store.length && this.store[left] < this.store[tmp]) {
                tmp = left;
            }
            if (right < this.store.length && this.store[right] < this.store[tmp]) {
                tmp = right;
            }

            if (tmp === idx) break;
            [this.store[idx], this.store[tmp]] = [this.store[tmp], this.store[idx]];
            idx = tmp;
        }

        return out;
    }
}

class MaxHeap {
    constructor() {
        this.store = [null]; 
    }

    size() {
        return this.store.length-1
    }

    push(val) {
        this.store.push(val);
        let idx = this.store.length - 1;

        while (idx > 1) {
            const pidx = Math.floor(idx / 2);
            if (this.store[pidx] < this.store[idx]) {
                [this.store[pidx], this.store[idx]] = [this.store[idx], this.store[pidx]];
                idx = pidx;
            } else {
                break;
            }
        }
    }

    pop() {
        if (this.store.length === 1) return undefined;
        if (this.store.length === 2) return this.store.pop();

        const out = this.store[1];
        this.store[1] = this.store.pop();

        let idx = 1;
        while (true) {
            let tmp = idx;
            const left = idx * 2;
            const right = idx * 2 + 1;

            if (left < this.store.length && this.store[left] > this.store[tmp]) {
                tmp = left;
            }
            if (right < this.store.length && this.store[right] > this.store[tmp]) {
                tmp = right;
            }

            if (tmp === idx) break;
            [this.store[idx], this.store[tmp]] = [this.store[tmp], this.store[idx]];
            idx = tmp;
        }

        return out;
    }
}

function calculate(infos) {
    const minH = new MinHeap()
    const maxH = new MaxHeap()
    
    let mid = infos[0]
    console.log(mid)
    for(let i = 1; i < infos.length; i++) {
        const n = infos[i]
        if ( mid < n ) { minH.push(n) }
        else { maxH.push(n) }
        
        if ( minH.size() === maxH.size() || minH.size()-1 === maxH.size() ) {
            
        }
        else {
            if ( minH.size() > maxH.size() ) {
                maxH.push(mid)
                mid = minH.pop()
            }
            else {
                minH.push(mid)
                mid = maxH.pop()
            }
        }
        console.log(mid)
    }
}

function main() {
    const fs = require("fs");
    const input = fs.readFileSync("input.txt", "utf8").trim().split("\n");

    const N = Number(input[0]);
    const infos = input.slice(1).map(Number);
    calculate(infos)
}

main();
