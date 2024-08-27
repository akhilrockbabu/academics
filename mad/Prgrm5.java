package com.example.prgrm5;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    EditText email,password;
    String a,b;
    SharedPreferences sp;
    Button login;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        sp=getSharedPreferences("MyPref",MODE_PRIVATE);
        email=(EditText) findViewById(R.id.ed1);
        password=(EditText) findViewById(R.id.ed2);

        login=(Button) findViewById(R.id.bt1);
        login.setOnClickListener(this);
        if(sp.contains("Email"))
            email.setText(sp.getString("Email",""));
        if(sp.contains("pass"))
            password.setText(sp.getString("pass",""));


    }

    @Override
    public void onClick(View view) {
        a=email.getText().toString();
        b=password.getText().toString();
        SharedPreferences.Editor editor=sp.edit();
        editor.putString("Email",a);
        editor.putString("pass",b);
        editor.apply();
        Intent i= new Intent(this,SecondAct.class);
        startActivity(i);


    }
}
