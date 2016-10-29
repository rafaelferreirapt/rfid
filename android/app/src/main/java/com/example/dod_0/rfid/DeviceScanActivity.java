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
import android.app.ListActivity;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothManager;
import android.content.Context;
import android.content.Intent;
import android.content.pm.ActivityInfo;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;

/**
 * Activity for scanning and displaying available Bluetooth LE devices.
 */
public class DeviceScanActivity extends ListActivity {

    private LeDeviceListAdapter mLeDeviceListAdapter;   //responsible for holding devices found
    private BluetoothAdapter mBluetoothAdapter; //represents the local device Bluetooth adapter
    private boolean mScanning;  //see if scanning is being done
    private Handler mHandler;   // Handler allows you to send and process and Runnable objects associated with a thread's
    private static final int REQUEST_ENABLE_BT = 1;
    private static final long SCAN_PERIOD = 10000;     // Stops scanning after 10 seconds


    /*
     * Called when the activity is first created.
     * This is where you should do all of your normal static set up: create views, bind data to lists, etc.
     * This method also provides you with a Bundle containing the activity's previously frozen state, if there was one.
     * Always followed by onStart().
     */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);

        //getActionBar().setTitle(R.string.title_devices);
        mHandler = new Handler();

        // Use this check to determine whether BLE is supported on the device.  Then you can
        // selectively disable BLE-related features.
        if (!getPackageManager().hasSystemFeature(PackageManager.FEATURE_BLUETOOTH_LE)) {
            Toast.makeText(this, R.string.ble_not_supported, Toast.LENGTH_SHORT).show();
            finish();
        }

        // Initializes a Bluetooth adapter.  For API level 18 and above, get a reference to
        // BluetoothAdapter through BluetoothManager.
        final BluetoothManager bluetoothManager =
                (BluetoothManager) getSystemService(Context.BLUETOOTH_SERVICE);
        mBluetoothAdapter = bluetoothManager.getAdapter();

        // Checks if Bluetooth is supported on the device.
        if (mBluetoothAdapter == null) {
            Toast.makeText(this, R.string.error_bluetooth_not_supported, Toast.LENGTH_SHORT).show();
            finish();
            return;
        }
    }


    /*
     * Called when the activity is becoming visible to the user.
     * Followed by onResume() if the activity comes to the foreground, or onStop() if it becomes hidden.
     */
    @Override
    public void onStart() {
        super.onStart();
    }

    /*
     * Called when the activity will start interacting with the user.
     * At this point your activity is at the top of the activity stack, with user input going to it.
     * Always followed by onPause().
     *
     * Activity running
     */
    @Override
    protected void onResume() {
        super.onResume();

        // Ensures Bluetooth is enabled on the device.  If Bluetooth is not currently enabled,
        // fire an intent to display a dialog asking the user to grant permission to enable it.
        if (!mBluetoothAdapter.isEnabled()) {
            if (!mBluetoothAdapter.isEnabled()) {
                Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
                startActivityForResult(enableBtIntent, REQUEST_ENABLE_BT);
            }
        }

        mLeDeviceListAdapter = new LeDeviceListAdapter();   // Initializes list view adapter.

        setListAdapter(mLeDeviceListAdapter);
        scanLeDevice(true); //starts automaticaly the scanning -> stops when finished the scanning period
    }


    /*
     * Called when the system is about to start resuming a previous activity.
     * This is typically used to commit unsaved changes to persistent data,
     *      stop animations and other things that may be consuming CPU, etc.
     * Implementations of this method must be very quick because the next activity
     *      will not be resumed until this method returns.
     * Followed by either onResume() if the activity returns back to the front,
     *      or onStop() if it becomes invisible to the user.
     */
    @Override
    protected void onPause() {  //pausing the ble scanning after the period scanning
        super.onPause();
        scanLeDevice(false);
        mLeDeviceListAdapter.clear();
    }


    /*
     * Called when the activity is no longer visible to the user,
     *      because another activity has been resumed and is covering this one.
     * This may happen either because a new activity is being started, an existing one
     *      is being brought in front of this one, or this one is being destroyed.
     * Followed by either onRestart() if this activity is coming back to interact with the user,
     *      or onDestroy() if this activity is going away.
     */
    @Override
    public void onStop() {
        super.onStop();
    }


    /*
     * This function is responsible to start the scanning of the ble devices
     * This would be treated in the scan callback function (mLeScanCallback)
     */
    private void scanLeDevice(final boolean enable) {

        if (enable) {
            mHandler.postDelayed(new Runnable() {
                @Override
                public void run() {
                    mScanning = false;
                    mBluetoothAdapter.stopLeScan(mLeScanCallback);
                    Log.d("[R]scanLeDevice","scanning stopped!");
                    //invalidateOptionsMenu();
                }
            }, SCAN_PERIOD);    // Stops scanning after a pre-defined scan period.
            Log.d("[R]scanLeDevice","scanning running");
            mScanning = true;
            mBluetoothAdapter.startLeScan(mLeScanCallback); //view callback!
        } //else {
        //  mScanning = false;
        //  mBluetoothAdapter.stopLeScan(mLeScanCallback);
        //}
        //invalidateOptionsMenu();
    }


    /*
     * Creation of the callbak function to treat the ble devices in the network
     */
    private BluetoothAdapter.LeScanCallback mLeScanCallback = new BluetoothAdapter.LeScanCallback() {

        @Override
        public void onLeScan(final BluetoothDevice device, int rssi, final byte[] scanRecord) {
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    mLeDeviceListAdapter.addDevice(device);
                    mLeDeviceListAdapter.notifyDataSetChanged();    //calls getView form the LeDeviceAdapter class
                }
            });
        }
    };


    /*
    * This method will be called when an item in the list is selected
    * Starts the DeviceControlActivity intent
    */
    @Override
    protected void onListItemClick(ListView l, View v, int position, long id) {
        final BluetoothDevice device = mLeDeviceListAdapter.getDevice(position);

        if (device == null) return;

        final Intent intent = new Intent(this, DeviceControlActivity.class);
        intent.putExtra(DeviceControlActivity.EXTRAS_DEVICE_NAME, device.getName());
        intent.putExtra(DeviceControlActivity.EXTRAS_DEVICE_ADDRESS, device.getAddress());
        if (mScanning) {    //stop scanning if is running
            mBluetoothAdapter.stopLeScan(mLeScanCallback);
            mScanning = false;
        }
        startActivity(intent);  //starts DeviceControlActivity intent
    }


    /*
     * Controls the response of the user after being asked to turn on the ble of the device
     * Result of the: startActivityForResult(enableBtIntent, REQUEST_ENABLE_BT);
     */
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {

        if (requestCode == REQUEST_ENABLE_BT && resultCode == Activity.RESULT_CANCELED) {
            finish();
            return;
        }
        super.onActivityResult(requestCode, resultCode, data);
    }


    /*
     * This class is responsible to create and manage the list of the several devices found
     */
    private class LeDeviceListAdapter extends BaseAdapter {
        private ArrayList<BluetoothDevice> mLeDevices;
        private LayoutInflater mInflator;   //Instantiates a layout XML file into its corresponding objects

        /*
         * Initializes the ArrayList of the ble devices
         * Get the layout infaltor ??
         */
        public LeDeviceListAdapter() {
            super();
            mLeDevices = new ArrayList<BluetoothDevice>();  //Array of the ble devices found
            mInflator = DeviceScanActivity.this.getLayoutInflater();
        }

        /*
         *  Add new ble device to the arrayList created before (mLeDevices)
         */
        public void addDevice(BluetoothDevice device) {
            if (!mLeDevices.contains(device)) {
                mLeDevices.add(device); //add new device to the arraylist
                Log.d("DEVICE found: ",device.getName());
            }
        }

        /*
         *  Get device based on the position in the arraylist
         */
        public BluetoothDevice getDevice(int position) { return mLeDevices.get(position); }

        /*
         * Clears the arraylist
         */
        public void clear() {
            mLeDevices.clear();
        }

        /*
         * Get number of ble devices found
         */
        public int getCount() { return mLeDevices.size(); }


        /*
         * Responsible to update the view of the list of the ble devices in display
         * Is processed after the notification: mLeDeviceListAdapter.notifyDataSetChanged();
         */
        @Override
        public View getView(int i, View view, ViewGroup viewGroup) {
            ViewHolder viewHolder;
            // General ListView optimization code.
            if (view == null) {
                view = mInflator.inflate(R.layout.listitem_device, null);
                viewHolder = new ViewHolder();
                viewHolder.deviceAddress = (TextView) view.findViewById(R.id.device_address);
                viewHolder.deviceName = (TextView) view.findViewById(R.id.device_name);
                view.setTag(viewHolder);
            } else {
                viewHolder = (ViewHolder) view.getTag();
            }

            BluetoothDevice device = mLeDevices.get(i);
            String deviceName;
            if (mLeDevices.size() == 1)
                deviceName = "Device List:\n" + device.getName();
            else
                deviceName = device.getName();

            if (deviceName != null && deviceName.length() > 0)
                viewHolder.deviceName.setText(deviceName);  //set the device name in the display list
            else
                viewHolder.deviceName.setText(R.string.unknown_device); //set "unkown device" if can't get name
            viewHolder.deviceAddress.setText(device.getAddress());

            return view;
        }

        @Override
        public Object getItem(int i) {
            return mLeDevices.get(i);
        }

        @Override
        public long getItemId(int i) {
            return i;
        }

    }

    static class ViewHolder {
        TextView deviceName;
        TextView deviceAddress;
    }
}

