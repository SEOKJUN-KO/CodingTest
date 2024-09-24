import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void bfs(ArrayList<ArrayList<String>> board, int y, int x, int N, ArrayList<String> target) {
        int dx[] = {0, 0, -1, 1}, dy[] = {-1, 1, 0, 0};

        Queue<ArrayList<Integer>> que = new LinkedList<>();
        que.add(new ArrayList<>(List.of(y, x)));
        board.get(y).set(x, "V");

        while (!que.isEmpty()) {
            ArrayList<Integer> tmp = que.poll();
            int ny = tmp.get(0), nx = tmp.get(1);
            for (int i = 0; i < 4; i++) {
                int Y = ny + dy[i], X = nx + dx[i];
                if (0 <= Y && Y < N && 0 <= X && X < N) {
                    if ( target.contains(board.get(Y).get(X)) ) {
                        board.get(Y).set(X, "V");
                        que.add(new ArrayList<>(List.of(Y, X)));
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inp[] = br.readLine().split(" ");
        int N = Integer.parseInt(inp[0]);
        ArrayList<ArrayList<String>> board = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            inp = br.readLine().split("");
            ArrayList<String> tmp = new ArrayList<>();
            for (String st : inp) {
                tmp.add(st);
            }
            board.add(tmp);
        }

        for (int i = 1; i <= 2; i++) {
            ArrayList<ArrayList<String>> copyB = new ArrayList<>();
            for (ArrayList<String> row : board) {
                copyB.add(new ArrayList<>(row));  // ArrayList 복사
            }
            int count = 0;
            for (int y = 0; y < N; y++) {
                for (int x = 0; x < N; x++) {
                    if (!copyB.get(y).get(x).equals("V")) {
                        if (i == 1) {
                            bfs( copyB, y, x, N, new ArrayList<>(List.of(copyB.get(y).get(x))) );
                        }
                        else {
                            if ( copyB.get(y).get(x).equals("B") ) {
                                bfs(copyB, y, x, N, new ArrayList<>(List.of("B")));
                            }
                            else {
                                bfs(copyB, y, x, N, new ArrayList<>(List.of("R", "G")));
                            }
                        }
                        count += 1;
                    }
                }
            }
            System.out.print(count + " ");
        }
    }
}