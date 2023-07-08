let inputs = readLine()!.split(separator: " ").map{ Int($0)! }
let N = inputs[0]
let M = inputs[1]
var graph = Array(repeating: [[Int]](), count: N+1)
for _ in 1..<N{
    let inputs = readLine()!.split(separator: " ").map{ Int($0)! }
    let a = inputs[0]
    let b = inputs[1]
    let w = inputs[2]
    graph[a].append([b, w])
    graph[b].append([a, w])
}

private func getDistance(_ pre: Int, _ now: Int, _ weight: Int, _ target: Int) -> Int{
    if(target == now){
        return weight
    }
    var ans = -1000
    for info in graph[now]{
        let node = info[0]
        let w = info[1]
        if(node != pre){
            ans = max(ans, getDistance(now, node, weight+w, target))
        }
    }
    return ans
}
for _ in 0..<M{
    let inputs = readLine()!.split(separator: " ").map{ Int($0)! }
    var ans = -1000
    let now = inputs[0]
    let target = inputs[1]
    for info in graph[now]{
        let node = info[0]
        let weight = info[1]
        ans = max(getDistance(now, node, weight, target), ans)
    }
    print(ans)
}
