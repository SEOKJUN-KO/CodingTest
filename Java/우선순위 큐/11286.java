import java.util.*;
import java.io.*;

class Data implements Comparable<Data> {
    int first, second;

    Data(int f, int s) {
        this.first = f;
        this.second = s;
    }

    public int compareTo(Data d) {
        if(this.first < d.first) { return -1; }
        else if (this.first == d.first && this.second < d.second) { return -1; }
        return 1;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader( new InputStreamReader(System.in));
        String inp = br.readLine();
        int N = Integer.parseInt(inp);
        PriorityQueue<Data> pq = new PriorityQueue<>();
        for( int i = 0; i < N; i++ ) {
            inp = br.readLine();
            int number = Integer.parseInt(inp);
            if (number == 0) {
                if ( pq.size() == 0 ) { System.out.println(0); }
                else {
                    Data tmp = pq.poll();
                    System.out.println(tmp.second);
                }
            }
            else { pq.add( new Data( Math.abs(number), number) ); }
        }
    }
}