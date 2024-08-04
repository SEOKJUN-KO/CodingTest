let inputs = readLine()!.split(separator:" ").map{ Int($0.split(separator:":")[0])!*60 + Int($0.split(separator:":")[1])! }
var S = inputs[0], E = inputs[1], Q = inputs[2]
var dict = Set<String>()
var ans = Set<String>()
while true  {
    var input2 : String? = nil
    input2 = readLine()
    if input2 == nil || input2! == "" { break }
    let str = input2!.split(separator:" ")
    let time = Int(str[0].split(separator:":")[0])!*60 + Int(str[0].split(separator:":")[1])!
    let name = String(str[1])
    if time <= S {
        dict.insert(name)
    }
    else if E <= time && time <= Q {
        if dict.contains(name) {
            ans.insert(name)
        }
    }
}
print(ans.count)
