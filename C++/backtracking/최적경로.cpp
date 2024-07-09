#include<iostream>
#include<algorithm>
using namespace std;
#define X first
#define Y second
pair<int, int> office, house, last;
int length, N, ans;
void backTracking( bool visit[], pair<int, int> points[] , int deep ) {
    if ( deep == N ){
        length += abs(house.X - last.X) + abs(house.Y - last.Y);
        if ( ans > length ) ans = length;
        length -= abs(house.X - last.X) + abs(house.Y - last.Y);
        return ;
    }
    for( int i = 0; i < N; i++ ) {
        if (!visit[i]) {
            pair<int, int> tmp;
            length += abs(last.X - points[i].X) + abs(last.Y - points[i].Y);
            tmp = last;
            last = points[i];
            visit[i] = true;
            backTracking(visit, points, deep + 1);
            visit[i] = false;
            last = tmp;
            length -= abs(last.X - points[i].X) + abs(last.Y - points[i].Y);
        }
    }
    return ;
}

int main(int argc, char** argv)
{
  int T;
  cin>>T;
  for( int test_case = 1; test_case <= T; ++test_case)
  {
        cin >> N;
        pair<int, int> points[N];
        for( int i = 0; i < 2; i++) {
          int x, y;
            cin >> x;
            cin >> y;
      if( i == 0 ) office = {x, y};
            else house = {x, y};
        }
        for( int i = 0; i < N; i++) {
          int x, y;
            cin >> x;
            cin >> y;
            points[i] = {x, y};
        }
        length = 0; ans = 99999999;
        bool visit[N];
        fill_n(visit,N,false);
        last = office;
        backTracking(visit, points, 0);
        cout << "#" << test_case << " " << ans << endl;
  }
  return 0;
}
