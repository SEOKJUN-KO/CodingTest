const inEdge = []
const outEdge = []

class Node {
    constructor(value) {
        this.pre = null
        this.next = null
        this.value = value
    }
}

class Deque {
    constructor() {
        this.head = new Node("head")
        this.tail = new Node("tail")
        this.head.next = this.tail
        this.tail.pre = this.head
        this.size = 0
    }

    append(value) {
        const node = new Node(value)
        node.pre = this.tail.pre
        node.next = this.tail

        this.tail.pre.next = node
        this.tail.pre = node
        this.size++
    }

    getSize() { return this.size }

    popleft() {
        const node = this.head.next
        
        this.head.next = node.next
        node.next.pre = this.head

        node.pre = null
        node.next = null

        for( let [k, _] of outEdge[node.value].entries() ) {
            inEdge[k].delete(node.value)
            if ( inEdge[k].size === 0) {
                this.append(k)
            }
        }
        this.size--

        return node.value
    }

    printAll() {
        let p = this.head.next
        while (p.value !== this.tail.value) {
            console.log(p.value)
            p = p.next            
        }
    }
}

const deque = new Deque()
function setInfo(N, M, input) {
    
    for ( let i = 0; i <= N; i++ ) {
        inEdge.push(new Map())
        outEdge.push(new Map())
    }

    for ( let i = 0; i < M; i++ ) {
        const [A, B] = input[i].trim().split(" ").map(Number)
        inEdge[B].set(A, true)
        outEdge[A].set(B, true)
    }

}

function findStart(N) {
    for ( let i = 1; i <= N; i++ ) {
        if ( inEdge[i].size === 0 ) {
            deque.append(i)
        }
    }
}

const answer = []
function calculate() {
    while( deque.getSize() > 0 ) {
        const now = deque.popleft()
        answer.push(String(now))
    }
}

function main () {
    const fs = require("fs");
    const input = fs.readFileSync('input.txt', "utf-8").trim().split("\n")
    
    const [N, M] = input[0].trim().split(" ").map(n => Number(n))
    setInfo(N, M, input.slice(1))
    findStart(N)
    calculate()
    console.log(answer.join(" "))
}

main()