var cnt = 0;
var limit = 0;
var ans = 0;
var arr = [];

function backtracking(level, target) {
    if (level === limit) {
        if (target === cnt) {
            ans += 1;
        }
        return ;
    }
    for (var c of [1, -1]) {
        cnt += c*arr[level]
        backtracking(level+1, target)
        cnt -= c*arr[level]
    }
}

function solution(numbers, target) {
    arr = numbers;
    limit = numbers.length;
    backtracking(0, target);
    return ans;
}