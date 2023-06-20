let inputs = readLine()!.split(separator: " ").map{ Int($0)! }
let N = inputs[0]
let L = inputs[1]

var ans = [0.0, 0.0]
var holes = readLine()!.split(separator: " ").map{ Double($0)! }
holes = holes.sorted()

var i = 0
while( i < N ) {
    if( holes[i] > ans[1] ) {
        ans[1] = ( holes[i] - 0.5 ) + Double(L)
        ans[0] += 1
    }
    i += 1
}
print(Int(ans[0]))
