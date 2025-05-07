const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 첫 줄: N(노드 수), M(간선 수)
const [N, M] = input[0].split(" ").map(Number);

// 이후 줄: 간선 정보 [a, b, c]
const arr = input.slice(1).map(line => line.split(" ").map(Number));

// 가중치 기준 오름차순 정렬
const sortArr = arr.sort((a, b) => {
  if (a[2] < b[2]) return -1;
  if (a[2] > b[2]) return 1;
  return 0;
});

const parent = Array(N + 1).fill(0);
for (let i = 1; i <= N; i++) parent[i] = i;

function find(x) {
  if (x === parent[x]) return x;
  return parent[x] = find(parent[x]); // 경로 압축 추가
}

let cnt = 1;

function union(x, y) {
  let X = find(x);
  let Y = find(y);
  if (X === Y) return false;
  cnt += 1
  if (X < Y) parent[Y] = X;
  else parent[X] = Y;
  return true;
}

let w = 0;
let last = 0;


for (const [a, b, c] of sortArr) {
  if (union(a, b)) {
    w += c;
    last = c;
    if (cnt === N) {
        break;
    }
  }
}

console.log(w - last);