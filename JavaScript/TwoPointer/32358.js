const fs = require("fs");


function throwTrash(trashList, p) {
    trashList.push(p)
}

function binary_search(now, trashList) {
    let [l, r] = [0, trashList.length-1]
    let startP = -1
    let minL = Number.MAX_VALUE
    while(l <= r) {
        let mid = Math.floor( (l+r)/2 )

        if (trashList[mid] == now) {
            return mid
        }
        
        if (trashList[mid] > now) { r = mid - 1 }
        else { l = mid + 1 }

        if ( Math.abs(trashList[mid]-now) === minL && startP > mid ) {
            startP = mid
        }
        else if ( Math.abs(trashList[mid]-now) < minL ) {
            startP = mid
            minL = Math.abs(trashList[mid]-now)
        }
    }
    return startP
}

function twoPointer(now, trashList) {
    let startP = binary_search(now, trashList)
    let [s, e] = [startP, startP]

    let move = Math.abs(now - trashList[startP])
    let nowP = trashList[startP]
    while(s >= 0 && e < trashList.length) {
        if ( Math.abs(trashList[s]-nowP) <= Math.abs(trashList[e]-nowP) ){
            move += Math.abs(trashList[s]-nowP)
            nowP = trashList[s]
            s -= 1
        }
        else {
            move += Math.abs(trashList[e]-nowP)
            nowP = trashList[e]
            e += 1
        }
    }
    while ( s >= 0 ) {
        move += Math.abs(trashList[s]-nowP)
        nowP = trashList[s]
        s -= 1
    }
    while( e < trashList.length ) {
        move += Math.abs(trashList[e]-nowP)
        nowP = trashList[e]
        e += 1
    }
    return [nowP, move]
}


function solution() {
    let input = fs.readFileSync('input.txt', 'utf-8').trim().split("\n")
    let N = Number(input[0].trim())
    
    let trashList = []
    let now = 0
    let move = 0
    for( let i = 1; i <= N; i++ ) {
        const inputD = input[i].trim().split(" ").map(Number)
    
        if (inputD[0] === 1) {
            throwTrash(trashList, inputD[1])
        }
        else {
            if (trashList.length === 0) { continue }
            trashList.sort((a, b) => a-b)
            const ret = twoPointer(now, trashList)
            now = ret[0]
            move += ret[1]
            trashList = []    
        }
    }
    console.log(move)
}

solution()