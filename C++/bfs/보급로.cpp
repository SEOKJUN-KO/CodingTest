#include<iostream>
#include<algorithm>
#include<queue>
#include<string>
using namespace std;
#define X first
#define Y second
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
string board[101];
int dist[101][101];
int main(int argc, char** argv) {
    int test_case, T;
    cin>>T;
    for(test_case = 1; test_case <= T; ++test_case) {
        int N;
        string str;
        cin >> N;
        cin.ignore();
        for( int i = 0; i < N; i++ ) cin >> board[i];
        for( int i = 0; i < N; i++ ) fill( dist[i], dist[i]+N, 9999 );
        queue<pair<int, int>> que;
        que.push({0, 0});
        dist[0][0] = 0;
        while(!que.empty( )) {
            auto cur = que.front(); que.pop();
            for (int i = 0; i < 4 ; i++) {
                int X = cur.X + dx[i];
                int Y = cur.Y + dy[i];
                if ( X >= N || X < 0 || Y >= N || Y < 0 ) continue;
                int b = board[Y][X] - '0';
                if ( dist[Y][X] > b + dist[cur.Y][cur.X] ) {
                    dist[Y][X] =  b + dist[cur.Y][cur.X];
                    que.push({X, Y});
                }
            }
        }
        cout << "#" << test_case << " " << dist[N-1][N-1] << endl;
    }
    return 0;
}
