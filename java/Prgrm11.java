import java.util.Scanner;
class Student
{
	String name;
	float academic_score;
	Student(String n,float a_s)
	{
		name=n;
		academic_score=a_s;
	}
}

class Sports extends Student
{
	String sports_name;
	float sports_score;
	Sports(String n,float a_s,String s_n,float s_s)
	{
		super(n,a_s);
		sports_name=s_n;
		sports_score=s_s;
	}
}

class Result extends Sports
{
	Result(String n,float a_s,String s_n,float s_s)
	{
		super(n,a_s,s_n,s_s);
	}

	void display()
	{
		System.out.println("student name = "+name);
		System.out.println("student score = "+academic_score);
		System.out.println("sports name = "+sports_name);
		System.out.println("sports score = "+sports_score);
	}
}

class Prgrm11
{
	public static void main(String arg[])
	{
		Scanner s1=new Scanner(System.in);
		Scanner s2=new Scanner(System.in);
		String name;
		String sports;
		float ac_score;
		float spo_score;
		System.out.println("enter the student name");
		name=s1.nextLine();
		System.out.println("enter the academic score");
		ac_score=s2.nextFloat();
		System.out.println("enter the sports name");
		sports=s1.nextLine();
		System.out.println("enter the sports score");
		spo_score=s2.nextFloat();
		Result r=new Result(name,ac_score,sports,spo_score);
		r.display();
	}
}