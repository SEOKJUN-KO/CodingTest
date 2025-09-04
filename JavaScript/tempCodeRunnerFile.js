function DP(arr) {
    const dp = [0]
    arr.forEach(n => {
        dp.push(dp[dp.length-1] + n)
    })
    return dp
}

function doWork(dp, arr, orders) {
    const M = new Map()
    orders.forEach(order => {
        const [mode, A, B] = order
        if (mode === 1) {
            M.set( A, B - arr[A-1] )
        }
        else {
            let cnt = dp[B] - dp[A-1]
            for( let [k, v] of M.entries() ) {
                if (A <= k && k <= B) {
                    cnt += v
                }
            }
            console.log(cnt)
        }
    })
}

function main() {
    const fs = require("fs");
    const input = fs.readFileSync('input.txt', "utf-8").trim().split("\n");
    const [N, M, K] = input[0].split(" ").map(d => Number(d))
    const arr = input.slice(1, 1+N).map(d => Number(d))
    const orders = input.slice(1+N).map(A => A.split(" ").map(d => Number(d)))
    const dp = DP(arr)
    doWork(dp, arr, orders)
}
main()