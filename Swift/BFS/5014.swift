struct Queue {
    var In = [[Int]]()
    var Out = [[Int]]()
    
    func isEmpty()->Bool{
        if In.count == 0 && Out.count == 0 {
            return true
        }
        return false
    }
    
    mutating func append(_ val: [Int]){
        In.append(val)
    }
    
    mutating func popleft() -> [Int]{
        var out = [-1, -1]
        if(isEmpty()){ return out }
        if(Out.isEmpty){
            Out = In.reversed()
            In = []
        }
        return Out.popLast()!
    }
}

let inputs = readLine()!.split(separator: " ").map{ Int($0)! }
let F = inputs[0]
let S = inputs[1]
let G = inputs[2]
let U = inputs[3]
let D = inputs[4]

var isVisited = Array(repeating: false, count: F+1)
var que = Queue()
que.append([S, 0])
isVisited[S] = true

var now = -1
while( !(que.isEmpty()) ){
    let o = que.popleft()
    now = o[0]
    let cnt = o[1]
    if(now == G){
        print(cnt)
        break
    }
    if(now + U <= F && isVisited[now+U] == false){
        que.append([now+U, cnt+1])
        isVisited[now+U] = true
    }
    if(now - D >= 1 && isVisited[now-D] == false){
        que.append([now-D, cnt+1])
        isVisited[now-D] = true
    }
}
if(now != G){
    print("use the stairs")
}
