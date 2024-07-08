#include<iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
using namespace std;
 
int arr[1000];
int main(int argc, char** argv) {
    int test_case, T;
    cin>>T;
    for(test_case = 1; test_case <= T; ++test_case) {
        int p;
        int ans;
        cin>>p;
        for( int i = 0; i < p; ++i ) {
            cin>>arr[i];
        }
        if ( p == 1) ans = arr[0]*arr[0];
        else {
            sort(arr, arr+p);
            ans = arr[0]*arr[p-1];
        }
        cout << "#" << test_case << " " << ans << endl;
    }
    return 0;
}
