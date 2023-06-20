let N = Int(readLine()!)!
var people = [[Int]]()

for _ in 1...N {
    people.append( readLine()!.split(separator: " ").map{ Int($0)!} )
}
for i in 0...N-1 {
    var rank = 1
    for j in 0...N-1 {
        if(people[i][0] < people[j][0] && people[i][1] < people[j][1] ){
            rank += 1
        }
    }
    print(rank, terminator: " ")
}
