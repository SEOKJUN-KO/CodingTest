import java.io.*;
import java.util.*;

class Box {
    Box front, back;
    int number;
    Box(int number) {
        this.front = null;
        this.back = null;
        this.number = number;
    }

    public void connect(Box frontBox) {
        this.front = frontBox;
        frontBox.back = this;
    }

    public void disconnect() {
        if ( this.front != null ) {
            this.front.back = null;
            this.front = null;
        }
        if ( this.back != null ) {
            this.back.front = null;
            this.back = null;
        }

    }

    public int getInfo() {
        int a = -1, b = -1;
        if (this.front != null) { a = this.front.number; }
        if (this.back != null) { b = this.back.number; }
        return a+2*b;
    }
}

class Belt {
    Deque<Box> que;

    Belt() { this.que = new ArrayDeque<>(); }

    public void add(Box boxN) {
        if (que.size() >= 1) {
            Box back = this.que.getFirst();
            back.connect(boxN);
        }
        this.que.addFirst(boxN);
    }

    public Box removeFront() {
        if ( this.que.size() <= 0 ) { return null; }
        Box firstBox = this.que.removeFirst();
        firstBox.disconnect();
        return firstBox;
    }

    public Box removeBack() {
        if ( this.que.size() <= 0 ) { return null; }
        Box lastBox = this.que.removeLast();
        lastBox.disconnect();
        return lastBox;
    }

    public int getFloor() { return this.que.size()/2; }
    public int getNumberOfBox() { return this.que.size(); }

    public int getInfo() {
        int a = -1, b = -1, c = this.que.size();
        if (this.que.size() > 0) {
            a = this.que.getFirst().number;
            b = this.que.getLast().number;
        }
        return a + 2*b + 3*c;
    }
}

public class Main {
    public static void buildFactory(String inp[], ArrayList<Belt> list, HashMap<Integer, Box> map) {
        int n = Integer.parseInt(inp[1]);
        int m = Integer.parseInt(inp[2]);
        for ( int i = 0; i <= n; i++ ) { list.add( new Belt() ); }
        for ( int i = inp.length-1; i >= 3; i-- ) {
            int idx = Integer.parseInt(inp[i]);
            Box box = new Box(i-2);
            map.put(i-2, box);
            list.get(idx).add(box);
        }
    }

    public static void moveAll(int src, int dst, ArrayList<Belt> list, HashMap<Integer, Box> map) {
        Belt srcB = list.get(src), dstB = list.get(dst);
        while(true) {
            Box returnBox = srcB.removeBack();
            if ( returnBox == null ) { break; }
            dstB.add(returnBox);
        }
        System.out.println(dstB.getNumberOfBox());
    }

    public static void changeFront(int src, int dst, ArrayList<Belt> list, HashMap<Integer, Box> map) {
        Belt srcB = list.get(src), dstB = list.get(dst);
        Box srcBox = srcB.removeFront(), dstBox = dstB.removeFront();
        if ( srcBox != null ) { dstB.add(srcBox); }
        if ( dstBox != null ) { srcB.add(dstBox); }
        System.out.println(dstB.getNumberOfBox());
    }

    public static void divideBox(int src, int dst, ArrayList<Belt> list, HashMap<Integer, Box> map) {
        Belt srcB = list.get(src), dstB = list.get(dst);
        int iter = srcB.getFloor();
        if (iter == 0) {
            System.out.println(dstB.getNumberOfBox());
            return;
        }
        ArrayList<Box> tmp = new ArrayList<>();
        for ( int i = 1; i <= iter; i++ ) { tmp.add(srcB.removeFront()); }
        for ( int i = 1; i <= iter; i++ ) {
            Box box = tmp.remove(tmp.size()-1);
            dstB.add(box);
        }
        System.out.println(dstB.getNumberOfBox());
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader( new InputStreamReader( System.in ) );
        BufferedWriter bw = new BufferedWriter( new OutputStreamWriter( System.out ) );
        ArrayList<Belt> beltList = new ArrayList<>();
        HashMap<Integer, Box> map = new HashMap<>();

        int Q = Integer.parseInt(br.readLine());
        for( int q = 1; q <=Q ; q++ ) { // 10^5
            String inp[] = br.readLine().split(" ");
            if (inp[0].equals("100")) { // 1
                buildFactory(inp, beltList, map);
            }
            else if (inp[0].equals("200")) { //
                int src = Integer.parseInt(inp[1]), dst = Integer.parseInt(inp[2]);
                moveAll(src, dst, beltList, map);
            }
            else if (inp[0].equals("300")) {
                int src = Integer.parseInt(inp[1]), dst = Integer.parseInt(inp[2]);
                changeFront(src, dst, beltList, map);
            }
            else if (inp[0].equals("400")) {
                int src = Integer.parseInt(inp[1]), dst = Integer.parseInt(inp[2]);
                divideBox(src, dst, beltList, map);
            }
            else if (inp[0].equals("500")) {
                int num = Integer.parseInt(inp[1]);
                Box box = map.get(num);
                System.out.println( box.getInfo() );
            }
            else if (inp[0].equals("600")) {
                int num = Integer.parseInt(inp[1]);
                Belt belt = beltList.get(num);
                System.out.println( belt.getInfo() );
            }
        }
    }
}