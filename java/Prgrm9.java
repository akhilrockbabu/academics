import java.util.Scanner;

class Prgrm9
{
	static void area(float a)
	{
		System.out.println("area of Circle = "+3.14*a*a);
	}

	static void area(int b)
	{
		System.out.println("area of Square = "+b*b);
	}

	static void area(int b,int c)
	{
		System.out.println("area of Rectangle = "+b*c);
	}
	
	public static void main(String arg[])
	{
		int b,c;
		float a;
		Scanner s=new Scanner(System.in);
		while(true)
		{
			System.out.println("1.Circle\n2.Square\n3.Rectangle\n4.Exit\nEnter your choice : ");
			c=s.nextInt();
			switch(c)
			{
				case 1:
					System.out.println(" enter the radius");
					a=s.nextFloat();
					area(a);
					break;
				case 2:
					System.out.println(" enter the side");
					b=s.nextInt();
					area(b);
					break;
				case 3:
					System.out.println(" enter the length");
					b=s.nextInt();
					System.out.println(" enter the breadth");
					c=s.nextInt();
					area(b,c);
					break;
				case 4:
					return;
				default:
					System.out.println(" Invalid choice");
			}
		}
	}
}
