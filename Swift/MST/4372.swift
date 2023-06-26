let T = Int(readLine()!)!

var P = [Int]()
func findP(_ idx: Int)->Int{
    if(idx == P[idx]){
        return idx
    }
    return findP(P[idx])
}

func union(_ x: Int, _ y: Int)->Bool{
    let X = findP(x)
    let Y = findP(y)
    if(X == Y){
        return false
    }
    else if( X < Y ){
        P[Y] = X
    }
    else{
        P[X] = Y
    }
    return true
}

for _ in 1...T {
    let inputs = readLine()!.split(separator: " ").map{ Int($0)! }
    var cnt = 0
    P = Array<Int>(0...inputs[0])
    for _ in 1...inputs[1] {
        let nodes = readLine()!.split(separator: " ").map{ Int($0)! }
        if(union(nodes[0], nodes[1])){
            cnt += 1
        }
    }
    print(cnt)
}
