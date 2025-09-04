// 주어진 중위 표기식 -> 우선순위에 따라 괄호로 묶기
// 괄호 안의 여난자를 괄호의 오른쪽으로 옮긴다

// a+b/(a-b+c*d+(e*f))+(a+d/e)

const M = new Map()
let n = 0

function find(strArr) {
    let idx = 0
    let str = [...strArr]
    let left = -1
    while(idx < str.length) {
        if (str[idx] === "(") {
            left = idx
        }
        else if(str[idx] === ")") {
            let tmp = str.slice(left+1, idx)
            tmp = first(tmp)
            tmp = second(tmp)
            let changed = change(tmp[0]).join("")
            M.set(n, changed)
            str = [...str.slice(0, left), n, ...str.slice(idx+1)]
            n++
            idx = 0
        }
        idx ++
    }
    return str
}

function first(strArr) {
    let idx = 0
    let str = [...strArr]
    while(idx < str.length) {
        if (str[idx] === "*" || str[idx] === "/") {
            M.set(n, [str[idx-1], str[idx], str[idx+1]])
            str = [...str.slice(0, idx-1), n, ...str.slice(idx+2)]
            n ++
            idx = 0
            continue
        }
        idx++
    }
    return str
}

function second(strArr) {
    let idx = 0
    let str = [...strArr]
    while(idx < str.length) {
        if (str[idx] === "+" || str[idx] === "-") {
            M.set(n, [str[idx-1], str[idx], str[idx+1]])
            str = [...str.slice(0, idx-1), n, ...str.slice(idx+2)]
            n ++
            idx = 0
            continue
        }
        idx++
    }
    return str
}

function change(k) {
    let str = M.get(k)
    if ( typeof str === typeof "" ) {
        M.delete(k)
        return str
    } 
    
    let [A, O, B] = M.get(k)
    if (typeof A === typeof 0) {
        const tmp = A
        A = change(A)
        M.delete(tmp)
    }
    if (typeof O === typeof 0) {
        const tmp = O
        O = change(O)
        M.delete(tmp)
    }
    if (typeof B === typeof 0) {
        const tmp = B
        B = change(B)
        M.delete(tmp)
    }
    M.delete
    if (B === "+" || B === "-" || B === "*" || B === "/") {
        return [...A, ...O, ...B]
    }
    return [...A, ...B, ...O]
}

function main() {
    const fs = require("fs");
    const input = fs.readFileSync(0, "utf-8").trim().split("\n")[0].split("");
    input = find(input)
    input = first(input)
    input = second(input)
    input = change(input[0])
    console.log(input.join(""))
    console.log(M)
}
main()