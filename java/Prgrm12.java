/*Create an interface having prototypes of functions area() and perimeter().
 Create two class Circle and Rectangle which implements the above interface.
  Create a menu driven program to find area and perimeter of objects.*/

import java.util.Scanner;
interface area_perimeter
{
	void area();
	void peri();
}

class Circle implements area_perimeter
{
	int r;
	Scanner s=new Scanner(System.in);
	public void area()
	{
		System.out.println("enter the radius");
		r=s.nextInt();
		System.out.println("the area of circle = "+3.14*r*r);
	}
	public void peri()
	{
		System.out.println("enter the radius");
		r=s.nextInt();
		System.out.println("the perimeter of circle = "+2*3.14*r);
	}
}

class Rectangle implements area_perimeter
{
	int l;
	int b;
	Scanner s=new Scanner(System.in);
	public void area()
	{
		System.out.println("enter the length");
		l=s.nextInt();
		System.out.println("enter the breadth");
		b=s.nextInt();
		System.out.println("the area of rectangle = "+l*b);
	}
	public void peri()
	{
		System.out.println("enter the length");
		l=s.nextInt();
		System.out.println("enter the breadth");
		b=s.nextInt();
		System.out.println("the perimeter of rectangle = "+2*(l+b));
	}
}

class Prgrm12
{
		static int c1,c2;
		public static void main(String arg[])
		{
			Rectangle r=new Rectangle();
			Circle c=new Circle();
			Scanner s=new Scanner(System.in);
			while(true)
			{
				System.out.println(" 1.Circle \n 2.Rectangle \n 3.Exit \n Enter your choice");
				c1=s.nextInt();
				switch(c1)
				{
					case 1:
						System.out.println(" 1.Area \n 2.Perimeter \n Enter your choice");
						c2=s.nextInt();
						switch(c2)
						{
							case 1:
								c.area();
								break;
							case 2:
								c.peri();
								break;
							default:
								System.out.println(" Invalid choice");
						}
						break;
					case 2:
						System.out.println(" 1.Area \n 2.Perimeter \nEnter your choice");
						c2=s.nextInt();
						switch(c2)
						{
							case 1:
								r.area();
								break;
							case 2:
								r.peri();
								break;
							default:
								System.out.println(" Invalid choice");
						}
					case 3:
						return;
					default:
						System.out.println(" Invalid choice");
				}
			}
	}
}
