let N = Int(readLine()!)!

var graph = Array(repeating: [Int](), count: N+1)
for _ in 0..<N-1{
    let inputs = readLine()!.split(separator: " ").map{ Int($0)! }
    let a = inputs[0]
    let b = inputs[1]
    graph[a].append(b)
    graph[b].append(a)
}

var leaves = Array(repeating: false, count: N+1)
for i in 1...N{
    if(graph[i].count == 1){
        leaves[i] = true
    }
}
let q = Int(readLine()!)!
for _ in 0..<q{
    let inputs = readLine()!.split(separator:" ").map{ Int($0)! }
    if(inputs[0] == 1){
        if(leaves[inputs[1]]){
            print("no")
        }
        else{
            print("yes")
        }
    }
    else{
        print("yes")
    }
}
