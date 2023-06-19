let N = Int(readLine()!)!
var arr = [[Int]]()
for _ in 1...N {
    let inputs = readLine()!.split(separator: " ").map{ Int($0)! }
    arr.append(inputs)
}

arr = arr.sorted(by: { ($0[1], $0[0]) < ($1[1], $1[0]) })
for i in 0...N-1 {
    print(arr[i].map{ String($0) }.joined(separator: " ") )
}
