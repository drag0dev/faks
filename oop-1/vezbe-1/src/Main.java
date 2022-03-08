import java.util.*;

public class Main {
	public static void main(String args[]) {
		//zad1();
		//zad2();
		//zad3();
		//zad4();
		//zad5();
		//zad6();
		//zad7();
		zad8();
	}

	public static void zad1() {
		System.out.println("A");
		System.out.println("B");
		System.out.println("\tB.1");
		System.out.println("\t\tB.1.1");
		System.out.println("\tB.2");
		System.out.println("C");
		
	}
	
	public static void zad2() {
		double povrsina = 16;
		int osnovica = 4;
		int krak = 6;
		System.out.printf("Osnovica kvadrata: %.2f\n", Math.sqrt(povrsina));
		double visinaTrougla = Math.sqrt(krak*krak - (osnovica * osnovica) / 4);
		System.out.printf("Povrsina trougla je: %.2f\n", (osnovica * visinaTrougla)/2);
	}
	
	public static void zad3() {
		Scanner sc = new Scanner(System.in);
		while (true){
			System.out.print("Uneiste godinu izmedju 1538 i 10000: ");
			int godina = sc.nextInt();
			if (godina <= 1538 || godina >= 10000) {
				System.out.println("Godina mora biti u opsegu 1538-10000!");
				continue;
			}
			if (godina % 400 == 0 || (godina%100!=0 && godina%4==0)) {
				System.out.printf("Godina %d. je prestupna!\n", godina);
			}else {
				System.out.printf("Godina %d. nije presutpna!\n", godina);
			}
			
			break;
		}
		sc.close();
	}
	
	public static void zad4() {
		Scanner sc = new Scanner(System.in);
		System.out.print("Unesite rastojanje u centimetrima: ");
		double cm = sc.nextDouble();
		System.out.printf("%.2f centimetara je %.2fdm i %.5fm \n", cm, cm/10, cm/100);
		sc.close();
	}
	
	public static void zad5() {
		int a = 3, b = 4, c = 5;
		double povrsina = 2 * (a*b + b*c + c*a);
		System.out.printf("Povrsina kvadra dimenzija %d, %d, %d je: %f\n", a, b, c, povrsina);
	}
	
	public static void zad6() {
		int R = 6;
		int r = 3;
		int h = 4;
		double s = Math.sqrt(r*r + h*h);
		System.out.printf("Povrsina kupe precnika %d i visine %d je: %.2f Pi\n", R, h, (r*s) + (r*r));
	}
	
	public static void zad7() {
		int x, y, z;
		Scanner sc = new Scanner(System.in);
		System.out.print("Unesite vrednost x: ");
		x = sc.nextInt();
		System.out.print("Unesite vrednost y: ");
		y = sc.nextInt();
		
		if (x<y) {
			z = Math.max(x, y) / (1 + Math.abs(Math.min(x, y)));
		}else {
			z = Math.max(x, y) / (1 + Math.min(x, y));
		}
		
		System.out.printf("Vrednost z za x:%d i y:%d je: %d\n", x, y, z);
		
		sc.close();
	}
	
	public static void zad8() {
		int a,b,c;
		Scanner sc = new Scanner(System.in);
		System.out.print("Unesite a: ");
		a = sc.nextInt();
		System.out.print("Unesite b: ");
		b = sc.nextInt();
		System.out.print("Unesite c: ");
		c = sc.nextInt();
		sc.close();
		
		double determinanta = Math.sqrt(b*b - 4 * a * c ); 
		if (Double.isNaN(determinanta)) {
			System.out.println("Jednacina sa zadatim parametrima nema realnih resenja!");
			return;
		}
		// diskutuje ??

		double resenjeJedan, resenjeDva;
		resenjeJedan = (-b + determinanta)/ 2*a;
		resenjeDva = (-b - determinanta) / 2*a;
		
		System.out.printf("Prov resenje: %f, Drugo resenje: %f\n", resenjeJedan, resenjeDva);
		
	}
}
