import java.util.Set;
import java.util.HashSet;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader( new InputStreamReader( System.in ) );
        String inp[] = br.readLine().split(" ");

        Set<String> set = new HashSet<>();
        for( int i=0; i < inp[0].length(); i++ ) {
            String tmp = inp[0].charAt(i)+"";
            set.add(tmp);
            for( int j = i + 1; j < inp[0].length(); j++ ) {
                tmp += inp[0].charAt(j);
                set.add(tmp);
            }
        }
        System.out.print( set.size() );
    }
}
