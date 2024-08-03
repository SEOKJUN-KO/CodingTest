import Foundation
var N = Int(readLine()!)!

func getPrime(_ n: Int) -> [Int] {
    // 0과 1은 소수가 아니므로 false로 시작합니다.
    guard n >= 2 else { return [] }
    
    // 초기화: 모든 수를 소수라고 가정
    var isPrime = [Bool](repeating: true, count: n + 1)
    isPrime[0] = false
    isPrime[1] = false
    
    // 소수 여부 결정
    for p in 2...( Int( sqrt( Double(n)) ) + 1) {
        if isPrime[p] {
            // p의 배수들을 소수가 아니라고 표시
            for multiple in stride(from: p * p, through: n, by: p) {
                isPrime[multiple] = false
            }
        }
    }
    
    // 소수 리스트 생성
    var primes = [Int]()
    for i in 2...n {
        if isPrime[i] {
            primes.append(i)
        }
    }
    return primes
}
var arr = getPrime(N)
if arr == [] {
    print(0)
}
else {
    var L = 0, R = 0, S = arr[0], ans = 0
    let length = arr.count
    while(L <= R && R <= length) {
        if S > N {
            S -= arr[L]
            L += 1
        }
        else if S == N {
            ans += 1
            R += 1
            if R == length {
                break
            }
            S += arr[R]
        }
        else if S < N {
            R += 1
            if R == length {
                break
            }
            S += arr[R]
        }
    }
    print(ans)
}
