import java.util.*;

class Main{
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		
		String answer = "";
		for(char x: str.toCharArray()) {
			if(x>=65 && x<=90) 
				answer+=(char)(x+32);
			else
				answer+=(char)(x-32);
		}
		System.out.println(answer);
	}
}