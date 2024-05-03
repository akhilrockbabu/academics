import java.util.Scanner;
class Neg extends Exception
{
	Neg(String msg)
	{
		super(msg);
	}
}
class Prgrm15
{
	public static void main(String arg[])
	{
		int n,a;
		int avg=0;
		Scanner s=new Scanner(System.in);
		System.out.println("enter the number elements to array");
		n=s.nextInt();
		System.out.println("enter the numbers in array");
		for(int i=0;i<n;++i)
		{
			a=s.nextInt();
			try
			{
				if(a<0)
				{
					--i;
					throw new Neg("the number is negative please re-enter it!");
				}
				else
				{
					avg=avg+a;
				}
			}
			catch(Neg e)
			{
				System.out.println(e);
			}
		}
		System.out.println("Average of integers= "+avg/n);
	}
}
