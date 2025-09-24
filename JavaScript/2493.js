function solution() {
    const fs = require('fs')
    const input = fs.readFileSync('input.txt', 'utf-8').trim().split("\n");
    const N = Number(input[0])
    const buildings = input[1].trim().split(" ").map(Number)
    
    stack = []
    for(let i = N-1; i >= 0; i--) {
        while( stack.length > 0 && buildings[i] > stack[stack.length-1][0] ) {
            const [_, idx] = stack.pop()
            buildings[idx] = String(i+1)
        }
        stack.push([ buildings[i], i ])
    }
    while(stack.length > 0) {
        const [_, idx] = stack.pop()
        buildings[idx] = '0'
    }
    console.log(buildings.join(" "))
}

solution()