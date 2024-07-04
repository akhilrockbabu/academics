import java.awt.*;
import java.awt.event.*;

public class Prgrm18b extends Frame implements ActionListener
{
	TextField t1,t2,t3;
	Label l1,l2,l3;
	Button b1,b2,b3,b4;
	Prgrm18b()
	{
		setLayout(new GridLayout(8, 2,10,10));
		l1=new Label("First Number");
		l2=new Label("Second Number");
		l3=new Label("Result");
		t1=new TextField(2);
		t2=new TextField(2);
		t3=new TextField(5);
		b1=new Button("+");
		b2=new Button("-");
		b3=new Button(" *");
		b4=new Button("/");
		add(l1);
		add(t1);
		add(l2);
		add(t2);
		add(b1);
		add(b2);
		add(b3);
		add(b4);
		add(l3);
		add(t3);
		b1.addActionListener(this);
		b2.addActionListener(this);
		b3.addActionListener(this);
		b4.addActionListener(this);
	}
	public void actionPerformed(ActionEvent ae)
	{
		Double a,b;
		a=Double.parseDouble(t1.getText());
		b=Double.parseDouble(t2.getText());

		if(ae.getSource()==b1)
			t3.setText(""+(a+b));

		else if(ae.getSource()==b2)
			t3.setText(""+(a-b));

		else if(ae.getSource()==b3)
			t3.setText(""+(a*b));

		else
			{
				if(b==0)
					t3.setText("ERROR");
				else
					t3.setText(""+(a/b));
			}
	}
	public static void main(String arg[])
	{
		Prgrm18b p=new Prgrm18b();
		p.setTitle("Calculator");
		p.setSize(500,300);
		p.setVisible(true);
	}
}