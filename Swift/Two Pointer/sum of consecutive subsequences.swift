// https://school.programmers.co.kr/learn/courses/30/lessons/178870

func solution(_ sequence:[Int], _ k:Int) -> [Int] {
    var left = 0
    var right = 0 
    var s = sequence[0]
    var leng = sequence.count
    var ans = Int.max
    var result = [Int]()
    while( left <= right && left < leng && right < leng){
        if(s >= k){
            if(s == k && right-left+1 < ans){
                ans = right-left+1
                result = [left, right]
            }
            s -= sequence[left]
            left += 1
        }
        else{
            right += 1
            if(right == leng){ break }
            s += sequence[right]
        }
    }
    return result
}
