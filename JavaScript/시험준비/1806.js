
function twoPointer(arr, N, S) {
    let [s, e] = [0, 0]
    let sum = arr[0]
    if ( S <= sum ) { return 1 }
    ans = Number.MAX_VALUE

    while ( s <= e && e < N ) {
        while( sum < S && e < N-1) {
            e++
            sum += arr[e]
        }
        if ( e === N-1 && sum < S ) { break } 
        while(s < e && sum >= S) {
            if ( sum >= S && e-s+1 < ans ) {
                ans = e-s+1
            }
            if ( ans === 1 ) { return 1 }
            sum -= arr[s]
            s++
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