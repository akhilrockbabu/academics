class A
{
	int x=10;
	void show()
	{
		System.out.println("class A show -> value :"+x);
	}
}

class B extends A
{
	int x=20;
	int y=50;
	void show()
	{
		System.out.println("class B show -> value :"+x);
	}
	void display()
	{
		super.show();
		System.out.println("class B display -> value:"+y);
	}
}

class Inheritdemo
{
	public static void main(String a[])
	{
		B b=new B();
		b.show();
		b.display();
	}
	
}
