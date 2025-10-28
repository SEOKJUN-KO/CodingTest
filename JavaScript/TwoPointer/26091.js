const fs = require("fs");

function twoPointer(a, M) {
    let ans = 0
    let [l, r] = [0, a.length-1]

    let arr = a.sort((a, b) => a-b )

    while (l < r) {
        if (arr[l]+arr[r] < M) {
            l += 1
        }
        else {
            l += 1
            r -= 1
            ans += 1
        }
    }

    return ans
}

function solution() {
    input = fs.readFileSync('input.txt', 'utf-8').trim().split("\n")
    const [_, M] = input[0].trim().split(" ").map(Number)
    const arr = input[1].trim().split(" ").map(Number)
    console.log(twoPointer(arr, M))
}

solution()