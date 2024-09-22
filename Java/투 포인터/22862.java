import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Main {
    static BufferedReader br = new BufferedReader( new InputStreamReader(System.in) );
    static BufferedWriter bw = new BufferedWriter( new OutputStreamWriter(System.out));
    public static void main(String[] args) throws Exception {
        String inp[] = br.readLine().split(" ");
        int N = Integer.parseInt(inp[0]), K = Integer.parseInt(inp[1]);
        inp = br.readLine().split(" ");

        ArrayList<Integer> list = new ArrayList<>();
        for(int i=0; i < inp.length; i++) { list.add(Integer.parseInt(inp[i])); }
        int left = 0, right = 0;
        int odd = 0, even = 0;

        if ( list.get(0)%2 == 0 ) { even += 1;}
        else { odd += 1; }

        int ans = 0;
        while( left <= right && right <= N ) {
            if ( odd <= K ) {
                int l = (right-left+1) - odd;
                if (ans < l) { ans = l; }
            }
            if ( right == N-1 && left < N-1 ) {
                if ( list.get(left)%2 == 0 ) { even -= 1; }
                else { odd -= 1; }
                left += 1;
            }
            else if ( left == N-1 && right == N-1 ) { break; }
            else if ( left == right ) {
                right += 1;
                if ( list.get(right)%2 == 0 ) { even += 1; }
                else { odd += 1; }
            }
            else if ( odd <= K ) {
                right += 1;
                if ( list.get(right)%2 == 0 ) { even += 1; }
                else { odd += 1; }
            }
            else {
                if ( list.get(left)%2 == 0 ) { even -= 1; }
                else { odd -= 1; }
                left += 1;
            }
        }
        System.out.println(ans);
    }
}
