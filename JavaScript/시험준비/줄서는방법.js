function getPermutationN(n) {
    let cnt = 1
    for (let i = 1; i <= n; i++) {
        cnt *= i
    }
    return cnt
}

function getNow(n, p) {
    return getPermutationN(n-p)
}

let ans = []
let used = new Map()
function calculate(n, k) {
    let level = 1
    let K = k
    while(level <= n) {
        let N = getNow(n, level)
        for (let i = 1; i <= n; i++) {
            if ( used.get(i) === true ) continue
            if ( 0 <= K && K < N ) {
                used.set(i, true)
                ans.push(i)
                break
            }
            K -= N
        }
        level += 1
    }
    return ans
}

function solution(n, k) {
    return calculate(n, k-1)
}