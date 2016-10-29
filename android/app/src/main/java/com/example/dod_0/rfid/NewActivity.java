package com.example.dod_0.rfid;

import android.content.BroadcastReceiver;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.ServiceConnection;
import android.content.pm.ActivityInfo;
import android.os.Bundle;
import android.os.IBinder;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.widget.Toast;

import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeoutException;

import io.swagger.client.api.CategoryApi;
import io.swagger.client.model.Category;
import io.swagger.client.ApiException;

public class NewActivity extends AppCompatActivity {
    public static final String EXTRAS_DEVICE_NAME = "DEVICE_NAME"; //name
    public static final String EXTRAS_DEVICE_ADDRESS = "DEVICE_ADDRESS";    //mac address
    private static BluetoothLeService mBluetoothLeService;
    private String mDeviceName;
    private String mDeviceAddress;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
        final Intent intent = getIntent();
        mDeviceName = intent.getStringExtra(EXTRAS_DEVICE_NAME);
        mDeviceAddress = intent.getStringExtra(EXTRAS_DEVICE_ADDRESS);
        setContentView(R.layout.activity_new);

        Thread t = new Thread(new Runnable() {
            @Override
            public void run() {
                CategoryApi apiInstance = new CategoryApi();
                try {
                    List<Category> result = apiInstance.categoryDetailsGet();
                    System.out.println(result);
                } catch (ApiException e) {
                    System.err.println("Exception when calling CategoryApi#categoryDetailsGet");
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } catch (ExecutionException e) {
                    e.printStackTrace();
                } catch (TimeoutException e) {
                    e.printStackTrace();
                }
            }
        });
        t.start();

    }

    @Override
    protected void onResume() {
        super.onResume();

        /*
         * Register a BroadcastReceiver to be run in the main activity thread.
         */
        Log.d("DEVICECONTROL","onResume");
        registerReceiver(mGattUpdateReceiver, makeGattUpdateIntentFilter());
        if (mBluetoothLeService != null) {
            final boolean result = mBluetoothLeService.connect(mDeviceAddress);
            Log.d("aa", "Connect request result=" + result);
        }
        else
            Log.e("a", "Connection error!!");
    }


    private final ServiceConnection mServiceConnection = new ServiceConnection() {

        /**
         * Called when a connection to the Service has been established,
         *      with the IBinder of the communication channel to the Service.
         */
        @Override
        public void onServiceConnected(ComponentName componentName, IBinder service) {
            mBluetoothLeService = ((BluetoothLeService.LocalBinder) service).getService();
            if (!mBluetoothLeService.initialize()) {
                Log.e("as", "Unable to initialize Bluetooth");
                finish();
            }
            // Automatically connects to the device upon successful start-up initialization.
            mBluetoothLeService.connect(mDeviceAddress);
            //Log.d(TAG, "Connected Successfully!!");

            //[rodrigo]
            //((TextView) findViewById(R.id.deviceName)).setText(mDeviceName);
        }

        /**
         * Called when a connection to the Service has been lost.
         */
        @Override
        public void onServiceDisconnected(ComponentName componentName) {
            mBluetoothLeService = null;
        }
    };


    /**
     *  Base class for code that will receive intents sent by sendBroadcast().
     *
     *  Handles various events fired by the Service.
     *      ACTION_GATT_CONNECTED: connected to a GATT server.
     *      ACTION_GATT_DISCONNECTED: disconnected from a GATT server.
     *      ACTION_GATT_SERVICES_DISCOVERED: discovered GATT services.
     *      ACTION_DATA_AVAILABLE: received data from the device.  This can be a result of read
     *                        or notification operations.
     */
    private final BroadcastReceiver mGattUpdateReceiver = new BroadcastReceiver() {

        /*
         * This method is called when the BroadcastReceiver is receiving an Intent broadcast.
         * During this time you can use the other methods on BroadcastReceiver to view/modify the current result values
         *
         * This intent broadcast are being sent by the BluetoothLeService
         */
        @Override
        public void onReceive(Context context, Intent intent) {
            final String action = intent.getAction();

            Log.d("BROADCAST_RECEIVER_NEW",action);



            if (BluetoothLeService.ACTION_DATA_AVAILABLE.equals(action)) {
                displayData(intent.getStringExtra(BluetoothLeService.EXTRA_DATA));
            }

        }
    };

    private void displayData(String data) {
        if (data != null) {
            //mDataField.setText(data);
            Log.d("DATA RECEIVED: ",data);
            //Toast.makeText(getApplicationContext(), data, Toast.LENGTH_SHORT).show();
        }

    }

    private static IntentFilter makeGattUpdateIntentFilter() {
        final IntentFilter intentFilter = new IntentFilter();
        intentFilter.addAction(BluetoothLeService.ACTION_GATT_CONNECTED);
        intentFilter.addAction(BluetoothLeService.ACTION_GATT_DISCONNECTED);
        intentFilter.addAction(BluetoothLeService.ACTION_GATT_SERVICES_DISCOVERED);
        intentFilter.addAction(BluetoothLeService.ACTION_DATA_AVAILABLE);
        return intentFilter;
    }

}
