import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {
    static String answer = "";
    static int mo = 0, ja = 0;
    static boolean[] used;
    static BufferedWriter bw;

    public static void backTracking(String[] str, int idx, int length) throws Exception {
        if (answer.length() == length) {
            if (mo >= 1 && ja >= 2) { // 최소 모음 1개, 자음 2개 조건
                bw.write(answer + "\n");
                bw.flush();
            }
            return;
        }

        for (int i = idx; i < str.length; i++) {
            if (!used[i]) {
                used[i] = true;

                if (str[i].equals("a") || str[i].equals("e") || str[i].equals("i") || str[i].equals("o") || str[i].equals("u")) {
                    mo++;
                } else {
                    ja++;
                }

                answer += str[i]; // 선택한 문자 추가
                backTracking(str, i + 1, length); // 다음 문자 선택
                answer = answer.substring(0, answer.length() - 1); // 마지막 문자 제거

                if (str[i].equals("a") || str[i].equals("e") || str[i].equals("i") || str[i].equals("o") || str[i].equals("u")) {
                    mo--;
                } else {
                    ja--;
                }

                used[i] = false;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            String inp[] = br.readLine().split(" ");
            int L = Integer.parseInt(inp[0]), C = Integer.parseInt(inp[1]);
            String str[] = br.readLine().split(" ");

            Arrays.sort(str); // 문자열 정렬
            used = new boolean[C]; // 사용된 문자 체크 배열 생성

            // 백트래킹 함수 호출 (길이 L, 시작 인덱스 0)
            backTracking(str, 0, L);
        } finally {
            br.close();
            bw.close(); // BufferedWriter 닫기
        }
    }
}