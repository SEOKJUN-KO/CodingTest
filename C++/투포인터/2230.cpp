#include <iostream>
#include <deque>
#include <algorithm>

using namespace std;

bool cmp(int a, int b) { return a < b; }

int main() {
    int N, M;
    cin >> N >> M;
    deque<int> arr;
    for (int i=0; i<N; i++) {
        int tmp; cin >> tmp;
        arr.push_back(tmp);
    }
    sort(arr.begin(), arr.end(), cmp);
    int left=0, right=0;
    int ans = 2000000000;
    while ( left <= right && right < N ) {
        if ( arr[right]-arr[left] == M ) {
            ans = M;
            break;
        }
        else if ( arr[right]-arr[left] > M) {
            if ( arr[right]-arr[left] < ans ) { ans = arr[right]-arr[left]; }
            left += 1;
        }
        else { right += 1; }
    }
    cout << ans;
    return 0;
}
