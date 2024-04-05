// 유일성 && 최소성

var keySet = Set<[Int]>()
var tmp = Set<Int>()
func makeKeyArr(_ idx: Int, _ L: Int, _ N: Int) {
    if tmp.count == N {
        keySet.insert( Array(tmp).sorted(by: { $0 < $1 }) )
        return
    }
    for i in 0..<L {
        if !tmp.contains(i) {
            tmp.insert(i)
            makeKeyArr(i, L, N)
            tmp.remove(i)
        }
    }
}

func solution(_ relation:[[String]]) -> Int {
    let L = relation[0].count
    for l in 1...L { makeKeyArr(0, L, l) }
    var keyArr = Array(keySet).sorted(by: { $0.count < $1.count })
    var keySave = Set<[Int]>()
    var ans = 0
    for i in 0..<keyArr.count{
        var arr = Set<String>()
        for rel in relation {
            var tmp = ""
            for key in keyArr[i] {
                tmp += rel[key]
            }
            arr.insert(tmp)
        }
        if arr.count == relation.count {
            var tmp = [Int]()
            for key in keyArr[i] {
                tmp.append(key)
            }
            let s = Set(tmp)
            var flag = true
            for key in keySave {
                let q = s.intersection(Set(key))
                if q.count == key.count { flag = false; break }
            }
            if flag { keySave.insert(keyArr[i]) }
        }
    }
    return keySave.count
}
