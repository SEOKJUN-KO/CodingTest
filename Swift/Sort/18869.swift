var input = readLine()!.split(separator:" ").map{ Int($0)! }
let M = input[0], N = input[1]

var universeArr = [[String]]()
for _ in 1...M {
    let tmp = readLine()!.split(separator:" ")
    var arr = [[Int]]()
    for i in 0..<tmp.count { arr.append( [Int(tmp[i])!, i] ) }
    arr = arr.sorted{ $0[0] < $1[0] }
    var tmpArr = [String](); tmpArr.append( String(arr[0][1]) )
    for i in 1..<arr.count {
        if arr[i-1][0] == arr[i][0] {tmpArr.append(String(arr[i][1])+"+")}
        else { tmpArr.append(String(arr[i][1])) }
    }
    universeArr.append(tmpArr)
}

var ans = 0
for i in 0..<M-1 {
    for j in i+1..<M {
        if universeArr[i] == universeArr[j] { ans += 1 }
    }
}
print(ans)
