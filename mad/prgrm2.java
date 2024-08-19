package com.example.project4;

import android.graphics.Color;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.Toast;
import android.widget.ToggleButton;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity implements TextWatcher, View.OnClickListener, CompoundButton.OnCheckedChangeListener {
    EditText percentage;
    CheckBox terms_Conds;
    ToggleButton theme;
    LinearLayout l;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        percentage = (EditText) findViewById(R.id.ed1);
        terms_Conds = (CheckBox) findViewById(R.id.cb1);
        theme = (ToggleButton) findViewById(R.id.tb1);
        terms_Conds.setOnClickListener(this);
        percentage.addTextChangedListener(this);
        theme.setOnCheckedChangeListener(this);
        l = findViewById(R.id.main);
    }


    @Override
    public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2)
    {

    }

    @Override
    public void onTextChanged(CharSequence charSequence, int i, int i1, int i2)
    {

    }

    @Override
    public void afterTextChanged(Editable editable)
    {

        float num;
        String s = editable.toString();
        if(s!=null && !s.isEmpty())
        {
            num = Float.parseFloat(s);
            if(num>100)
                editable.replace(0, editable.length(), "100");
        }

    }


    @Override
    public void onClick(View view)
    {
        if(terms_Conds.isChecked())
            Toast.makeText(this,"ACCEPTED", Toast.LENGTH_LONG).show();
        else
            Toast.makeText(this,"NOT ACCEPTED",Toast.LENGTH_LONG).show();
    }


    @Override
    public void onCheckedChanged(CompoundButton compoundButton, boolean b)
    {
        if(b)
        {
            l.setBackgroundColor(Color.WHITE);
            percentage.setTextColor(Color.DKGRAY);
            terms_Conds.setTextColor(Color.DKGRAY);
            theme.setTextColor(Color.DKGRAY);
        }
        else
        {
            l.setBackgroundColor(Color.DKGRAY);
            percentage.setTextColor(Color.WHITE);
            terms_Conds.setTextColor(Color.WHITE);
            theme.setTextColor(Color.WHITE);
        }
    }

}
