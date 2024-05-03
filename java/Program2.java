/*Define a class ‘product’ with data members pcode, pname and price. 
Create three objects of the class and find the product having the lowestprice.*/


import java.util.Scanner;
class Program2
{
	public static void main(String arg[])
	{
		Product p1=new Product();
		Product p2=new Product();
		Product p3=new Product();
		float p1price=p1.accept();
		float p2price=p2.accept();
		float p3price=p3.accept();
		System.out.println("The Product with lowest price is : ");
		if(p1price<p2price && p1price<p3price )
		{
			p1.display();
		}
		else if(p2price<p3price)
		{
			p2.display();
		}
		else
		{
			p3.display();
		}
	}
}

class Product
{
	int pcode;
	String pname;
	float pprice;
	
	float accept()
	{
		Scanner s=new Scanner(System.in);
		System.out.println("enter name");
		pname=s.nextLine();
		System.out.println("enter code");
		pcode=s.nextInt();
		System.out.println("enter price");
		pprice=s.nextFloat();
		return pprice;
		
	}
	
	void display()
	{
		System.out.println("Product Code = "+pcode);
		System.out.println("Product Name = "+pname);
		System.out.println("Product price = "+pprice);
	}
}
