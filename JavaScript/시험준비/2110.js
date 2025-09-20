
const arr = []
function getArray(input, N) {
    for ( let i = 0; i < N; i++ ) {
        arr.push(Number(input[i].trim()))
    }
    arr.sort((a, b) => { return a - b })
}

function calculate(M, C) {
    let ans = 0
    let [s, e] = [0, 9000000000]
    while (s <= e) {
        const mid = Math.floor((s+e)/2)
        let cnt = 0
        let [idx, minP] = [0, 0]
        while(idx < M) {
            if ( minP <= arr[idx] ) {
                minP = arr[idx] + mid
                cnt++
            }
            else {
                idx++
            }
            if (cnt >= C) {
                if ( ans < mid ) { ans = mid }
                break
            }
        }
        if ( cnt >= C ) {
            s = mid + 1
        }
        else {
            e = mid - 1
        }
    }
    console.log(ans)
}

function solution() {
    const fs = require('fs')
    const input = fs.readFileSync('input.txt', 'utf-8').trim().split("\n")

    const [M, C] = input[0].trim().split(" ").map(Number)
    getArray(input.slice(1), M)
    calculate(M, C)
}

solution()