var input = readLine()!.split(separator:" ").map{ Int($0)! }; var N = input[0], S = input[1]
var arr = readLine()!.split(separator:" ").map{ Int($0)! }
var L = 0, R = 0
var l = Int.max, ans = arr[0]
while( L <= R && R < N ) {
    if ans >= S {
        ans -= arr[L]
        if l >= (R-L+1) l = (R-L+1)
        L += 1
    }
    else {
        R += 1
        if (R-L+1) >= l {
            ans -= arr[L]
            L += 1
        }
        if R == N break
        ans += arr[R]
    }
}
if l == Int.max print(0)
else print(l)
