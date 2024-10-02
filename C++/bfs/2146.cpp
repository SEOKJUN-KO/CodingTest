#include <iostream>
#include <deque>
#include <tuple>
#include <cstdlib>

using namespace std;

int N = 0;

void bfs(deque<deque<int>>& board, deque<deque<tuple<int, int>>>& arr, int y, int x) {
    deque<tuple<int, int>> que; que.push_back(make_tuple(y, x));
    board[y][x] = 2;
    int dy[4] = {1, -1, 0, 0}, dx[4] = {0, 0, 1, -1};
    while(que.size() > 0) {
        auto cur = que.front(); que.pop_front();
        int ny = get<0>(cur), nx = get<1>(cur);
        bool flag = false;
        for (int i = 0; i < 4; i++) {
            int Y = ny+dy[i], X = nx+dx[i];
            if ( 0 <= Y && Y < N && 0 <= X && X < N) {
                if ( board[Y][X] == 1 ) { que.push_back(make_tuple(Y, X)); board[Y][X] = 2; }
                else if ( board[Y][X] == 0 ) { flag = true; }
            }
        }
        if (flag) { arr[arr.size()-1].push_back(make_tuple(ny, nx)); }
    }
}

int main() {
    cin >> N;
    deque<deque<int>> board;
    deque<deque<tuple<int, int>>> arr;
    for (int y = 0; y < N; y++) {
        board.push_back({});
        for (int x = 0; x < N; x++) {
            int tmp;
            cin >> tmp;
            board[y].push_back(tmp);
        }
    }
    int cnt = 0;
    for (int y = 0; y < N; y++) {
        for (int x = 0; x < N; x++) {
            if (board[y][x] == 1) {
                arr.push_back({});
                bfs(board, arr, y, x);
                cnt += 1;
            }
        }
    }
    int ans = 999999999;
    for ( int i = 0; i < cnt-1; i++ ) {
        for ( int j = 0; j < arr[i].size(); j++ ) {
            auto cur = arr[i][j];
            int ny = get<0>(cur), nx = get<1>(cur);
            for ( int k = i+1; k < cnt; k++ ) {
                for ( int l= 0; l < arr[k].size(); l++ ) {
                    auto curr = arr[k][l];
                    int nyy = get<0>(curr), nxx = get<1>(curr);
                    if ( ans > abs(ny-nyy)+abs(nx-nxx) ) {
                        ans = abs(ny-nyy)+abs(nx-nxx);
                    }
                }
            }
        }
    }
    cout << ans-1;
    return 0;
}
