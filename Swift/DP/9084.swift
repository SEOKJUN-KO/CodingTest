let T = Int(readLine()!)!
for _ in 1...T{
    let N = Int(readLine()!)!
    let coins = readLine()!.split(separator: " ").map{Int(String($0))!}
    let M = Int(readLine()!)!
    var DP = [Int](repeating: 0, count: M+1)
    DP[0] = 1
    for i in 0...N-1{
        if(coins[i]<=M){
            for j in coins[i]...M{
                DP[j] += DP[ j - coins[i] ]
            }
        }
    }
    print(DP[M])
}

