let k = Int(readLine()!)!
let inputs = readLine()!.split(separator: " ")

var big = ""
var b = 9
var n = 0
for i in 0..<k{
    if(inputs[i] == ">") {
        var tmp = [b]
        b -= 1
        while(n>0){
            n -= 1
            tmp.append(b)
            b -= 1
        }
        big += tmp.reversed().map{ Character(String($0)) }
    }
    else {
        n += 1
    }
}
if(big.count < k+1){
    var tmp = [b]
    b -= 1
    while( big.count + tmp.count < k+1 ){
        tmp.append(b)
        b -= 1
    }
    big += tmp.reversed().map{ Character(String($0)) }
}

print(big)

var small = ""
var s = k
n = 0
for i in stride(from: k-1, to: -1, by: -1){
    if(inputs[i] == "<") {
        var tmp = [s]
        s -= 1
        while(n>0){
            n -= 1
            tmp.append(s)
            s -= 1
        }
        small += tmp.reversed().map{ Character(String($0)) }
    }
    else {
        n += 1
    }
}
if(small.count < k+1){
    var tmp = [s]
    s -= 1
    while( small.count + tmp.count < k+1 ){
        tmp.append(s)
        s -= 1
    }
    small += tmp.reversed().map{ Character(String($0)) }
}
print( small.reversed().map{ String($0) }.joined(separator: ""))
