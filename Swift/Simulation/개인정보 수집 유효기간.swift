func solution(_ today:String, _ terms:[String], _ privacies:[String]) -> [Int] {
    
    var dict = [String: Int]()
    var typeDict = [String: Int]()
    let Y = 12*28, M = 28
    let todayArr = today.split(separator: ".")
    var todayInt = Int(todayArr[0])!*Y + Int(todayArr[1])!*M + Int(todayArr[2])!
    for term in terms {
        let ret = term.split(separator: " ")
        let type = String(ret[0]), month = ret[1]
        typeDict[type] = Int(month)!
    }
    var ans = [Int]()
    for i in 0..<privacies.count {
        let ret = privacies[i].split(separator: " ")
        let date = ret[0].split(separator: ".")
        let type = String(ret[1])
        let nowInt = Int(date[0])!*Y + ( Int(date[1])! + typeDict[type]! )*M + Int(date[2])!
        if nowInt <= todayInt { ans.append(i+1) }
    }
    return ans
}
