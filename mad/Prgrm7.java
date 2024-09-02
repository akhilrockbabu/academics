package com.example.prgrm7;

import android.graphics.Typeface;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    ImageView i1;
    LinearLayout l1;
    TextView t1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        i1 = (ImageView) findViewById(R.id.img1);
        l1 = (LinearLayout) findViewById(R.id.layout1);
        t1 = (TextView) findViewById(R.id.tv1);

        Typeface myfont = Typeface.createFromAsset(getAssets(),"font/CarryYouRegular-3z71M.ttf");
        t1.setTypeface(myfont);

        i1.setOnClickListener(this);
        l1.setOnClickListener(this);
    }

    @Override
    public void onClick(View view)
    {
        if(view.getId() == R.id.img1)
        {
            i1.setVisibility(View.GONE);
            l1.setVisibility(View.VISIBLE);
        }
        else
        {
            i1.setVisibility(View.VISIBLE);
            l1.setVisibility(View.GONE);
        }

    }
}
