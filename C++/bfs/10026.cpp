#include <iostream>
#include <deque>
#include <tuple>
#include <set>

using namespace std;

int N = 0;

int bfs(deque<deque<char>> board, set<char> s) {
    int dy[4] = {1, -1, 0, 0};
    int dx[4] = {0, 0, 1, -1};
    int cnt = 0;
    for ( int y = 0; y < N; y++ ) {
        for ( int x = 0; x < N; x++ ) {
            if ( board[y][x] != 'N' ) {
                cnt += 1;
                deque<tuple<int, int, char>> que;
                que.push_back( make_tuple(y, x, board[y][x]) );
                char start = board[y][x]; board[y][x] = 'N';
                while(que.size() > 0) {
                    auto cur = que.front(); que.pop_front();
                    int ny = get<0>(cur); int nx = get<1>(cur); char ns = get<2>(cur);
                    for ( int i = 0; i <= 3; i++ ) {
                        int Y = ny+dy[i], X = nx+dx[i];
                        if ( 0 <= Y && Y < N && 0 <= X && X < N && board[Y][X] != 'N') {
                            if ( start == 'B' && board[Y][X] == 'B') {
                                que.push_back(make_tuple(Y, X, board[Y][X]));
                                board[Y][X] = 'N';
                            }
                            else if ( start != 'B' && (s.count(board[Y][X]) == 1 || ns == board[Y][X]) ) {
                                que.push_back(make_tuple(Y, X, board[Y][X]));
                                board[Y][X] = 'N';
                            }
                        }
                    }
                }
            }
        }
    }
    return cnt;
}

int main() {
    cin >> N;
    deque<deque<char>> board1, board2;
    for ( int y = 0; y < N; y++ ) {
        board1.push_back({});
        board2.push_back({});
        string tmp;
        cin >> tmp;
        for ( int x = 0; x < N; x++ ) {
            board1[y].push_back(tmp[x]);
            board2[y].push_back(tmp[x]);
        }
    }
    set<char> s1, s2;
    s1.insert(' ');
    s2.insert('R'); s2.insert('G');
    
    cout << bfs(board1, s1) << " ";
    cout << bfs(board2, s2);
    return 0;
}
