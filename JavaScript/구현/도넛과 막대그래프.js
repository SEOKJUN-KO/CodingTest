// 나가는 간선 있고 들어오는 간선이 없으면서 나가는게 2개 이상 있는 경우 => 추가 정점
// 도넛
// node = n, edge = n
// 막대
// node = n, edge = n-1
// 8자 그래프
// 그 외

class Queue {
    constructor() {
        this.q = {}
        this.head = 0
        this.tail = 0
    }
    add(val) {
        this.q[this.tail++] = val
    }
    popfront() {
        const out = this.q[this.head]
        delete(this.q[this.head++])
        return out
    }
    isEmpty() {
        return this.head === this.tail
    }
}

function doEdge(inE, outE, now, ns, es, que, n) {
    if (inE[now] !== undefined) {
        for (let shooter of inE[now]) {
            if (n.has(shooter)) {
                que.add(shooter)
                ns.add(shooter)
                n.delete(shooter)
            }
            es.add(""+shooter+" "+now)
        }
    }
    
    if (outE[now] !== undefined) {
        for (let receiver of outE[now]) {
            if (n.has(receiver)) {
                que.add(receiver)
                ns.add(receiver)
                n.delete(receiver)
            }
            es.add(""+now+" "+receiver)
        }   
    }
}

function calculate(inE, outE, n) {
    const ans = [0, 0, 0]
    while(n.size > 0) {
        const i = n.values().next().value
        n.delete(i)
        const que = new Queue()
        que.add(i)
        const nodeS = new Set()
        const edgeS = new Set()
        nodeS.add(i);
        while(!que.isEmpty()) {
            let now = que.popfront()
            doEdge(inE, outE, now, nodeS, edgeS, que, n)
        }
        if(nodeS.size === edgeS.size) {
            ans[0] += 1
        }
        else if(nodeS.size-1 === edgeS.size) {
            ans[1] += 1
        }
        else {
            ans[2] += 1
        }
    }
    return ans
}

function solution(edges) {
    const inE = {}
    const outE = {}
    const n = new Set()
    for (let [a, b] of edges) {
        if(! (a in outE)) outE[a] = new Set()
        outE[a].add(b)
        if(! (b in inE)) inE[b] = new Set()
        inE[b].add(a)
        n.add(a); n.add(b)
    }
    
    let out = 0
    for(let key in outE ) {
        if(inE[key] === undefined && outE[key].size >= 2) {
            out = Number(key)
            for (let o of outE[key]){
                inE[o].delete(Number(key))
            }
            delete(outE[key])
            n.delete(Number(key))
            break
        }
    }
    return [out, ...calculate(inE, outE, n)]
}