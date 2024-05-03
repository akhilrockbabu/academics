import java.util.Scanner;
class Arraydemo
{
	public static void main(String arg[])
	{
		int[] arr1=new int[10];
		int len=arg.length;
		Input in=new Input();
		arr1=in.read();
		System.out.println("Recieved array is : ");
		for(int i=0;i<10;++i)
		{
			System.out.println(arr1[i]);
		}
		System.out.println("command line Recieved array is : ");
		for(int i=0;i<len;++i)
		{
			System.out.println(arg[i]);
		}
	}
}

class Input
{
	int[] res=new int[10];
	int[] read()
	{
		Scanner s=new Scanner(System.in);
		System.out.println("enter the array with 10 elements");
		for(int i=0;i<10;++i)
		{
			res[i]=s.nextInt();
		}
		return res;
	}
	
}
