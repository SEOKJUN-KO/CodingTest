// 2042 - 구간 합 구하기 (네 로직 유지 + BigInt 적용)

function DP(arr) {
  const dp = [0n];
  arr.forEach(n => {
    dp.push(dp[dp.length - 1] + n);
  });
  return dp;
}

function doWork(dp, arr, orders) {
  const M = new Map();
  orders.forEach(order => {
    const mode = Number(order[0]);
    const A = Number(order[1]);
    const C = order[2];

    if (mode === 1) {
      const newVal = BigInt(C);
      M.set(A, newVal - arr[A - 1]);
    } else {
      const B = Number(C);
      let cnt = dp[B] - dp[A - 1];
      for (const [k, v] of M.entries()) {
        if (A <= k && k <= B) cnt += v;
      }
      console.log(cnt.toString());
    }
  });
}

function main() {
  const fs = require("fs");
  const input = fs.readFileSync('input.txt', "utf-8").trim().split("\n");

  const [N, M, K] = input[0].trim().split(" ").map(Number);
  const arr = input.slice(1, 1 + N).map(s => BigInt(s));
  const orders = input.slice(1 + N).map(line => line.trim().split(" "));

  const dp = DP(arr);
  doWork(dp, arr, orders);
}
main();
