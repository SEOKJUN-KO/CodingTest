function solution(order) {
    const belt = []
    let point = 0
    for(let i = 1; i <= order.length; i++) {
        if (order[point] === i) {
            point += 1
        }
        else {
            belt.push(i)
        }
        while(belt.length > 0 && order[point] === belt[belt.length-1]) {
            point += 1
            belt.pop()
        }
    }

    return point;
}