package com.example.prgrm11;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    EditText e1, e2;
    Button b1, b2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        e1 = (EditText) findViewById(R.id.usr);
        e2 = (EditText) findViewById(R.id.pass);
        b1 = (Button) findViewById(R.id.btn1);
        b2 = (Button) findViewById(R.id.btn2);

        b1.setOnClickListener(this);
        b2.setOnClickListener(this);
    }

    @Override
    public void onClick(View view) {
        if (view.getId() == R.id.btn1) {
            if (e1.getText().toString().equals("dona") && e2.getText().toString().equals("123")) {
                Toast.makeText(this, "Login successful", Toast.LENGTH_LONG).show();
            } else {
                Toast.makeText(this, "Login failed", Toast.LENGTH_LONG).show();
            }
        } else {
            Intent i = new Intent(this, Registration.class);
            startActivity(i);
        }
    }
}
