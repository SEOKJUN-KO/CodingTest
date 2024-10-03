#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

bool compare(string a, string b) { return a < b; }

int L = 0, C = 0;
int ja = 0, mo = 0;
deque<bool> used = {};
void backtracking(deque<string> &arr, int idx, deque<string> &ans) {
    if (ans.size() == L ) {
        if ( ja >= 2 && mo >= 1) {
            for (int i = 0; i < L; i++) { cout << ans[i]; }
            cout << endl;
        }
        return ;
    }
    for (int i = idx; i < C; i++) {
        if (!used[i]) {
            used[i] = true;
            if ( arr[i] == "a" || arr[i] == "e" || arr[i] == "i" || arr[i] == "o" || arr[i] == "u") { mo += 1; }
            else { ja += 1; }
            ans.push_back(arr[i]);
            backtracking(arr, i+1, ans);
            if ( arr[i] == "a" || arr[i] == "e" || arr[i] == "i" || arr[i] == "o" || arr[i] == "u") { mo -= 1; }
            else { ja -= 1; }
            ans.pop_back();
            used[i] = false;
        }
    }
}

int main() {
    cin >> L >> C;
    deque<string> arr;
    for (int i = 0; i < C; i++) {
        string tmp; cin >> tmp;
        arr.push_back(tmp);
        used.push_back(false);
    }
    sort(arr.begin(), arr.end(), compare);
    deque<string> ans;
    backtracking(arr, 0, ans);
    return 0;
}
