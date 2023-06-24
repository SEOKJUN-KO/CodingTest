let inputs = readLine()!.split(separator: " ").map{ Int($0)! }
let N = inputs[0]
let k = inputs[2]
let c = inputs[3]

var arr: [Int] = [Int]()
for _ in 0..<N {
    arr.append(Int(readLine()!)!)
}
arr = arr + Array(arr[0...k-2])
var dic = [Int: Int]()
var ans = 0
for i in 0..<k{
    if(arr[i] != c){
        dic[arr[i]] = dic[arr[i], default: 0]+1
    }
    ans = dic.count
}
for i in k..<arr.count{
    if(arr[i] != c){
        dic[arr[i]] = dic[arr[i], default: 0]+1
    }
    if(arr[i-k] != c){
        dic[arr[i-k]] = dic[arr[i-k], default: 0]-1
    }
    if(dic[arr[i-k]] == 0){
        dic.removeValue(forKey: arr[i-k])
    }
    ans = max(ans, dic.count)
}
print(ans+1)
