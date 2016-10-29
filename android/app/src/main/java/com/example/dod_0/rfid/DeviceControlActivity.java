/*
 * Copyright (C) 2013 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.example.dod_0.rfid;

import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothGattCharacteristic;
import android.bluetooth.BluetoothGattService;
import android.content.BroadcastReceiver;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.ServiceConnection;
import android.content.pm.ActivityInfo;
import android.os.Bundle;
import android.os.IBinder;
import android.util.Log;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * For a given BLE device, this Activity provides the user interface to connect, display data,
 * and display GATT services and characteristics supported by the device.  The Activity
 * communicates with {@code BluetoothLeService}, which in turn interacts with the
 * Bluetooth LE API.
 */
public class DeviceControlActivity extends Activity {
    private final static String TAG = DeviceControlActivity.class.getSimpleName();

    public static final String EXTRAS_DEVICE_NAME = "DEVICE_NAME"; //name
    public static final String EXTRAS_DEVICE_ADDRESS = "DEVICE_ADDRESS";    //mac address

    private TextView mConnectionState;  //TextView for the connection State display
    private TextView mDataField;    //Text view for exposing the received data
    private String mDeviceName;
    private String mDeviceAddress;
    //private ExpandableListView mGattServicesList;
    private static BluetoothLeService mBluetoothLeService;
    private ArrayList<ArrayList<BluetoothGattCharacteristic>> mGattCharacteristics =
            new ArrayList<ArrayList<BluetoothGattCharacteristic>>();
    private boolean mConnected = true;  //check if app is connected to device
    private BluetoothGattCharacteristic mNotifyCharacteristic;

    private final String LIST_NAME = "NAME";
    private final String LIST_UUID = "UUID";

