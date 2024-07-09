#include<iostream>
#include<queue>
using namespace std;

int main(int argc, char** argv)
{
  for(int t = 1; t <= 10; t++)
  {
        int T;
    int board[101][101];
        queue<pair<int, int>> que;
        cin >> T;
        for( int i = 0; i < 100; i++) {
      for( int j = 0; j < 100; j++) {
                cin >> board[i][j];
                if( i == 99 && board[i][j] == 2 ) {
                    que.push( {j, i} );
                }
            }
        }
        int dx[3] = {1, -1, 0};
        int dy[3] = {0, 0, -1};
        bool flag = false;
        while( !que.empty() ) {
            if (flag) break;
          auto cur = que.front(); que.pop();
            for( int i = 0; i < 3; i++ ) {
                int X = cur.first + dx[i];
                int Y = cur.second + dy[i];
                 if( X < 0 || X >= 100 || Y < 0 || Y >= 100) continue;
                if( board[Y][X] == 1 ) {
                    if( Y == 0 ) {
                        cout << "#" << t << " " << X << endl;
                        flag = true;
                    } else {
                        board[Y][X] = 0;
                      que.push( {X, Y} );
                    }
                    break;
                }
            }
        }
        if (!flag)  cout << "#" << t << " 없음?" << endl;
  }
  return 0;
}
