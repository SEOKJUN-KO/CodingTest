const used = new Set();

function backtracking(set, str) {
    if (str !== "" && !used.has(str) ) {
        used.add(str)
    }
    if(set.size >= 4) {
        return
    }
    
    for( const e of ["aya", "ye", "woo", "ma"]) {
        if ( !set.has(e) ) {
            set.add(e); 
            backtracking(set, str+e)
            set.delete(e); 
        }
    }
}

function solution(babbling) {
    let ans = 0
    backtracking(new Set(), "")
    babbling.forEach((e)=> {
        if (used.has(e)) {
            ans += 1
        }
    })
    return ans;
}