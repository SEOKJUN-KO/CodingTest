//https://school.programmers.co.kr/learn/courses/30/lessons/181188?language=swift

func solution(_ targets:[[Int]]) -> Int {
    var answer = 1
    var target = targets.sorted{ $0[1] < $1[1] }
    var m = Double(target[0][1]) - 0.5
    for t in target[1...]{
        if(m < Double(t[0])){
            answer += 1
            m = Double(t[1]) - 0.5
        }
    }
    return answer
}
