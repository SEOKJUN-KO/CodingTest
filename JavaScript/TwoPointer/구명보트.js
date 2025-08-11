function solution(people, limit) {
    var answer = 0;
    people.sort((a, b) => { return a-b})
    let [l, r] = [0, people.length-1]
    while(l <= r) {
        answer += 1
        const [L, R] = [people[l], people[r]]
        if (L+R <= limit) {
            l += 1
            r -= 1
        }
        else {
            r -= 1
        }
    }
    return answer;
}