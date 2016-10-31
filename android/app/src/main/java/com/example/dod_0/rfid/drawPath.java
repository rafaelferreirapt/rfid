package com.example.dod_0.rfid;

import android.content.BroadcastReceiver;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.ServiceConnection;
import android.content.pm.ActivityInfo;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.IBinder;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.Toast;
import com.example.dod_0.rfid.reader;



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
    //private String[] hallArr = {"1A253","1A254","1A255","1A256", "1A257"};
    private List<ImageView> floorTags = new ArrayList<>();
    //private List<SurfaceView> floorTags2 = new ArrayList<>();
    private List<Hall> result = new ArrayList<>();
    private HashMap<String, ImageView> mapTags = new HashMap<>();
    //private String[] realTags = {"3185769091","3858496131","3331314280","1754763934","1930754691"};
    private String[] tagsIdFloor = {"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"};
    private String stateTag;

    //to receive BLE info
    public static final String EXTRAS_DEVICE_NAME = "DEVICE_NAME"; //name
    public static final String EXTRAS_DEVICE_ADDRESS = "DEVICE_ADDRESS";    //mac address
    private static BluetoothLeService mBluetoothLeService;
    private String mDeviceName;
    private String mDeviceAddress;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE);
        final Intent intent = getIntent();

        //Get extra arguments
        Bundle extras = getIntent().getExtras();
        if (extras != null) {
            //The key argument here must match that used in the other activity
            sourceTag = extras.getString("sourceTAG");
            destCategory = UUID.fromString(extras.getString("destCat"));
        }
        stateTag = sourceTag;
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

                //first path
                String hallTag = sourceTag;//tagsIdFloor[0]; // String | Hall tag.
                UUID categoryId = destCategory; // UUID | Category ID
                try {
                    Log.d("DRAW_PATH", "Start drawing the path------------->" + apiInstance);
                    result = apiInstance.categorySearchSubHallTagCategoryIdGet(hallTag, categoryId);
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
                        floorTags.add(0,(ImageView) findViewById(R.id.subhall1));
                        floorTags.add(1,(ImageView) findViewById(R.id.subhall2));
                        floorTags.add(2,(ImageView) findViewById(R.id.subhall3));
                        floorTags.add(3,(ImageView) findViewById(R.id.subhall4));
                        floorTags.add(4,(ImageView) findViewById(R.id.subhall5));
                        floorTags.add(5,(ImageView) findViewById(R.id.subhall6));
                        floorTags.add(6,(ImageView) findViewById(R.id.subhall7));
                        floorTags.add(7,(ImageView) findViewById(R.id.subhall8));
                        floorTags.add(8,(ImageView) findViewById(R.id.subhall9));
                        floorTags.add(9,(ImageView) findViewById(R.id.subhall10));
                        floorTags.add(10,(ImageView) findViewById(R.id.subhall11));
                        floorTags.add(11,(ImageView) findViewById(R.id.subhall12));
                        floorTags.add(12,(ImageView) findViewById(R.id.subhall13));
                        floorTags.add(13,(ImageView) findViewById(R.id.subhall14));
                        floorTags.add(14,(ImageView) findViewById(R.id.subhall15));
                        floorTags.add(15,(ImageView) findViewById(R.id.subhall16));
                        floorTags.add(16,(ImageView) findViewById(R.id.subhall17));
                        floorTags.add(17,(ImageView) findViewById(R.id.subhall18));
                        floorTags.add(18,(ImageView) findViewById(R.id.subhall19));
                        floorTags.add(19,(ImageView) findViewById(R.id.subhall20));


                        //initialize floorTags
                        //floorTags2.add(0,(SurfaceView) findViewById(R.id.surfaceView12));
                        //floorTags2.add(1,(SurfaceView) findViewById(R.id.surfaceView22));
                        //floorTags2.add(2,(SurfaceView) findViewById(R.id.surfaceView32));
                        //floorTags2.add(3,(SurfaceView) findViewById(R.id.surfaceView62));
                        //floorTags2.add(4,(SurfaceView) findViewById(R.id.surfaceView72));

                        for(int i=0; i < tagsIdFloor.length; i++) {
                            mapTags.put(tagsIdFloor[i],floorTags.get(i));

                            //floorTags.get(i).setVisibility(View.INVISIBLE); //all invisible
                            //floorTags.get(i).setVisibility(View.INVISIBLE); //all invisible
                            //floorTags2.get(i).setVisibility(View.INVISIBLE); //all invisible
                        }
                        Log.d("DRAW_PATH","Initialization done");

                        for (int i = 0; i < result.size(); i++) {
                            Log.d("TAG -->", result.get(i).getName());
                            mapTags.get(result.get(i).getName()).setVisibility(View.VISIBLE);
                        }
                    }
                });
            }
        });
        tt.start();

        //reader.stateTag = "5";
        //Log.d("LASTSTATE","-->setting last state"+stateTag);
    }

    @Override
    protected void onStop() {
        unregisterReceiver(mGattUpdateReceiver);
        super.onStop();
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
                    result = apiInstance.categorySearchSubHallTagCategoryIdGet(hallTag, categoryId);
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

                        for(int i=0; i < tagsIdFloor.length; i++) {
                            mapTags.put(tagsIdFloor[i],floorTags.get(i));

                            floorTags.get(i).setVisibility(View.INVISIBLE); //all invisible
                            //floorTags2.get(i).setVisibility(View.INVISIBLE); //all invisible
                        }
                        Log.d("DRAW_PATH","Initialization done");

                        System.out.println("--->"+result);
                        for (int i = 0; i < result.size(); i++) {
                            Log.d("TAG -->", result.get(i).getName());
                            mapTags.get(result.get(i).getName()).setVisibility(View.VISIBLE);
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
            String tag = ""+Integer.parseInt(data);
            Toast.makeText(getApplicationContext(), tag, Toast.LENGTH_SHORT).show();

            //((reader) this.getApplication()).setSomeVariable("foo");
            //reader.a= "a";

            int pos = isTagValid(tag); //if tag is valid, return the tag position
            if(pos != -1 && !tag.equals(stateTag)) {
                pathUpdate(tagsIdFloor[pos]);
                stateTag = tag;

                //set lastState
                reader.stateTag = "5";
                Log.d("LASTSTATE","-->setting last state"+stateTag);
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
        for(int i = 0; i < tagsIdFloor.length; i++){
            if(tagsIdFloor[i].equals(tag))
                return i;
        }
        return -1;
    }

    /*
     * buttons
     */
    public void goBackButton(View abc){
        finish();   //return to the last activity without calling onCreate/onStart/onResume
        //final Intent intent = new Intent(this, reader.class );
        //startActivity(intent);
        //setContentView(R.layout.activity_reader);
    }


}