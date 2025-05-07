class MinHeap {
    constructor() {
      this.nodes = [null]; // 0번 인덱스는 더미
    }
  
    isNotEmpty() {
      return this.nodes.length > 1;
    }
  
    heappush(val) {
      this.nodes.push(val);
      let index = this.nodes.length - 1;
  
      while (index > 1 && this.nodes[index] < this.nodes[Math.floor(index / 2)]) {
        [this.nodes[index], this.nodes[Math.floor(index / 2)]] =
          [this.nodes[Math.floor(index / 2)], this.nodes[index]];
        index = Math.floor(index / 2);
      }
    }
  
    heappop() {
      if (!this.isNotEmpty()) return undefined;
  
      const out = this.nodes[1];
      this.nodes[1] = this.nodes[this.nodes.length - 1];
      this.nodes.pop();
  
      let index = 1;
      while (this.isNotEmpty()) {
        let left = index * 2;
        let right = index * 2 + 1;
        let smallest = index;
  
        if (left < this.nodes.length && this.nodes[smallest] > this.nodes[left]) {
          smallest = left;
        }
        if (right < this.nodes.length && this.nodes[smallest] > this.nodes[right]) {
          smallest = right;
        }
        if (smallest !== index) {
          [this.nodes[index], this.nodes[smallest]] = [this.nodes[smallest], this.nodes[index]];
          index = smallest;
        } else {
          break;
        }
      }
  
      return out;
    }
  }
  