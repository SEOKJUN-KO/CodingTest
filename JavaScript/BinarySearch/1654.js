const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [K, N] = input[0].split(" ").map(Number);
const lengths = input.slice(1).map(Number);

const arr = lengths.sort((a, b)=> {
    if(a < b) return -1
    else if(a > b) return 1
    return 0
})

function binarySearch() {
    let [left, right] = [0, 2**31-1]
    let mid = 0
    let ans = 0
    while(left <= right) {
        mid = Math.floor((left+right)/2)
        let cnt = 0
        for(const a of arr) {
            cnt += Math.floor(a/mid)
            if (cnt >= N) {
                if (ans < mid) ans = mid
                break
            }
        }
        if (cnt < N) right = mid - 1
        else left = mid + 1
    }
    return ans
}

console.log(binarySearch())