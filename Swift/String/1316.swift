let N = Int(readLine()!)!
var ans = 0
for _ in 0..<N {
    let input = Array(readLine()!)
    var dict = [Character: Bool]()
    for i in 0..<input.count{
        if( dict[input[i]] == nil ){
            dict[input[i]] = true
        }
        else{
            if(input[i-1] != input[i]){
                break
            }
        }
        if(i == input.count-1){
            ans += 1
        }
    }
}
print(ans)
