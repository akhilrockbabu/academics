import java.io.*;

class Prgrm17
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
			FileWriter fw=new FileWriter("/home/user/academics/java/prgrm17.txt");
			BufferedWriter bw=new BufferedWriter(fw);
			bw.write(s);
			bw.append("data appended");
			bw.close();
			
			FileReader fr=new FileReader("/home/user/academics/java/prgrm17.txt");
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



































