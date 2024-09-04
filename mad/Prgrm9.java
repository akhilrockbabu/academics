package com.example.prgrm9;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    EditText num1,num2;
    TextView result;
    RadioButton add,sub,mul,div;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        num1 = (EditText) findViewById(R.id.et1);
        num2 = (EditText) findViewById(R.id.et2);
        result = (TextView) findViewById(R.id.tv1);

        add = (RadioButton) findViewById(R.id.add);
        sub = (RadioButton) findViewById(R.id.sub);
        mul = (RadioButton) findViewById(R.id.mul);
        div = (RadioButton) findViewById(R.id.div);

        add.setOnClickListener(this);
        sub.setOnClickListener(this);
        mul.setOnClickListener(this);
        div.setOnClickListener(this);



    }

    @Override
    public void onClick(View v)
    {
        int a = Integer.parseInt(num1.getText().toString());
        int b = Integer.parseInt(num2.getText().toString());
        if(v.getId() == R.id.add)
            result.setText(String.valueOf(a+b));
        if(v.getId() == R.id.sub)
            result.setText(String.valueOf(a-b));
        if(v.getId() == R.id.mul)
            result.setText(String.valueOf(a*b));
        if(v.getId() == R.id.div)
            result.setText(String.valueOf(a/b));

    }
}
