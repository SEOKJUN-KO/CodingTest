let plusCross = []
let minusCross = []
let useX = []
let ans = 0

function calculateCrossLine(y, x) {
    // plus
    // [0, 0]
    // [1, 0] [0, 1]
    // [2, 0] [1, 1] [0, 2]
    
    // minus
    // [n-1, 0]
    // [n-2, 0], [n-1, 1]
    // [n-3, 0], [n-2, 1], [n-1, 2]
    return [y+x, y-x]
}

function backTracking(n, y) {
    if (y >= n) { 
        ans += 1
        return
    }
    for( let x = 0; x < n; x++ ) {
        const [pU, mU] = calculateCrossLine(y, x)
        if( !useX[x] && !plusCross[pU] && !minusCross[mU] ) {
            useX[x] = true; plusCross[pU] = true; minusCross[mU] = true
            backTracking(n, y+1)
            useX[x] = false; plusCross[pU] = false; minusCross[mU] = false
        }
    }
}

function solution(n) {
    for ( let i = 1; i < 2*n; i++ ) {
        plusCross.push(false)
        minusCross.push(false)
        useX.push(false)
    }
    backTracking(n, 0)
    return ans;
}