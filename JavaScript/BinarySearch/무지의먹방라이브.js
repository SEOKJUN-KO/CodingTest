// food_times = 2*10^5
// k = 2*10^13

// food_times[i] = 10^8
// 1 turn ~ 10^8 turn -> 이분탐색 27

function binarySearch(food_times, k) {
    let [s, e] = [0, 10**8+2]
    while(s <= e) {
        const turn = Math.floor((s+e)/2)     
        const arr = []
        let K = k
        for (let i = 0; i < food_times.length; i++) {
            const food = food_times[i]
            if ( turn < food ) {
                arr.push(i)
                K -= turn
            }
            else {
                K -= food    
            }
            if (K < 0) break
        }
        // turn만큼 빼고나서, K가 0 또는  
        if ( K >= 0 && K < arr.length ) {
            return arr[K]+1
            break
        }
        if ( K < 0 ) e = turn - 1
        else if ( K >= arr.length) s = turn + 1
    }
    return -1
}

function solution(food_times, k) {
    return binarySearch(food_times, k);
}