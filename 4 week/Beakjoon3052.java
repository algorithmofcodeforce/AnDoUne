import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int count = 1;
        int[] r = new int[10];
        for(int i=0;i<10;i++) {
            int num = scan.nextInt();
            r[i] = num%42;
        }
        Arrays.sort(r);
        for(int i=0; i<9; i++) {
            if(r[i]!=r[i+1]) {
                count++;
            }
        }
        
        System.out.println(count);
    }
}
