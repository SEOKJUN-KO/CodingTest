let N = Int(readLine()!)!
let snows = readLine()!.split(separator:" ").map{ Int($0)! }.sorted()
var ans = Int.max
for i in 0..<snows.count-1 {
    for j in (i+1...snows.count-1).reversed() {
        let outL = i, outR = j, outS = snows[outL] + snows[outR]
        var inL = i+1, inR = j-1, inS = snows[inL] + snows[inR]
        while( inL < inR ) {
            let tmp = abs(outS-inS)
            if tmp < ans { ans = tmp }
            if inS == outS { ans = 0; break }
            if inS < outS { inL += 1 }
            else { inR -= 1 }
            if inL == outR || inR == outL { break }
            inS = snows[inL] + snows[inR]
        }
        if ans == 0 { break }
    }
    if ans == 0 { break }
}
print(ans)
