let N = Int(readLine()!)!
var In = [String]()
for _ in 0..<N {
    In.append(readLine()!)
}
var Out = [String]()
for _ in 0..<N {
    Out.append(readLine()!)
}

var mark = -1
var cnt = 0
for i in 0..<N{
    let idx = Out.firstIndex(of: In[i])!
    if( idx  > mark ){
        mark = idx
        cnt += 1
    }
}
print(N-cnt)
