package com.example.dod_0.rfid;

import android.content.BroadcastReceiver;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.ServiceConnection;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.graphics.PixelFormat;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.IBinder;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.Surface;
import android.view.SurfaceView;
import android.view.View;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.Toast;


import java.io.InputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.UUID;

import io.swagger.client.ApiException;
import io.swagger.client.api.CategoryApi;
import io.swagger.client.model.Hall;


public class drawPath extends AppCompatActivity {
    private String sourceTag;
    private UUID destCategory;
    private String[] hallArr = {"1A253","1A254","1A255","1A256", "1A257"};
    private List<SurfaceView> floorTags = new ArrayList<>();
    private List<SurfaceView> floorTags2 = new ArrayList<>();
    private List<Hall> result = new ArrayList<>();
    private HashMap<String, SurfaceView> mapTags = new HashMap<>();
    private String[] realTags = {"3185769091","3858496131","3331214280","1754763934","1930754691"};

    //to receive BLE info
    public static final String EXTRAS_DEVICE_NAME = "DEVICE_NAME"; //name
    public static final String EXTRAS_DEVICE_ADDRESS = "DEVICE_ADDRESS";    //mac address
    private static BluetoothLeService mBluetoothLeService;
    private String mDeviceName;
    private String mDeviceAddress;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        final Intent intent = getIntent();

        //Get extra arguments
        Bundle extras = getIntent().getExtras();
        if (extras != null) {
            //The key argument here must match that used in the other activity
            sourceTag = extras.getString("sourceTAG");
            destCategory = UUID.fromString(extras.getString("destCat"));
        }
        Log.d("[DRAW_PATH]","--> "+sourceTag+ " -->"+destCategory);

        //Ble related
        mDeviceName = intent.getStringExtra(EXTRAS_DEVICE_NAME);
        mDeviceAddress = intent.getStringExtra(EXTRAS_DEVICE_ADDRESS);

        //set map on the display
        setContentView(R.layout.map_drawer);

