import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader( new InputStreamReader( System.in ) );
        String inp[] = br.readLine().split(" ");
        int N = Integer.parseInt(inp[0]);
        inp = br.readLine().split(" ");
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < inp.length; i++) { list.add( Integer.parseInt(inp[i])); }

        int idx = 0;
        int l = Math.abs(list.get(0)+list.get(1)), store = list.get(0)+list.get(1);
        while( idx < N ) {
            int target = -list.get(idx);
            int left = idx, right = list.size()-1;
            if ( (left >= N) || (left == right) ) { break; }
            int mid = (left+right)/2;
            while(left <= right) {
                mid = (left+right)/2;
                if (list.get(mid) == target) { break; }
                else if ( list.get(mid) > target ) { right = mid - 1; }
                else { left = mid + 1; }
            }
            int tmp[] = { mid-1, mid, mid+1 };
            for(int i: tmp) {
                if ( !( 0 <= i && i < N ) || ( idx == i ) ) { continue; }
                int tmpN = Math.abs( list.get(i) + list.get(idx) );
                if ( l > tmpN ) { l = tmpN; store = list.get(i) + list.get(idx); }
            }
            idx += 1;
        }
        System.out.print(store);
    }
}