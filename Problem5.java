/*
2520 is the smallest number that can be divided by each of the numbers from 
1 to 10 without any remainder.

What is the smallest positive number that 
is evenly divisible by all of the numbers from 1 to 20?
*/

public class Problem5  {
	public static void main(String[] args) {

		int base = 2520;
		int cur = 1;
		while(cur < 21)  {
			if(base%cur == 0)  {
				cur++;
			}
			else  {
				cur=1;
				base++;
			}
		}
		System.out.println("The smallest: " + base);
	}

}