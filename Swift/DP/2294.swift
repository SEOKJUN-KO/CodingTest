let inputs = (readLine()!).split(separator: " ").map{Int(String($0))!}
var N = inputs[0]
var K = inputs[1]

var coins = [Int]()
for _ in 1...N { coins.append(Int(readLine()!)!) }
var tmpCoins = Set(coins)
coins = Array(tmpCoins).sorted()

var DP = Array(repeating: 0, count: K+1)

for i in 0...coins.count-1{
    if(coins[i] <= K){ DP[coins[i]] = 1 }
    if(coins[i]+1 <= K){
        for j in coins[i]+1...K{
            let idx = j - coins[i]
            if(DP[idx] != 0){
                if(DP[j] == 0){ DP[j] = DP[idx]+1 }
                else{ if(DP[j] > DP[idx]+1){ DP[j] = DP[idx]+1 } }
            }
        }
    }
}
if(DP.last! == 0){ print(-1) }
else{ print(DP.last!) }
