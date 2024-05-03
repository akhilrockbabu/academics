import java.util.Scanner;
class Person
{
	String name,gender,address;
	int age;
	
	
	Person(String n,String g,String ad,int ag)
	{
		name=n;
		gender=g;
		address=ad;
		age=ag;
	}
}


class Employee extends Person
{
	int eid;
	String cname,qual;
	float salary;
	
	
	Employee(String n,String g,String ad,int ag,int e,String c,String q,float sa)
	{
		super(n,g,ad,ag);
		eid=e;
		cname=c;
		qual=q;
		salary=sa;
	}
}



class Teacher extends Employee
{
	String sub,dept;
	int tid;
	
	
	Teacher(String n,String g,String ad,int ag,int e,String c,String q,float sa,String su,String d,int t)
	{
		super(n,g,ad,ag,e,c,q,sa);
		sub=su;
		dept=d;
		tid=t;
	}
	
	
	void display()
	{
		System.out.println("Name : "+name);
		System.out.println("Gender : "+gender);
		System.out.println("Address : "+address);
		System.out.println("Age : "+age);
		System.out.println("Employee ID : "+eid);
		System.out.println("Company Name : "+cname);
		System.out.println("Qualification : "+qual);
		System.out.println("Salary : "+salary);
		System.out.println("Teacher ID : "+tid);
		System.out.println("Subject : "+sub);
		System.out.println("Department : "+dept);	
	}
}


class Prgrm10
{
	
	
	public static void main(String arg[])
	{
		int n;
		Scanner s1=new Scanner(System.in);
		Scanner s2=new Scanner(System.in);
		System.out.println("Enter the no: of Teachers");
		n=s1.nextInt();
		Teacher t[]=new Teacher[n];
		for(int i=0;i<n;++i)
		{
			System.out.println("Enter the details of Teacher "+(i+1));
			System.out.println("Name : ");
			String name=s2.nextLine();
			System.out.println("Gender : ");
			String gender=s2.nextLine();
			System.out.println("Address : ");
			String address=s2.nextLine();
			System.out.println("Age : ");
			int age=s1.nextInt();
			System.out.println("Employee ID : ");
			int eid=s1.nextInt();
			System.out.println("Company Name : ");
			String cname=s2.nextLine();
			System.out.println("Qualification : ");
			String qual=s2.nextLine();
			System.out.println("Salary : ");
			float salary=s1.nextFloat();
			System.out.println("Teacher ID : ");
			int tid=s1.nextInt();
			System.out.println("Subject : ");
			String sub=s2.nextLine();
			System.out.println("Department : ");
			String dept=s2.nextLine();
			t[i]=new Teacher(name,gender,address,age,eid,cname,qual,salary,sub,dept,tid);
		}
		
		System.out.println("Entered Teacher Details are : ");
		for(int i=0;i<n;++i)
		{
			System.out.println("Details of Teacher "+(i+1));
			t[i].display();
		}
		
	}
}

