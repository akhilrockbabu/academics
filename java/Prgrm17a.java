import java.io.*;

class Prgrm17a
{
	public static void main(String arg[]) throws IOException
	{
		String s;
		try
		{
			InputStreamReader in=new InputStreamReader(System.in);
			BufferedReader br1=new BufferedReader(in);
			System.out.println("enter the string");	
			s=br1.readLine();
			FileWriter fw=new FileWriter("D:/Codes/academics/java/prgrm17a.txt");
			BufferedWriter bw=new BufferedWriter(fw);
			bw.append(s);
			bw.newLine();
			System.out.println("File Updated Successfully !");
			bw.close();
			System.out.println("Current File Content is : ");

			FileReader fr=new FileReader("D:/Codes/academics/java/prgrm17a.txt");
			BufferedReader br2=new BufferedReader(fr);
			while((s=br2.readLine())!=null)
			{
				System.out.println(s);			
			}
			br2.close();
		}
		catch(IOException e)
		{
			System.out.println(e);
		}
		
	}
}



































