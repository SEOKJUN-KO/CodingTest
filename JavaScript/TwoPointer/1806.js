const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 첫 줄: N, S
const [N, S] = input[0].split(" ").map(Number);

// 두 번째 줄: 배열
const arr = input[1].split(" ").map(Number);

let [left, right] = [0, 0]
let s = arr[0]
let ans = Infinity

function compare() {
    if (s >= S && ans > right-left+1) {
        ans = right-left+1
    }
}

compare()

while(left <= right && right < N) {
    if (right === N-1) {
        if (s < S) break
        s -= arr[left++]
        compare()
        continue
    }
    if (s < S) s += arr[++right]
    else s -= arr[left++]
    compare()
}
console.log(ans === Infinity ? 0 : ans)