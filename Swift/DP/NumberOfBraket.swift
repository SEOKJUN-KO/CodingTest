func solution(_ n:Int) -> Int {
    var A = [0, 1, 1]
    var N = [0, 1, 2]
    if (n <= 2){
        return N[n]
    }
    for i in 3...n{
        A.append(N[i-1])
        var tmp = N[i-1]
        for j in 1...i-1{
            tmp += A[j]*N[i-j]
        }
        N.append(tmp)
    }
    return N.last!
}
