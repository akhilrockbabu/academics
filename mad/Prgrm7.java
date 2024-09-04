package com.example.prgrm6;

import android.os.Bundle;

import androidx.activity.EdgeToEdge;

import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    EditText user,pwd;
    Button login;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        user = (EditText) findViewById(R.id.ed1);
        pwd = (EditText) findViewById(R.id.ed2);
        login = (Button) findViewById(R.id.bt1);

        login.setOnClickListener(this);

    }

    @Override
    public void onClick(View view)
    {
        if(user.getText().toString().equals("rockiey") && pwd.getText().toString().equals("123"))
        {
            Toast t1 = Toast.makeText(this," ", Toast.LENGTH_LONG);
            LayoutInflater Lin = getLayoutInflater();
            View appear = Lin.inflate(R.layout.toast2_layout, (ViewGroup) findViewById(R.id.toast2_id));
            t1.setGravity(Gravity.TOP,0,1200);
            t1.setView(appear);
            t1.show();

        }
        else
        {
            Toast t1 = Toast.makeText(this," ", Toast.LENGTH_LONG);
            LayoutInflater Lin = getLayoutInflater();
            View appear = Lin.inflate(R.layout.toast1_layout, (ViewGroup) findViewById(R.id.toast1_id));
            t1.setGravity(Gravity.TOP,0,1200);
            t1.setView(appear);
            t1.show();
        }



    }
}
