let str1 = [" "]+Array(readLine()!)
let str2 = [" "]+Array(readLine()!)
var DP = Array(repeating: Array(repeating: 0, count: str1.count), count: str2.count)

for i in 1..<str2.count {
    for j in 1..<str1.count {
        if( str2[i] == str1[j] ){
            DP[i][j] = DP[i-1][j-1] + 1
        }
        else{
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])
        }
    }
}

let n = DP.last!.last!
print(n)
if( n != 0 ){
    var ans = [Character]()
    var i = str2.count-1
    var j = str1.count-1
    while( i > 0 && j > 0 && DP[i][j] != 0 ) {
        if( DP[i][j-1] == DP[i][j]) { j -= 1 }
        else if( DP[i-1][j-1] + 1 == DP[i][j] && str2[i] == str1[j] ){
            ans.append(str2[i])
            i -= 1
            j -= 1
        }
        else { i -= 1 }
    }
    print(ans.reversed().map{ String($0) }.joined(separator: ""))
}
