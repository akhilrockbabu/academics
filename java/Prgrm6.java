import java.util.Scanner;
class Prgrm6
{
	static void strsort(int n)
	{
		String[] str=new String[n];
		Scanner s=new Scanner(System.in);
		
		//read the strings
		System.out.println("enter strings : ");
		for(int i=0;i<n;++i)
		{
			str[i]=s.nextLine();	
		}
		
		//sort the strings
		for(int i=0;i<n;++i)
		{
			for(int j=i+1;j<n;++j)
			{
				if(str[i].compareTo(str[j])>0)
				{
					String temp=str[i];
					str[i]=str[j];
					str[j]=temp;
				}
			}
		}
		
		//print the sorted strings
		System.out.println("The sorted strings are : ");
		for(int i=0;i<n;++i)
		{
			System.out.println(str[i]);
		}
	}
	
	public static void main(String arg[])
	{
		int n;
		Scanner sc=new Scanner(System.in);
		System.out.println("enter the number of strings");
		n=sc.nextInt();
		strsort(n);
	}
}

