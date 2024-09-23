import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader( new InputStreamReader( System.in ) );
        String inp[] = br.readLine().split(" ");
        int T = Integer.parseInt(inp[0]);
        for( int t = 0; t < T; t++ ) {
            inp = br.readLine().split(" ");
            int N = Integer.parseInt(inp[0]);
            HashMap<String, ArrayList<String>> map = new HashMap<>();
            for( int i = 0; i < N; i ++ ) {
                inp = br.readLine().split(" ");
                String name = inp[0], category = inp[1];
                if ( !map.containsKey(category) ) { map.put(category, new ArrayList<>()); }
                map.get(category).add(name);
            }
            int ans = 1;
            for (String key: map.keySet()) { ans *= (map.get(key).size()+1); }
            System.out.println(ans-1);
        }
    }
}