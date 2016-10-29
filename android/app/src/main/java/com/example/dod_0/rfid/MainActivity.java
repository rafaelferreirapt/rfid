package com.example.dod_0.rfid;

import android.content.Intent;
import android.content.pm.ActivityInfo;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
        setContentView(R.layout.activity_main);
    }

    public void NEXT(View abc){
        //Intent intent = new Intent(this, NewActivity.class);
        Intent intent = new Intent(this, reader.class);
        startActivity(intent);
    }

    public void bluetoothButtonMethod(View abc){
        Intent intent = new Intent(this, DeviceScanActivity.class );
        startActivity(intent);
    }

}
