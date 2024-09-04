package com.example.prgrm11;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.RadioButton;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class Registration extends AppCompatActivity implements View.OnClickListener {
    EditText e1,e2;
    RadioButton f,m;
    CheckBox c1,c2;
    Button b;
    SharedPreferences sp;
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registration);

        e1 = (EditText) findViewById(R.id.n);
        e2 = (EditText) findViewById(R.id.p);
        f = (RadioButton) findViewById(R.id.f);
        m = (RadioButton) findViewById(R.id.m);
        c1 = (CheckBox) findViewById(R.id.c1);
        c2 = (CheckBox) findViewById(R.id.c2);
        b = (Button) findViewById(R.id.b);
        b.setOnClickListener(this);
    }

    @Override
    public void onClick(View v)
    {
        String name = e1.getText().toString();
        String phno = e2.getText().toString();
        sp = getSharedPreferences("mypref",MODE_PRIVATE);
        SharedPreferences.Editor ed = sp.edit();
        ed.putString("Name",name);
        ed.putString("Phno",phno);
        ed.apply();
        Intent i = new Intent(this,display.class);
        startActivity(i);
    }
}
