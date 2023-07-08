let n = Int(readLine()!)!
var graph = Array(repeating: Array(repeating: Int.max, count: n+1), count: n+1)

var inputs = readLine()!.split(separator: " ").map{ Int($0)! }
while(inputs != [-1, -1] ){
    let a = inputs[0]
    let b = inputs[1]
    graph[a][b] = 1
    graph[b][a] = 1
    inputs = readLine()!.split(separator: " ").map{ Int($0)! }
}

for k in 1...n{
    for i in 1...n{
        for j in 1...n{
            if( graph[i][k] != Int.max && graph[k][j] != Int.max && i != k && k != j && i != j){
                graph[i][j] = min( graph[i][j], graph[i][k] + graph[k][j] )
                graph[j][i] = graph[j][i]
            }
        }
    }
}

var score = Int.max
var ans = [Int]()
for i in 1...n{
    graph[i][i] = 1
    let m = graph[i][1...].max()!
    if( m < score){
        score = m
        ans = [i]
    }
    else if( m == score){
        ans.append(i)
    }
}
print(score, ans.count)
print( ans.map{ String($0) }.joined(separator: " ") )
