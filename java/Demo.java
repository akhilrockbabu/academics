import java.util.*;
class Demo
{
	int tamount=0;
	void bank()
	{
		int amount;
		Scanner scan=new Scanner(System.in);
		System.out.println("enter the  amount to deposit");
		amount=scan.nextInt();
		this.tamount=this.tamount+amount;
		System.out.println("new balance="+this.tamount);
	}
	public static void main(String a[])
	{
		String name=a[0];
		System.out.println("Welcome to Reserve Bank of India");
		System.out.println("hello "+a[0]);
		Demo d1=new Demo();
		d1.bank();
		d1.bank();
		
	}
	
}