    private boolean initFlag = true;
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE);
        setContentView(R.layout.gatt_services_characteristics); //set new layout (gatt_services_characteristics layout)

        final Intent intent = getIntent();
        mDeviceName = intent.getStringExtra(EXTRAS_DEVICE_NAME);
        mDeviceAddress = intent.getStringExtra(EXTRAS_DEVICE_ADDRESS);

        // Sets up UI references.
        ((TextView) findViewById(R.id.device_address)).setText(mDeviceAddress);//???
        //mGattServicesList = (ExpandableListView) findViewById(R.id.gatt_services_list);
        //mGattServicesList.setOnChildClickListener(servicesListClickListner);

        //TextView's responsible for the 'data' and 'data title'
        mConnectionState = (TextView) findViewById(R.id.connection_state);  //connection state
        mDataField = (TextView) findViewById(R.id.data_value);  //data

        Intent gattServiceIntent = new Intent(this, BluetoothLeService.class);

        /**
         *  The first parameter of bindService() is an Intent that explicitly names the service to bind
         *      (thought the intent could be implicit).
         *  The second parameter is the ServiceConnection object.
         *  The third parameter is a flag indicating options for the binding.
         *      It should usually be BIND_AUTO_CREATE in order to create the service if its not already alive.
         *      Other possible values are BIND_DEBUG_UNBIND and BIND_NOT_FOREGROUND, or 0 for none.
         */
        bindService(gattServiceIntent, mServiceConnection, BIND_AUTO_CREATE);
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
            Log.d(TAG, "Connect request result=" + result);
        }
        else
            Log.e(TAG, "Connection error!!");
    }

    @Override
    protected void onPause() {
        super.onPause();
        unregisterReceiver(mGattUpdateReceiver);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        unbindService(mServiceConnection);
        mBluetoothLeService = null;
    }



    /*
     *  Code to manage Service lifecycle.
     *  Monitors the connection with the service.
     *  The bindService() method returns immediately without a value,
     *      but when the Android system creates the connection between the client and service,
     *      it calls onServiceConnected() on the ServiceConnection, to deliver the IBinder
     *      that the client can use to communicate with the service.
     */
    private final ServiceConnection mServiceConnection = new ServiceConnection() {

        /**
         * Called when a connection to the Service has been established,
         *      with the IBinder of the communication channel to the Service.
         */
        @Override
        public void onServiceConnected(ComponentName componentName, IBinder service) {
            mBluetoothLeService = ((BluetoothLeService.LocalBinder) service).getService();
            if (!mBluetoothLeService.initialize()) {
                Log.e(TAG, "Unable to initialize Bluetooth");
                finish();
            }
            // Automatically connects to the device upon successful start-up initialization.
            mBluetoothLeService.connect(mDeviceAddress);
            Log.d(TAG, "Connected Successfully!!");

            //[rodrigo]
            ((TextView) findViewById(R.id.deviceName)).setText(mDeviceName);
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

            //TextView t = (TextView) findViewById(R.id.data_value);  //data place
            /*if(BluetoothLeService.color==0)
                t.setTextColor(Color.GREEN);
            else if(BluetoothLeService.color==1)
                t.setTextColor(Color.RED);
            else
                t.setTextColor(Color.BLUE);*/

            Log.d("BROADCAST_RECEIVER",action);



            if (BluetoothLeService.ACTION_GATT_CONNECTED.equals(action)) {
                mConnected = true;
                updateConnectionState(R.string.connected);
                //invalidateOptionsMenu();
            } else if (BluetoothLeService.ACTION_GATT_DISCONNECTED.equals(action)) {
                mConnected = false;
                updateConnectionState(R.string.disconnected);
                //invalidateOptionsMenu();
                //clearUI();
            } else if (BluetoothLeService.ACTION_GATT_SERVICES_DISCOVERED.equals(action)) {
                // Show all the supported services and characteristics on the user interface.
                displayGattServices(mBluetoothLeService.getSupportedGattServices());
                //updateConnectionState(R.string.connected);
            } else if (BluetoothLeService.ACTION_DATA_AVAILABLE.equals(action)) {
                displayData(intent.getStringExtra(BluetoothLeService.EXTRA_DATA));

                /*
                 * [!!IMPORTANTE]: necessário para a inicializacao da callback da characteristicsNotification!
                 *                  caso não seja feito este if, apenas se recebe a primera string de info!
                 */
                if(initFlag) {
                    displayGattServices(mBluetoothLeService.getSupportedGattServices());
                    initFlag = false;
                }
            }

        }
    };

    /*
    // If a given GATT characteristic is selected, check for supported features.  This sample
    // demonstrates 'Read' and 'Notify' features.  See
    // http://d.android.com/reference/android/bluetooth/BluetoothGatt.html for the complete
    // list of supported characteristic features.
    private final ExpandableListView.OnChildClickListener servicesListClickListner =
            new ExpandableListView.OnChildClickListener() {
                @Override
                public boolean onChildClick(ExpandableListView parent, View v, int groupPosition,
                                            int childPosition, long id) {
                    if (mGattCharacteristics != null) {
                        final BluetoothGattCharacteristic characteristic =
                                mGattCharacteristics.get(groupPosition).get(childPosition);
                        final int charaProp = characteristic.getProperties();
                        if ((charaProp | BluetoothGattCharacteristic.PROPERTY_READ) > 0) {
                            // If there is an active notification on a characteristic, clear
                            // it first so it doesn't update the data field on the user interface.
                            if (mNotifyCharacteristic != null) {
                                //mBluetoothLeService.setCharacteristicNotification(
                                //        mNotifyCharacteristic, false);
                                mNotifyCharacteristic = null;
                            }
                            mBluetoothLeService.readCharacteristic(characteristic);
                        }
                        if ((charaProp | BluetoothGattCharacteristic.PROPERTY_NOTIFY) > 0) {
                            mNotifyCharacteristic = characteristic;
                            //mBluetoothLeService.setCharacteristicNotification(
                            //        characteristic, true);
                        }
                        return true;
                    }
                    return false;
                }
    };

    /*private void clearUI() {
        mGattServicesList.setAdapter((SimpleExpandableListAdapter) null);
        mDataField.setText(R.string.no_data);
    }*/



    /*@Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.gatt_services, menu);
        if (mConnected) {
            menu.findItem(R.id.menu_connect).setVisible(false);
            menu.findItem(R.id.menu_disconnect).setVisible(true);
        } else {
            menu.findItem(R.id.menu_connect).setVisible(true);
            menu.findItem(R.id.menu_disconnect).setVisible(false);
        }
        return true;
    }*/

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        mBluetoothLeService.connect(mDeviceAddress);
        return true;
    }

    private void updateConnectionState(final int resourceId) {
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                mConnectionState.setText(resourceId);
            }
        });
    }

    private void displayData(String data) {
        if (data != null) {
            mDataField.setText(data);
            Log.d("DATA RECEIVED: ",data);
            //Toast.makeText(getApplicationContext(), data, Toast.LENGTH_SHORT).show();
        }

    }

    /*
     * Demonstrates how to iterate through the supported GATT Services/Characteristics.
     * In this sample, we populate the data structure that is bound to the ExpandableListView
     * on the UI.
     */
    private void displayGattServices(List<BluetoothGattService> gattServices) {
        if (gattServices == null) return;

        String uuid = null;
        String unknownServiceString = getResources().getString(R.string.unknown_service);
        String unknownCharaString = getResources().getString(R.string.unknown_characteristic);

        ArrayList<HashMap<String, String>> gattServiceData =
                new ArrayList<HashMap<String, String>>();
        ArrayList<ArrayList<HashMap<String, String>>> gattCharacteristicData
                = new ArrayList<ArrayList<HashMap<String, String>>>();
        mGattCharacteristics =
                new ArrayList<ArrayList<BluetoothGattCharacteristic>>();

        // Loops through available GATT Services.
        for (BluetoothGattService gattService : gattServices) {
            HashMap<String, String> currentServiceData = new HashMap<String, String>();
            uuid = gattService.getUuid().toString();

            currentServiceData.put(LIST_NAME, SampleGattAttributes.lookup(uuid, unknownServiceString));
            currentServiceData.put(LIST_UUID, uuid);
            gattServiceData.add(currentServiceData);

            ArrayList<HashMap<String, String>> gattCharacteristicGroupData =
                    new ArrayList<HashMap<String, String>>();
            List<BluetoothGattCharacteristic> gattCharacteristics = gattService.getCharacteristics();
            ArrayList<BluetoothGattCharacteristic> charas =
                    new ArrayList<BluetoothGattCharacteristic>();

            // Loops through available Characteristics.
            for (BluetoothGattCharacteristic gattCharacteristic : gattCharacteristics) {

                charas.add(gattCharacteristic);
                HashMap<String, String> currentCharaData = new HashMap<String, String>();
                uuid = gattCharacteristic.getUuid().toString();

                currentCharaData.put(LIST_NAME, SampleGattAttributes.lookup(uuid, unknownCharaString));
                currentCharaData.put(LIST_UUID, uuid);
                gattCharacteristicGroupData.add(currentCharaData);
            }
            mGattCharacteristics.add(charas);
            gattCharacteristicData.add(gattCharacteristicGroupData);
        Log.d("DisplayGattService","simple debug2");
        }

        //encontrada a carateristica de escrita!! "tentativa erro"
        final BluetoothGattCharacteristic characteristic = mGattCharacteristics.get(2).get(0);
        final int charaProp = characteristic.getProperties();
        Log.d("CHARAC_PROP", "" + charaProp);

        if ((charaProp | BluetoothGattCharacteristic.PROPERTY_READ) > 0) {
            Log.d("DisplayGattService", "simple debug3");
            // If there is an active notification on a characteristic, clear
            // it first so it doesn't update the data field on the user interface.
            if (mNotifyCharacteristic != null) {
                mBluetoothLeService.setCharacteristicNotification(
                        mNotifyCharacteristic, false);
                mNotifyCharacteristic = null;
            }

            mBluetoothLeService.readCharacteristic(characteristic);
        }
        if ((charaProp | BluetoothGattCharacteristic.PROPERTY_NOTIFY) > 0) {
            mNotifyCharacteristic = characteristic;
            mBluetoothLeService.setCharacteristicNotification(
                    characteristic, true);
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
    /*public void sendMessage(View view) {
        Intent intent = new Intent(this, End.class);
        BluetoothAdapter mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        if (mBluetoothAdapter.isEnabled()) {
            mBluetoothAdapter.disable();

        }
        mBluetoothLeService.close();
        mBluetoothAdapter=null;
        startActivity(intent);
    }*/

    public void returnButtonMethod(View abc){
        Log.d("DeviceControlActivity","Return Button pressed!");
        Intent intent = new Intent(this, MainActivity.class );
        startActivity(intent);
    }

    public void newScanButtonMethod(View abc){
        Log.d("DeviceControlActivity","New Scan Button pressed!");

        /*BluetoothAdapter mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        if (mBluetoothAdapter.isEnabled()) {
            mBluetoothAdapter.disable();

        }
        mBluetoothAdapter=null;*/
        mBluetoothLeService.close();

        onDestroy();    //unbind service
        Intent intent = new Intent(this, DeviceScanActivity.class );
        startActivity(intent);
    }


}
