// https://school.programmers.co.kr/learn/courses/30/lessons/154538
func solution(_ x:Int, _ y:Int, _ n:Int) -> Int {
    var DP = Array(repeating: 0, count: y+1)
    DP[x] = 1
    for i in (x...y){
        if(i < n){
            if(i%2 == 0 && i%3 == 0 && DP[i/2] != 0 && DP[i/3] != 0){
                DP[i] = min(DP[i/2], DP[i/3])+1
            }
            else if( i%2 == 0 && DP[i/2] != 0){
                DP[i] = DP[i/2]+1
            }
            else if( i%3 == 0 && DP[i/3] != 0){
                DP[i] = DP[i/3]+1
            }
        }
        else{
            if(i%2 == 0 && i%3 == 0 && DP[i/2] != 0 && DP[i/3] != 0 && DP[i-n] != 0){
                DP[i] = min(DP[i/2], DP[i/3], DP[i-n])+1
            }
            else if(i%2 == 0 && i%3 == 0 && DP[i/2] != 0 && DP[i/3] != 0){
                DP[i] = min(DP[i/2], DP[i/3])+1
            }
            else if(i%2 == 0 && DP[i/2] != 0 && DP[i-n] != 0){
                DP[i] = min(DP[i/2], DP[i-n])+1
            }
            else if(i%3 == 0 && DP[i/3] != 0 && DP[i-n] != 0){
                DP[i] = min(DP[i-n], DP[i/3])+1
            }
            else if(i%2 == 0 && DP[i/2] != 0){
                DP[i] = DP[i/2]+1
            }
            else if(i%3 == 0 && DP[i/3] != 0){
                DP[i] = DP[i/3]+1
            }
            else if(DP[i-n] != 0){
                DP[i] = DP[i-n]+1
            }
        }
    }
    return DP[y]-1
}
