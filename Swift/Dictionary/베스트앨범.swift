/* 장르별 재생 높은 노래 두개
# 수록 기준
# 1. 속한 노래가 많이 재생된 장르 = 총 플레이 수가 높은 장르부터 v
# 2. 장르 내에서 많이 재생된 노래 plays[i] = 같은 장르 내에서 재생 횟수가 많은 것
# 3. 장르 내에서 재생 횟수가 같은 노래 중 고유 번호가 낮은 노래 = 같은 장르 내에서 재생 횟수가 같을 때, 고유 번호가 작은 것
# 고유번호 i */

func solution(_ genres:[String], _ plays:[Int]) -> [Int] {
    var (dictSumPlay, dictPlay) = ( [String: Int](), [String: [Int: [Int] ]]() )
    for i in (0..<genres.count) {
        if dictSumPlay[genres[i]] == nil {
            dictSumPlay[genres[i]] = 0
            dictPlay[genres[i]] = [Int:[Int]]()
        }
        dictSumPlay[genres[i]]! += plays[i]
        if dictPlay[genres[i]]![plays[i]] == nil {
            dictPlay[genres[i]]![plays[i]] = []
        }
        dictPlay[genres[i]]![plays[i]]!.append(i)
    }
    var mostGenre = [Int:String]()
    for key in dictSumPlay.keys {
        mostGenre[dictSumPlay[key]!] = key
    }
    var keyArr = Array(mostGenre.keys)
    keyArr = keyArr.sorted(by: { $1 < $0 })
    var genreKeyArr = [String]()
    for key in keyArr {
        genreKeyArr.append(mostGenre[key]!)
    }
    var ans = [Int]()
    for genre in genreKeyArr {
        var tmp = 0
        var tmpKeyArr = Array(dictPlay[genre]!.keys)
        tmpKeyArr = tmpKeyArr.sorted(by: { $1 < $0 })
        for tmpKey in tmpKeyArr {
            for index in dictPlay[genre]![tmpKey]! {
                ans.append(index)
                tmp += 1
                if tmp == 2 { break }
            }
            if tmp == 2 { break }
        }
    }
    return ans
}
