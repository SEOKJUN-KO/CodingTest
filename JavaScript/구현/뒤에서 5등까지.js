function solution(num_list) {
    let answer = [];
    answer = num_list.sort((a, b) => {
        if ( a < b) { return -1 }
        else if ( a == b ) { return 0 } 
        return 1
    })
    
    return answer.slice(0, 5);
}