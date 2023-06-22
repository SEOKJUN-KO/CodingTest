let inputs = readLine()!.split(separator: " ").map{ Int($0)! }
let N = inputs[0]
let M = inputs[1]

var inDegrees = Array(repeating: 0, count: N+1)
var outDegrees = Array(repeating: [Int](), count: N+1)
for _ in 1...M {
    let inputR = readLine()!.split(separator: " ").map{ Int($0)! }
    let short = inputR[0]
    let tall = inputR[1]
    outDegrees[short].append(tall)
    inDegrees[tall] += 1
}

struct Queue<Int> {
    var inputStack = [Int]()
    var outputStack = [Int]()
    
    mutating func append(_ x: Int) {
        inputStack.append(x)
    }
    
    mutating func pop() -> Int? {
        var top: Int?
        if outputStack.isEmpty {
            outputStack = inputStack.reversed()
            inputStack = []
            top = outputStack.popLast()
        }
        else {
            top = outputStack.popLast()
        }
        return top
    }
    
    mutating func head() -> Int? {
        if outputStack.isEmpty {
            outputStack = inputStack.reversed()
            inputStack = []
        }
        return outputStack.isEmpty ? nil : outputStack[outputStack.endIndex-1]
    }
    
    func isEmpty() -> Bool {
        return inputStack.isEmpty && outputStack.isEmpty ? true : false
    }
}


var q = Queue<Int>()

for i in 1...N {
    if(inDegrees[i] == 0){
        q.append(i)
    }
}

while(!(q.isEmpty())){
    let node = q.pop()!
    print(node, terminator: " ")
    for n in outDegrees[node] {
        inDegrees[n] -= 1
        if(inDegrees[n] == 0){
            q.append(n)
        }
    }
}
