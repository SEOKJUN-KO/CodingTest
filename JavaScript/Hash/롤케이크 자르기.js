function solution(topping) {
    var ans = 0;
    const aDict = new Map();
    const bDict = new Map();
    
    topping.forEach((e) => {
        if (bDict.get(e) === undefined) { bDict.set(e, 0)}
         bDict.set(e, bDict.get(e)+1)
    })
    
    topping.forEach((e)=> {
        if (aDict[e] === undefined) { aDict.set(e, 0)}
        aDict.set(e, aDict.get(e)+1)
        
        bDict.set(e, bDict.get(e)-1)
        if (bDict.get(e) === 0) { bDict.delete(e) }
        
        if (aDict.size === bDict.size) {
            ans += 1
        }
    })
    return ans;
}