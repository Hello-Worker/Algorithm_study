import java.util.*;
class Main{
	public int solution(String str, char c) {
		int answer=0;
		str=str.toUpperCase();
		c=Character.toUpperCase(c);
		for(int i=0; i<str.length(); i++) {
			if(str.charAt(i)==c) 
				answer++;
		}
		return answer;
		
	}
	public static void main(String[] args) {
		Main T = new Main();
		Scanner sc = new Scanner(System.in);//System.in byte로 읽는다.
		String str=sc.next();//공백을 입력하기 전까지 값을 입력받는다.
		char c=sc.next().charAt(0);
		System.out.println(T.solution(str, c));
		
	}
}