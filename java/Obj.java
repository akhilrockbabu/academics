import java.util.Scanner;
class Cons
{
	int x=10;
	String y="rockiey";
	Cons(int a)
	{
		x=a;
	}
	Cons(int a,String b)
	{
		x=a;
		y=b;
	}
	void display()
	{
		System.out.println(x);
		System.out.println(y);
	}
}

class Obj
{
	public static void main(String a[])
	{
		Cons c=new Cons(26,"akhilrockbabu");
		Cons c1=new Cons(15);
		c.display();
		c1.display();
	}
}
