#include<iostream>
#include<queue>
#include<algorithm>
#include<tuple>
using namespace std;
// S 수연, D 여신, X 돌, * 악마
int main(int argc, char** argv) {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for(int test_case = 1; test_case <= T; test_case++) {
        cout << "#" << test_case << " ";
        int N, M;
        cin >> N >> M;
        string board[N][M], tmp;
        queue<tuple<int, int, int, int>> que;
        tuple<int, int, int, int> sp;
        for( int i = 0; i < N; i++ ) {
            cin >> tmp;
            for( int j = 0; j < M; j++ ) {
                board[i][j] = tmp[j];
                if ( tmp[j] == '*' ) que.push( make_tuple(j, i, 1, -1) );
                else if ( tmp[j] == 'S' ) sp = make_tuple(j, i, 0, 0);
            }
        }
        
        que.push(sp);
        int dx[4] = {1, -1, 0, 0}, dy[4] = {0, 0, 1, -1};
        bool flag = false;
        
        while( !que.empty() ) {
            auto cur = que.front(); que.pop();
            int nx = get<0>(cur); int ny = get<1>(cur);
            int mode = get<2>(cur); int time = get<3>(cur);
            for ( int i = 0; i < 4; i++ ) {
                int X = nx + dx[i]; int Y = ny + dy[i];
                if ( X < 0 || X >= M || Y < 0 || Y >= N ) continue;
                if (board[Y][X] == "X") continue;
                if (mode == 1) {
                    if ( board[Y][X] == "*" || board[Y][X] == "D") continue;
                    board[Y][X] = "*";
                    que.push(make_tuple(X, Y, 1, -1));
                } else {
                    if( board[Y][X] == "*" ) continue;
                    if( board[Y][X] == "D") {
                        flag = true;
                        cout << time+1 << "\n";
                        break;
                    }
                    else if (board[Y][X] == ".") {
                        board[Y][X] = "c";
                        que.push(make_tuple(X, Y, 0, time+1));
                    }
                }
            }
            if (flag) break;
        }
        if (!flag) cout << "GAME OVER" << "\n";
  }
  return 0;
}
