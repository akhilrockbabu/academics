import java.util.Scanner;
class Prgrm3
{
	public static void main(String[] a)
	{
		Complex re=new Complex(2.3,3.3);
		Complex im=new Complex(1.5,3.4);
		Complex temp;
		temp=Complex.add(re,im);
		re.display();
		im.display();
		temp.display();
	}
}

class Complex
{
	double a;
	double b;
	Complex(double x,double y)
	{
		a=x;
		b=y;
	}
	static Complex add(Complex ob1,Complex ob2)
	{
		Complex c=new Complex(0,0);
		c.a=ob1.a+ob2.a;
		c.b=ob1.b+ob2.b;
		return c;
	}
	void display()
	{
		System.out.println(+a+"+"+b+"i");
	}
}
