function solution(x1, x2, x3, x4) {
    let A = x1 | x2
    let B = x3 | x4
    
    return A & B ? true : false
}