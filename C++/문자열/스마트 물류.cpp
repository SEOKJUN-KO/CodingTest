#include<iostream>

using namespace std;

int main(int argc, char** argv) {
    int N, K;
    cin >> N >> K;
    string line;
    cin >> line;
    int ans = 0;
    for (int i = 0; i < line.size(); i++) { // 2*10^4
        if ( line[i] == 'H' || line[i] == 'N') { continue; }
        int start = i - K;
        if (start < 0) { start = 0; }
        bool flag = false;
        for (int j = start; j < i; j++) {
            if (line[j] == 'H') {
                line[j] = 'N'; ans += 1; flag = true;
                break;
            }
        }
        if (flag) { continue; }
        int end = i + K + 1;
        if ( end > line.size() ) { end = line.size(); }
        for (int j = i+1; j < end; j++) {
            if (line[j] == 'H') {
                line[j] = 'N'; ans += 1;
                break;
            }
        }
    }
    cout << ans;
    return 0;
}
