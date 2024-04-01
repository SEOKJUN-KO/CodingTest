// 셔틀 9:00 -
// n 번 t분 간격, 최대 m명
func timeToMin(_ cnt: Int, _ t: Int) -> String {
    let T = 9*60+(cnt*t)
    var (hour, minute) = (T/60, T%60)
    var (hourStr, minuteStr) = ("", "")
    hourStr = String(hour).count == 1 ? "0\(hour)" : "\(hour)"
    minuteStr = String(minute).count == 1 ? "0\(minute)" : "\(minute)"
    return "\(hourStr):\(minuteStr)"
}

func timeToMinTwo(_ str: String) -> String {
    let time = str.split(separator: ":").map{ Int($0)! }
    let T = time[0]*60+time[1]-1
    var (hour, minute) = (T/60, T%60)
    var (hourStr, minuteStr) = ("", "")
    hourStr = String(hour).count == 1 ? "0\(hour)" : "\(hour)"
    minuteStr = String(minute).count == 1 ? "0\(minute)" : "\(minute)"
    return "\(hourStr):\(minuteStr)"
}

func solution(_ n:Int, _ t:Int, _ m:Int, _ timetable:[String]) -> String {
    var arriveArr = timetable.sorted(by: { $0 > $1 })
    var busArr = [String]()
    for i in (0..<n) {
        busArr.append(timeToMin(i, t))
    }
    var ans = ""
    for bus in busArr {
        var cnt = 0
        while(!arriveArr.isEmpty) {
            let fast = arriveArr.last!
            if fast <= bus {
                cnt += 1
                _ = arriveArr.popLast()
                if cnt == m {
                    ans = timeToMinTwo(fast)
                    break
                }
                continue
            }
            break
        }
        if cnt != m {
            ans = bus
        }
    }
    return ans
}
