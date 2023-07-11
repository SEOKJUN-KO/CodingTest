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


let N = Int(readLine()!)!
let inputs = readLine()!.split(separator: " ").map{ Int($0)! }
let r1 = inputs[0]
let c1 = inputs[1]
let r2 = inputs[2]
let c2 = inputs[3]

var que = Queue()
que.append([r1, c1, 0])

let dr = [ -2, -2, +0, +0, +2, +2 ]
let dc = [ -1, +1, -2, +2, -1, +1 ]

var board = Array(repeating: Array(repeating: false, count: N), count: N)
var rN = -1
var cN = -1
while( !(que.isEmpty()) ){
    let o = que.popleft()
    rN = o[0]
    cN = o[1]
    let cnt = o[2]
    for i in 0..<6 {
        let R = rN + dr[i]
        let C = cN + dc[i]
        if ( 0 <= R && R < N && 0 <= C && C < N && board[C][R] == false){
            if(R == r2 && C == c2){
                print(cnt + 1)
                rN = r2
                cN = c2
                que.In = []
                que.Out = []
                break
            }
            board[C][R] = true
            que.append([R, C, cnt+1])
        }
    }
}
if( rN != r2 || cN != c2 ){
    print(-1)
}
