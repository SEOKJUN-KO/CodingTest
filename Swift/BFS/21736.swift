struct Queue{
    var In = [[Int]]()
    var Out = [[Int]]()
    
    func isEmpty()->Bool{
        if(In.count == 0 && Out.count == 0){ return true }
        return false
    }
    
    mutating func append(_ val: [Int]){
        In.append(val)
    }
    
    mutating func popleft()-> [Int]?{
        if(isEmpty()){ return nil }
        if(Out.count == 0){
            Out = In.reversed()
            In = []
        }
        return Out.popLast()
    }
    
}

let inputs = readLine()!.split(separator: " ").map{ Int($0)! }
let N = inputs[0]
let M = inputs[1]

var maps = [[String]]()
for _ in 0..<N{
    maps.append(readLine()!.map{String($0)})
}

func BFS() -> Int {
    var queue = Queue()
    var ans = 0
    for i in 0..<N{
        for j in 0..<M{
            if(maps[i][j] == "I"){
                queue.append([j,i])
                maps[i][j] = "X"
                break
            }
        }
        if( !(queue.isEmpty()) ){ break }
    }
    let dx = [-1, +1, +0, +0]
    let dy = [+0, +0, -1, +1]
    while( !(queue.isEmpty()) ){
        let now = queue.popleft()!
        for i in 0..<4 {
            let X = now[0]+dx[i]
            let Y = now[1]+dy[i]
            if( 0 <= X && X < M && 0 <= Y && Y < N && ( maps[Y][X] == "O" || maps[Y][X] == "P" )){
                if(maps[Y][X] == "P"){
                    ans += 1
                }
                queue.append([X, Y])
                maps[Y][X] = "X"
            }
        }
    }
    return ans
}
let r = BFS()
print( r == 0 ? "TT" : r )
