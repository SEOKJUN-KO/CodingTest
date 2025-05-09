class Queue {
    constructor() {
      this.s = {};
      this.head = 0;
      this.tail = 0;
    }
    add(val) {
      this.s[this.tail++] = val;
    }
    popfront() {
      const out = this.s[this.head];
      delete this.s[this.head++];
      return out;
    }
    isEmpty() {
      return this.head === this.tail;
    }
}
  
const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
  
let idx = 0;
const T = Number(input[idx++]);
  
for (let t = 0; t < T; t++) {
    const [N, K] = input[idx++].split(" ").map(Number);
    const buildTime = input[idx++].split(" ").map(Number);
  
    const outE = Array.from({ length: N }, () => new Set());
    const inE = Array.from({ length: N }, () => new Set());
  
    for (let i = 0; i < K; i++) {
      const [start, end] = input[idx++].split(" ").map(Number);
      outE[start - 1].add(end - 1);
      inE[end - 1].add(start - 1);
    }
  
    const W = Number(input[idx++]) - 1;
  
    const que = new Queue();
    const times = Array(N).fill(0);
  
    for (let i = 0; i < N; i++) {
      if (inE[i].size === 0) {
        que.add(i);
        times[i] = buildTime[i];
      }
    }
  
    while (!que.isEmpty()) {
      const now = que.popfront();
      for (let out of outE[now]) {
        inE[out].delete(now);
        times[out] = Math.max(times[out], times[now] + buildTime[out]);
        if (inE[out].size === 0) {
          que.add(out);
        }
      }
    }
  
    console.log(times[W]);
}