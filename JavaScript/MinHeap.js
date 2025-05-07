class MinHeap {
    constructor() {
      this.heap = [];
    }
  
    push(val) {
      this.heap.push(val);
      this._bubbleUp();
    }
  
    pop() {
      if (this.heap.length === 0) return undefined;
      if (this.heap.length === 1) return this.heap.pop();
  
      const min = this.heap[0];
      this.heap[0] = this.heap.pop();
      this._bubbleDown();
      return min;
    }
  
    peek() {
      return this.heap[0];
    }
  
    isEmpty() {
      return this.heap.length === 0;
    }
  
    _bubbleUp() {
      let index = this.heap.length - 1;
      const current = this.heap[index];
  
      while (index > 0) {
        const parentIdx = Math.floor((index - 1) / 2);
        const parent = this.heap[parentIdx];
  
        if (current >= parent) break;
  
        this.heap[index] = parent;
        this.heap[parentIdx] = current;
        index = parentIdx;
      }
    }
  
    _bubbleDown() {
      let index = 0;
      const length = this.heap.length;
      const current = this.heap[0];
  
      while (true) {
        const leftIdx = index * 2 + 1;
        const rightIdx = index * 2 + 2;
        let swapIdx = null;
  
        if (leftIdx < length && this.heap[leftIdx] < current) {
          swapIdx = leftIdx;
        }
  
        if (
          rightIdx < length &&
          this.heap[rightIdx] < (swapIdx === null ? current : this.heap[leftIdx])
        ) {
          swapIdx = rightIdx;
        }
  
        if (swapIdx === null) break;
  
        this.heap[index] = this.heap[swapIdx];
        this.heap[swapIdx] = current;
        index = swapIdx;
      }
    }
  }
  