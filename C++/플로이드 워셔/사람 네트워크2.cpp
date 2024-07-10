#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 99999;

int main(int argc, char** argv) {
    int T;
    cin >> T;
    for (int test_case = 1; test_case <= T; test_case++) {
        int N;
        cin >> N;
        
        // 동적 배열 할당
        vector<vector<int>> graph(N + 1, vector<int>(N + 1, INF));
        
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                int tmp;
                cin >> tmp;
                if (tmp == 0 && i != j) {
                    graph[i][j] = INF;
                } else {
                    graph[i][j] = tmp;
                }
            }
        }
        
        for (int k = 1; k <= N; k++) {
            for (int i = 1; i <= N; i++) {
                if (i == k) continue;
                for (int j = 1; j <= N; j++) {
                    if (i == j || k == j) continue;
                    if (graph[i][k] != INF && graph[k][j] != INF && graph[i][j] > graph[i][k] + graph[k][j]) {
                        graph[i][j] = graph[i][k] + graph[k][j];
                    }
                }
            }
        }
        
        int answer = INF;
        for (int i = 1; i <= N; i++) {
            int cnt = 0;
            for (int j = 1; j <= N; j++) {
                if (i != j) {
                    cnt += graph[i][j];
                }
            }
            if (answer > cnt) {
                answer = cnt;
            }
        }
        
        cout << "#" << test_case << " " << answer << endl;
    }
    return 0;
}