        /*
         * New thread -> display the path
         */
        Thread tt = new Thread(new Runnable() {
            @Override
            public void run() {
                CategoryApi apiInstance = new CategoryApi();
                String hallTag = hallArr[0]; // String | Hall tag.
                UUID categoryId = destCategory; // UUID | Category ID
                try {
                    Log.d("DRAW_PATH", "Start drawing the path------------->" + apiInstance);
                    result = apiInstance.categorySearchHallTagCategoryIdGet(hallTag, categoryId);
                    System.out.println(result);
                } catch (ApiException e) {
                    System.err.println("Exception when calling CategoryApi#categorySearchHallTagCategoryIdGet");
                    e.printStackTrace();
                } catch (Exception e) {
                    System.err.println("Exception when calling CategoryApi#categorySearchHallTagCategoryIdGet");
                    e.printStackTrace();
                }

                /*
                 * Draw the path
                 */
                Log.d("DRAW_PATH", "Start drawing the path...");
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        Log.d("DRAW_PATH","Initializing SurfaceViewer");
                        //initialize floorTags
                        floorTags.add(0,(SurfaceView) findViewById(R.id.surfaceView11));
                        floorTags.add(1,(SurfaceView) findViewById(R.id.surfaceView21));
                        floorTags.add(2,(SurfaceView) findViewById(R.id.surfaceView31));
                        floorTags.add(3,(SurfaceView) findViewById(R.id.surfaceView61));
                        floorTags.add(4,(SurfaceView) findViewById(R.id.surfaceView71));

                        //initialize floorTags
                        floorTags2.add(0,(SurfaceView) findViewById(R.id.surfaceView12));
                        floorTags2.add(1,(SurfaceView) findViewById(R.id.surfaceView22));
                        floorTags2.add(2,(SurfaceView) findViewById(R.id.surfaceView32));
                        floorTags2.add(3,(SurfaceView) findViewById(R.id.surfaceView62));
                        floorTags2.add(4,(SurfaceView) findViewById(R.id.surfaceView72));

                        for(int i=0; i < hallArr.length; i++) {
                            mapTags.put(hallArr[i],floorTags.get(i));

                            floorTags.get(i).setVisibility(View.INVISIBLE); //all invisible
                            floorTags2.get(i).setVisibility(View.INVISIBLE); //all invisible
                        }
                        Log.d("DRAW_PATH","Initialization done");

                        for (int i = 0; i < result.size(); i++) {
                            Log.d("TAG -->", result.get(i).getTag());
                            mapTags.get(result.get(i).getTag()).setVisibility(View.VISIBLE);
                        }
                    }
                });
            }
        });
        tt.start();
    }

    /*
     * Function to update the map showed when the position of the user changed
     */
    private void pathUpdate(final String actualTag){

        Thread t = new Thread(new Runnable() {
            @Override
            public void run() {
                CategoryApi apiInstance = new CategoryApi();
                String hallTag = actualTag; // String | Hall tag.
                UUID categoryId = destCategory; // UUID | Category ID
                try {
                    result = apiInstance.categorySearchHallTagCategoryIdGet(hallTag, categoryId);
                    System.out.println(result);
                } catch (ApiException e) {
                    System.err.println("Exception when calling CategoryApi#categorySearchHallTagCategoryIdGet");
                    e.printStackTrace();
                } catch (Exception e) {
                    System.err.println("Exception when calling CategoryApi#categorySearchHallTagCategoryIdGet");
                    e.printStackTrace();
                }

                //Draw the path
                Log.d("DRAW_PATH", "Start drawing the path...");
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {

                        for(int i=0; i < hallArr.length; i++) {
                            mapTags.put(hallArr[i],floorTags.get(i));

                            floorTags.get(i).setVisibility(View.INVISIBLE); //all invisible
                            floorTags2.get(i).setVisibility(View.INVISIBLE); //all invisible
                        }
                        Log.d("DRAW_PATH","Initialization done");

                        for (int i = 0; i < result.size(); i++) {
                            Log.d("TAG -->", result.get(i).getTag());
                            mapTags.get(result.get(i).getTag()).setVisibility(View.VISIBLE);
                        }
                    }
                });
            }
        });
        t.start();
    }

    private class DownloadImageTask extends AsyncTask<String, Void, Bitmap> {
        ImageView bmImage;

        public DownloadImageTask(ImageView bmImage) {
            this.bmImage = bmImage;
        }

        protected Bitmap doInBackground(String... urls) {
            String urldisplay = urls[0];
            Bitmap mIcon11 = null;
            try {
                InputStream in = new java.net.URL(urldisplay).openStream();
                mIcon11 = BitmapFactory.decodeStream(in);
            } catch (Exception e) {
                Log.e("Error", e.getMessage());
                e.printStackTrace();
            }
            return mIcon11;
        }

        protected void onPostExecute(Bitmap result) {
            bmImage.setImageBitmap(result);
        }
    }

    /*
     * Canvas
     */
    public class AdaptImageViewer extends ImageView {

        private Paint currentPaint;
        public boolean drawRect = false;
        public float left;
        public float top;
        public float right;
        public float bottom;
        public AdaptImageViewer(Context context) {
            super(context);
            // TODO Auto-generated constructor stub

            currentPaint = new Paint();
            currentPaint.setDither(true);
            currentPaint.setColor(0xFFFFCCFF);  // alpha.r.g.b
            currentPaint.setStyle(Paint.Style.FILL);
            currentPaint.setStrokeJoin(Paint.Join.ROUND);
            currentPaint.setStrokeCap(Paint.Cap.ROUND);
            currentPaint.setStrokeWidth(2);
        }

        @Override
        protected void onDraw(Canvas canvas) {
            super.onDraw(canvas);
            Paint p = new Paint(Paint.ANTI_ALIAS_FLAG);

            if (drawRect) {
                canvas.drawRect(left, top, right, bottom, currentPaint);
            }

        }

    }


    /*
     * BLE related stuff
     */
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
            Log.d("DATA RECEIVED: ", data);
            Toast.makeText(getApplicationContext(), data, Toast.LENGTH_SHORT).show();

            int pos = isTagValid(data); //if tag is valid, return the tag position
            if(pos != -1) {
                pathUpdate(hallArr[pos]);
            }
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

    //Do the conversion between real tag values and the values in the sever
    private int isTagValid(String tag){
        for(int i = 0; i < realTags.length; i++){
            if(realTags[i].equals(tag))
                return i;
        }
        return -1;
    }

    /*
     * buttons
     */
    public void goBackButton(View abc){
        final Intent intent = new Intent(this, reader.class );
        startActivity(intent);
    }


}