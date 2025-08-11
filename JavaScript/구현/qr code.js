function solution(q, r, code) {
    var ans = '';
    let baseIdx = 0  
    while(baseIdx+r < code.length) {
        ans += code[baseIdx+r]
        baseIdx += q
    }
    return ans;
}