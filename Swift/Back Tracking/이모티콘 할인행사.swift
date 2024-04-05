// 4 * 2 * 7 * 100
// 1. 구독 가입
// 2. 이모티콘 판매액 최대
// => [구독 수, 매출액]
var discountArr = [[Int]]()
var discountTmp = [Int]()

func backTDiscount() {
    if emoticonArr.count == discountTmp.count {
        discountArr.append(discountTmp)
        return
    }
    for discount in [10, 20, 30, 40] {
        discountTmp.append(discount)
        backTDiscount()
        _ = discountTmp.popLast()
    }
}

func solution(_ users:[[Int]], _ emoticons:[Int]) -> [Int] {
    backTDiscount()
    var (maxSub, maxCost) = (0, 0)
    for dArr in discountArr { // 4^7 [[ 10, 10 ], [10, 20]]
        var (subTmp, costTmp) = (Set<Int>(), 0)
        var userPay = Array(repeating: 0, count: users.count)
        for i in 0..<dArr.count {
            for j in 0..<users.count {
                let (discountLimit, scribeLimit) = (users[j][0], users[j][1])
                if dArr[i] < discountLimit { continue }
                if !subTmp.contains(j) {
                    userPay[j] += emoticons[i]/100*(100-dArr[i])
                    if userPay[j] >= scribeLimit {
                        subTmp.insert(j)
                        userPay[j] = 0
                    }
                }
            }
        }
        for pay in userPay {
            costTmp += pay
        }
        if maxSub < subTmp.count {
            maxSub = subTmp.count
            maxCost = costTmp
        }
        else if maxSub == subTmp.count && maxCost < costTmp {
            maxCost = costTmp
        }
    }
    return [maxSub,maxCost]
}
