import java.io.*;

class Prgrm17b
{
	public static void main(String arg[])throws IOException
	{
		String dig;
		try
		{
			FileWriter fw1=new FileWriter("/home/user/academics/java/prgrm17b1.txt");
			FileWriter fw2=new FileWriter("/home/user/academics/java/prgrm17b2.txt");
			BufferedWriter bw1=new BufferedWriter(fw1);
			BufferedWriter bw2=new BufferedWriter(fw2);
			
			FileReader fr1=new FileReader("/home/user/academics/java/prgrm17b.txt");
			BufferedReader br1=new BufferedReader(fr1);
			while((dig=br1.readLine())!=null)
			{
				if(Integer.parseInt(dig)%2==0)
				{
					bw2.append(dig);
					bw2.newLine();
				}
				else
				{
					bw1.append(dig);
					bw1.newLine();
				}
			}
			bw1.close();
			bw2.close();
			br1.close();
		}
		catch(IOException e)
		{
			System.out.println(e);
		}
	}
}
