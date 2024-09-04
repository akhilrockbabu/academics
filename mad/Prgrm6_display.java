package com.example.prgrm11;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class display extends AppCompatActivity
{
    TextView name,phno;
    SharedPreferences sp;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_display);

        name = (TextView) findViewById(R.id.t1);

        phno = (TextView) findViewById(R.id.t2);

        if(sp.contains("Name"))
            name.setText(sp.getString("Name",""));
        if(sp.contains("Phno"))
            phno.setText(sp.getString("Phno",""));


    }
}
