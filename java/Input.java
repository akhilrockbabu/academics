import java.util.*;

class Input
{
	public static void main(String arg[])
	{
		try{
			Scanner s=new Scanner(System.in);
			System.out.println("enter the string");
			String st=s.nextLine();
			System.out.println("enter the integer");
			int i=s.nextInt();
			System.out.println("enter the Float");
			float f=s.nextFloat();
			
			System.out.println("String="+st);
			System.out.println("integer="+i);
			System.out.println("Float="+f);
		}
		catch(Exception e)
		{
			System.out.println("maryadhaku correct aayittu adikada funde");
		}
	}
}
