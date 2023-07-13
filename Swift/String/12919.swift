struct Queue {
    var In = [[Character]]()
    var Out = [[Character]]()
    
    func isEmpty()->Bool{
        if( In.count == 0 && Out.count == 0 ){
            return true
        }
        return false
    }
    
    mutating func append(_ val: [Character]){
        In.append(val)
    }
    
    mutating func popleft()->[Character]{
        if(isEmpty()){
            return ["N"]
        }
        if(Out.count == 0){
            Out = In.reversed()
            In = []
        }
        return Out.popLast()!
    }
}

var S = Array(readLine()!)
var T = Array(readLine()!)

if( S.count > T.count ){
    ( S, T ) = ( T, S )
}
var que = Queue()
que.append(T)
var ans = 0
while( !(que.isEmpty()) ){
    var now = que.popleft()
    if(now[0] == "A" && now.last! == "A"){
        _ = now.popLast()
        if(now.count > S.count){
            que.append(now)
        }
        else if(now.count == S.count && now == S){
            ans = 1
            break
        }
    }
    else if(now[0] == "A" && now.last! == "B"){
        continue
    }
    else if(now[0] == "B" && now.last! == "B"){
        now = now.reversed()
        _ = now.popLast()
        if(now.count > S.count){
            que.append(now)
        }
        else if(now.count == S.count && now == S){
            ans = 1
            break
        }
    }
    else if(now[0] == "B" && now.last! == "A"){
        var tmpA = now
        var tmpB = now
        _ = tmpA.popLast()
        tmpB = tmpB.reversed()
        _ = tmpB.popLast()
        if(tmpA.count > S.count){
            que.append(tmpA)
            que.append(tmpB)
        }
        else if(tmpA.count == S.count && tmpA == S || tmpB == S){
            ans = 1
            break
        }
    }
}
print(ans)
