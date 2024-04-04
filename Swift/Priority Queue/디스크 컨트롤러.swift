struct MinHeap {
    var nodes = [[-1]]
    mutating func append(_ val: [Int]) {
        nodes.append(val)
        var idx = nodes.count-1
        while( idx/2 >= 1 && nodes[idx][1] < nodes[idx/2][1] ) {
            (nodes[idx], nodes[idx/2]) = (nodes[idx/2], nodes[idx])
            idx = idx/2
        }
    }
    mutating func pop() -> [Int] {
        if nodes.count == 1 { return [-1] }
        if nodes.count == 2 { return nodes.popLast()! }
        let out = nodes[1]
        nodes[1] = nodes.popLast()!
        var idx = 1
        while(idx*2 < nodes.count) {
            let (leftI, rightI) = (2*idx, 2*idx+1)
            var tmp = idx
            if nodes[tmp][1] > nodes[leftI][1] {
                tmp = leftI
            }
            if rightI < nodes.count && nodes[tmp][1] > nodes[rightI][1] {
                tmp = rightI
            }
            if tmp == idx { break }
            (nodes[idx], nodes[tmp]) = (nodes[tmp], nodes[idx])
            idx = tmp
        }
        return out
    }
}

func solution(_ jobs:[[Int]]) -> Int {
    var jobs = jobs
    jobs = jobs.sorted(by: { ($0[0], $0[1]) < ($1[0], $1[1]) })
    var (time, idx) = (0, 0)
    var heap = MinHeap()
    var s = 0
    while( idx < jobs.count || heap.nodes.count > 1 ) {
        if idx < jobs.count && time >= jobs[idx][0] {
            while(idx < jobs.count && time >= jobs[idx][0]) {
                heap.append(jobs[idx])
                idx += 1
            }
        }
        if heap.nodes.count > 1 {
            let out = heap.pop()
            let (inTime, workTime) = (out[0], out[1])
            s += workTime + (time-inTime)
            time += workTime
        }
        else {
            if idx < jobs.count {
                time = jobs[idx][0]
            }
        }
    }
    return s/jobs.count
}
