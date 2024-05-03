import java.util.Scanner;

class Prgrm4
{
	public static void main(String arg[])
	{
		Scanner s=new Scanner(System.in);
		System.out.println("enter the no of row");
		int row=s.nextInt();
		System.out.println("enter the no of column");
		int column=s.nextInt();
		Matrix m1=new Matrix();
		System.out.println("enter matrix 1");
		int arr1[][]=m1.read(row,column);
		System.out.println("enter matrix 2");
		int arr2[][]=m1.read(row,column);
		m1.add(arr1,arr2);
		
	}
	
	
	
}

class Matrix
{
	Scanner s=new Scanner(System.in);
	int[][] read(int row,int column)
	{
		int res[][]=new int[row][column];
		for(int i=0;i<row;++i)
		{
			for(int j=0;j<column;++j)
			{
				res[i][j]=s.nextInt();
			}
		}
		return res;
	}
	
	void add(int a1[][],int a2[][])
	{
		System.out.println("Sum Matrix is : ");
		for(int i=0;i<a1[1].length;++i)
		{
			for(int j=0;j<a1.length;++j)
			{
				System.out.print(a1[i][j]+a2[i][j]+"\t");
			}
			System.out.println();
		}
	}
}
