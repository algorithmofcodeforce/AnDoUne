import java.util.*;
public class B2609 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int a,b;
		int gcd=0, lcm=0;
		a = sc.nextInt();
		b = sc.nextInt();
		if (a<b) {
			for (int i = 1; i<a+1; i++) {
				if ((a%i==0) && (b%i==0)){
					gcd = i;
				}
			}
		}
		else {
			for (int i = 1; i<b+1; i++) {
				if ((a%i==0) && (b%i==0)) {
					gcd = i;
				}
			}
		}
		lcm = (a*b)/gcd;
		System.out.println(gcd);
		System.out.println(lcm);
	}
}
