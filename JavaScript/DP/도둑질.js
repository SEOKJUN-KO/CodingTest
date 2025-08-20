function dp(money, DP) {
    for( let i = 1; i < money.length; i++ ) { //10^7
        let A = DP[DP.length-1][1] + money[i]
        if( i === money.length-1 && DP[0][0] != 0) { A -= money[i] } 
        let B = Math.max(...DP[DP.length-1])
        DP.push([A, B])
    }
    return Math.max(...DP[DP.length-1])
}

function init(money) {
    const DPA = [[money[0], 0]]
    const DPB = [[0, 0]]
    let A = dp(money, DPA)
    let B = dp(money, DPB)
    return Math.max(A, B)
}

function solution(money) {
    var answer = 0;
    answer = init(money)
    return answer;
}