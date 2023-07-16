let N = Int(readLine()!)!
let nums = readLine()!.split(separator: " ").map{ Int($0)! }
let inputs = readLine()!.split(separator: " ").map{ Int($0)! }

let ops = Array(repeating: "+", count: inputs[0]) + Array(repeating: "-", count: inputs[1]) + Array(repeating: "*", count: inputs[2]) + Array(repeating: "/", count: inputs[3])
var visited = Array(repeating: false, count: ops.count)

var ansMax = Int.min
var ansMin = Int.max
func backT(_ deep: Int, _ total: Int){
    if(deep == ops.count){
        if( ansMax < total ){
            ansMax = total
        }
        if( ansMin > total){
            ansMin = total
        }
        return
    }
    for i in 0..<ops.count{
        if(visited[i] == false){
            visited[i] = true
            if(ops[i] == "+"){
                backT(deep+1, total+nums[deep+1])
            }
            else if(ops[i] == "-"){
                backT(deep+1, total-nums[deep+1])
            }
            else if(ops[i] == "*"){
                backT(deep+1, total*nums[deep+1])
            }
            else{
                backT(deep+1, total > 0 ? total/nums[deep+1] : -(-total/nums[deep+1]))
            }
            visited[i] = false
        }
    }
}
backT(0, nums[0])
print(ansMax)
print(ansMin)
