function isPrime(n) {
    if ( n === 2) return true
    for (let i = 2; i <= n**(0.5)+1 ; i++) {
        if (n%i === 0) {
            return false
        } 
    } 
    return true
}

function makePrimeArr(N) {
    let arr = []
    for (let i = 2; i <= N; i++) {
        if (isPrime(i)) { arr.push(i) }
    }
    return arr 
}

function twoPointer(arr, N) {
    let ans = 0
    let [s, e] = [0, 0]
    let cnt = 0
    while(s <= e && e < arr.length) {
        while( cnt < N && e < arr.length ) {
            cnt += arr[e]
            e += 1
        }

        while( cnt >= N && s <= e ) {
            if ( cnt === N ) { 
                ans += 1 
            }
            cnt -= arr[s]
            s += 1
        }
    }
    return ans
}

function solution() {
    const fs = require('fs')
    let N = fs.readFileSync('input.txt', 'utf-8').trim()
    N = Number(N)
    arr = makePrimeArr(N)
    console.log(twoPointer(arr, N))
}

solution()