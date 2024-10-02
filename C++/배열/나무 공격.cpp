#include<iostream>
#include<string>

using namespace std;

int main(int argc, char** argv) {
    int n, m;
    cin >> n >> m;
    int board[n];
    for( int y = 0; y < n; y++ ) {
        board[y] = 0;
        for (int x = 0; x < m; x++) {
            string tmp;
            cin >> tmp;
            if ( stoi(tmp) == 1 ) { board[y] += 1; }
        }
    }
    for ( int i = 1; i <= 2; i++ ) {
        int L, R;
        cin >> L >> R;
        for ( int y = L-1; y <= R-1; y++ ) { board[y] -= 1; }
    }
    int ans = 0;
    for ( int y = 0; y < n; y++ ) { if ( board[y] > 0 ) { ans += board[y]; } }
    cout << ans;
    
    return 0;
}
