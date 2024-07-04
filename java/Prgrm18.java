import java.awt.*;
import java.awt.event.*;
public class Prgrm18 extends Frame implements ActionListener
{
	TextField t1,t2,t3,t4;
	Label l1,l2,l3,l4;
	Button b1;
	Prgrm18()
	{
		setLayout(new FlowLayout());
		t1=new TextField(2);
		t2=new TextField(2);
		t3=new TextField(2);
		t4=new TextField(3);
		l1=new Label("First Number");
		l2=new Label("Second Number");
		l3=new Label("Third Number");
		l4=new Label("result");
		b1=new Button("check");
		add(l1);
		add(t1);
		add(l2);
		add(t2); 
		add(l3);
		add(t3);
		add(b1);
		add(l4);
		add(t4);
		t1.setText("");
		t2.setText("");
		t3.setText("");
		t4.setText("");
		b1.addActionListener(this);
	}
	public void actionPerformed(ActionEvent ae)
	{
		int a,b,c;
		if(ae.getSource()==b1)
		{
			a=Integer.parseInt(t1.getText());
			b=Integer.parseInt(t2.getText());
			c=Integer.parseInt(t3.getText());
			if(a>b && a>c)
				t4.setText(""+a);
			else if(b>c)
				t4.setText(""+b);
			else
				t4.setText(""+c);
		}
	}
	public static void main(String arg[])
	{
		Prgrm18 p=new Prgrm18();
		p.setTitle("Compare");
		p.setSize(200,300);
		p.setVisible(true);
	}
}
			
			
		
		
		
