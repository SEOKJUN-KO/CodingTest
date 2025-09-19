
function twoPointer(arr, N, S) {
    let [s, e] = [0, 0]
    let sum = arr[0]
    if ( S <= sum ) { return 1 }
    ans = Number.MAX_VALUE

    while (true) {
        if (sum >= S) {
            ans = Math.min(ans, e - s + 1)
            sum -= arr[s++]
        } else {
            if (e + 1 > N) break
            sum += arr[++e]
        }
    }


    return ans
}

function main () {
    const fs = require("fs");
    const input = fs.readFileSync('input.txt', "utf-8").trim().split("\n")
    const [N, S] = input[0].trim().split(" ").map(Number)
    const arr = input[1].trim().split(" ").map(Number)
    let ans = twoPointer(arr, N, S)
    
    if ( ans === Number.MAX_VALUE ) {
        console.log(0)
    }
    else {
        console.log(ans)
    }
}

main()