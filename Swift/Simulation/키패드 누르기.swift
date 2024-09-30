func solution(_ numbers:[Int], _ hand:String) -> String {
    let left = Set<Int>([1, 4, 7,])
    let mid = Set<Int>([2, 5, 8, 0])
    let right = Set<Int>([3, 6, 9])
    
    var ans = ""
    
    var lHand = [3, 0], rHand = [3, 2]
    
    for n in numbers {
        if left.contains(n) {
            ans += "L"
            lHand = [n/3, 0]
        }
        else if right.contains(n) {
            ans += "R"
            rHand = [(n-2)/3, 2]
        }
        else {
            var tmp = n
            if tmp == 0 { tmp = 11 }
            let m = [(tmp-1)/3, 1]
            let l = abs(lHand[0]-m[0])+abs(lHand[1]-m[1])
            let r = abs(rHand[0]-m[0])+abs(rHand[1]-m[1])
            if l == r {
                if hand == "left" { ans += "L"; lHand = [(tmp-1)/3, 1] }
                else { ans += "R"; rHand = [(tmp-1)/3, 1] }
            }
            else if l > r { ans += "R"; rHand = [(tmp-1)/3, 1] }
            else { ans += "L"; lHand = [(tmp-1)/3, 1] }
        }
    }
    return ans
}
