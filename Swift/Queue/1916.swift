struct Queue {
    var inA = [[Int]]()
    var outA = [[Int]]()
    func isEmpty()->Bool{
        if(inA.count == 0 && outA.count == 0){
            return true
        }
        return false
    }
    mutating func append(_ val: [Int]){
        inA.append(val)
    }
    mutating func popleft()->[Int]{
        if isEmpty() { return [-1, -1] }
        if(outA.count == 0){
            outA = inA.reversed()
            inA = []
        }
        return outA.popLast()!
    }
}

let n = Int(readLine()!)!
let m = Int(readLine()!)!
var graph = Array(repeating: [[Int]](), count: n+1)
for _ in 0..<m {
    let inputs = readLine()!.split(separator: " ").map{ Int($0)! }
    let a = inputs[0]
    let b = inputs[1]
    let cost = inputs[2]
    graph[a].append([cost, b])
}
var minL = Array(repeating: Int.max, count: n+1)
let inputs = readLine()!.split(separator: " ").map{ Int($0)! }
let start = inputs[0]
let target = inputs[1]
minL[start] = 0
var queue = Queue()
queue.append([0, start])
while(!(queue.isEmpty())){
    let now = queue.popleft()
    let w = now[0]
    let next = now[1]
    if(minL[next] == w){
        for info in graph[next]{
            let weight = info[0]
            let daum = info[1]
            if(w+weight < minL[daum]){
                minL[daum] = w+weight
                queue.append([w+weight, daum])
            }
        }
    }
}
print(minL[target])
