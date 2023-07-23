func solution(_ players:[String], _ callings:[String]) -> [String] {
    var dictName2Num = [String: Int]()
    var dictNum2Name = [Int: String]()
    var n = 1
    for p in players{
        dictName2Num[p] = n
        n += 1
    }
    for k in dictName2Num.keys{
        dictNum2Name[ dictName2Num[k]! ] = k
    }
    for c in callings{
        let nowN = dictName2Num[c]!
        let now = c
        let frontN = nowN - 1
        let front = dictNum2Name[frontN]!
        dictName2Num[now] = frontN
        dictNum2Name[frontN] = now
        dictNum2Name[nowN] = front
        dictName2Num[front] = nowN
    }
    var ans = [String]()
    for k in dictNum2Name.keys.sorted(){
        ans.append(dictNum2Name[k]!)
    }
    return ans
}
