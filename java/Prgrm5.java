/*Create a class CPU with attribute price. Create an inner class Processor (no. of cores, manufacturer) and a static nested class RAM (memory,
manufacturer). Create an object of CPU and print information of Processor and RAM.*/

import java.util.Scanner;
class Cpu
{
	float price;
	
	Cpu(float p)
	{
		price=p;
	}
	
	class Processor
	{
		int cores;
		String manu;
		Processor(int c,String ma)
		{
			cores=c;
			manu=ma;
		}
		void show()
		{
			System.out.println("No of Cores = "+cores);
			System.out.println("Manufacturer = "+manu);
		}
	}
	
	static class Ram
	{
		int memory;
		String manu;
		Ram(int m,String ma)
		{
			memory=m;
			manu=ma;
		}
		void show()
		{
			System.out.println("Memory = "+memory+"GB");
			System.out.println("Manufacturer = "+manu);
		}
	}
	
	void show()
	{
		System.out.println("price : "+price);

	}
}

class Prgrm5
{
	public static void main(String a[])
	{
		Cpu c=new Cpu(1500);
		Cpu.Processor p=c.new Processor(8,"Amd Ryzen");
		Cpu.Ram r=new Cpu.Ram(16,"gigabyte");
		c.show();
		p.show();
		r.show();
	}
}

