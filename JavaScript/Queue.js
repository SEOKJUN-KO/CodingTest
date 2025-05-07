class Queue {
    constructor() {
      this.data = {};
      this.head = 0;
      this.tail = 0;
    }
  
    enqueue(val) {
      this.data[this.tail++] = val;
    }
  
    dequeue() {
      if (this.isEmpty()) return undefined;
      const val = this.data[this.head];
      delete this.data[this.head++];
      return val;
    }
  
    isEmpty() {
      return this.head === this.tail;
    }
  }
  