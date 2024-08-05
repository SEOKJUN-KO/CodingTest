import Foundation

struct Queue {
    var In = [Int]()
    var Out = [Int]()
    
    mutating func append(_ val:Int) {
        In.append(val)
    }
    
    mutating func pop() -> Int {
        if Out == [] {
            Out = In.reversed()
            In = []
        }
        return Out.popLast()!
    }
}

var T = Int(readLine()!)!
for _ in 1...T {
    var input = readLine()!.split(separator: " ").map { Int($0)! }
    let N = input[0], K = input[1]
    let timeArr: [Int] = readLine()!.split(separator: " ").map { Int($0)! }
    var addedTime = Array(repeating: 0, count: N)
    var In = Array(repeating: 0, count: N+1)
    var Out: [[Int]] = Array(repeating: [], count: N+1)
    for _ in 1...K {
        input = readLine()!.split(separator: " ").map { Int($0)! }; let A = input[0]; let B = input[1];
        Out[A].append(B)
        In[B] += 1
    }
    let W = Int(readLine()!)!
    var que = Queue()
    for i in 1...N {
        if In[i] == 0 {
            que.append(i)
            addedTime[i-1] = timeArr[i-1]
        }
    }
    while( que.In != [] || que.Out != [] ) {
        let now = que.pop()
        for out in Out[now] {
            In[out] -= 1
            addedTime[out-1] = max(addedTime[now-1]+timeArr[out-1], addedTime[out-1])
            if In[out] == 0 {
                que.append(out)
            }
        }
    }
    print(addedTime[W-1])
}
