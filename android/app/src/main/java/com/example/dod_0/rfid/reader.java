package com.example.dod_0.rfid;

import android.app.Activity;
import android.content.BroadcastReceiver;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.ServiceConnection;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.os.IBinder;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.CheckBox;
import android.widget.ImageView;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.VideoView;
import android.widget.MediaController;
import java.io.InputStream;
import android.widget.Toast;
import android.widget.AdapterView.OnItemSelectedListener;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeoutException;

import io.swagger.client.api.CategoryApi;
import io.swagger.client.api.HallsApi;
import io.swagger.client.model.Category;
import io.swagger.client.ApiException;
import io.swagger.client.model.ContentHall;


public class reader extends  Activity implements OnItemSelectedListener{

    private final String DESCRIP = "Descrição: ";
    private VideoView video;
    private MediaController ctlr;
    private boolean flagState = false;
    private String[] hallArr = {"1A253","1A254","1A255","1A256", "1A257"};

    private CategoryApi categoryApi;
    private HallsApi hallsApi;

    private List<Category> categoriesResult;
    private List<ContentHall>  contentHallResult;
    private List<List<ContentHall>>  contentAllHals = new ArrayList<List<ContentHall>>();
    private CheckBox nfcTag;
    private ArrayAdapter<String> adapter;
    private Spinner spinner;

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
        mDeviceName = intent.getStringExtra(EXTRAS_DEVICE_NAME);
        mDeviceAddress = intent.getStringExtra(EXTRAS_DEVICE_ADDRESS);

        setContentView(R.layout.activity_reader);
        /*
         *
         */
        spinner = (Spinner) findViewById(R.id.spinner);
        //for Callback function
        spinner.setOnItemSelectedListener(this);

        // Create an ArrayAdapter using the string array and a default spinner layout
        //ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this, R.array.planets_array, android.R.layout.simple_spinner_item);
        List<String> categories = new ArrayList<String>();
        categories.add(" ... ");
        categories.add("Massas");
        categories.add("Águas");
        categories.add("Vinhos");
        categories.add("Congelados");
        categories.add("Carnes");


        //ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this, R.array.planets_array, android.R.layout.simple_spinner_item);
        adapter = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, categories);

        // Specify the layout to use when the list of choices appears
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        // Apply the adapter to the spinner
        spinner.setAdapter(adapter);

        String abc = "https://stocklogos-pd.s3.amazonaws.com/styles/logo-medium-alt/smartcart_2.png";
        new DownloadImageTask((ImageView) findViewById(R.id.imageView2)).execute(abc);

        //hide video player
        ((VideoView) findViewById(R.id.videoView5)).setVisibility(View.GONE);
        //hide warning message
        ((TextView) findViewById(R.id.warningText)).setVisibility(View.GONE);
        Thread t_cat = new Thread(new Runnable() {
            @Override
            public void run() {
                categoryApi = new CategoryApi();
                try {
                    Log.d("[Reader]","CategoryAPI Request");
                    categoriesResult = categoryApi.categoryDetailsGet();
                    System.out.println(categoriesResult);
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
        t_cat.start();



        Thread t_cont = new Thread(new Runnable() {
            @Override
            public void run() {
                hallsApi = new HallsApi();
                Log.d("[Reader]","ContentHallAPI Request");
                for(int i = 0; i < hallArr.length; i++) {
                    contentHallResult = null;
                    try {
                        contentHallResult = hallsApi.hallsContentsHallTagGet(hallArr[i]);
                        System.out.println(contentHallResult);

                        if(contentHallResult != null) {
                            contentAllHals.add(i, contentHallResult);
                            System.out.println("------------__>"+i);
                        }
                    } catch (ApiException e) {
                        System.err.println("Exception when calling CategoryApi#categoryHallHallTagGet");
                        e.printStackTrace();
                    } catch (Exception e) {
                        System.err.println("Exception when calling CategoryApi#categoryHallHallTagGet");
                        e.printStackTrace();
                    }

                }
            }
        });
        t_cont.start();


        /*String argument = "video";
        if(argument=="image") {
            String abc = "http://www.hipersuper.pt/wp-content/uploads/2014/12/image005.jpg";
            new DownloadImageTask((ImageView) findViewById(R.id.imageView2)).execute(abc);
        }
        else if(argument=="video")
        {

            String path ="http://sendvid.com/ll5ka8tf.mp4";
            video = (VideoView) findViewById(R.id.videoView4);
            video.setVideoPath(path);
            ctlr = new MediaController(this);
            ctlr.setMediaPlayer(video);
            video.setVisibility(View.VISIBLE);
            video.setMediaController(ctlr);
            video.requestFocus();
            video.start();
        }
        else{
            // tratar erro
        }*/

        nfcTag = (CheckBox)findViewById(R.id.checkBox);
        nfcTag.setChecked(false);
    }

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, final int position, long id) {
        // An item was selected. You can retrieve the selected item using
        //int position = parent.getItemAtPosition(pos);
        Log.d("POSITION: ", ""+position);

        // On selecting a spinner item
        String item = parent.getItemAtPosition(position).toString();

        // Showing selected spinner item
        Toast.makeText(parent.getContext(), "Selected: " + item, Toast.LENGTH_LONG).show();
        Log.d("POSITION: ", ""+position);

        setCategoriesHall(position);


    }
    public void onNothingSelected(AdapterView parent) {
        // Do nothing.
    }

    private void setCategoriesHall(int position)
    {
        Log.d("DEBUG","Setting Categories Hall");

        spinner.setSelection(position);
        //Show description
        if(position != 0) {
            ((TextView) findViewById(R.id.description)).setVisibility(View.VISIBLE);
            ((TextView) findViewById(R.id.description)).setText("" + DESCRIP + "" + categoriesResult.get(position - 1).getDescription());

            if(contentAllHals.get(position-1) == null || contentAllHals.get(position-1).isEmpty()) {
                ((TextView) findViewById(R.id.warningText)).setVisibility(View.VISIBLE);
                ((VideoView) findViewById(R.id.videoView5)).setVisibility(View.GONE);
                ((ImageView) findViewById(R.id.imageView3)).setVisibility(View.GONE);
                ((ImageView) findViewById(R.id.imageView4)).setVisibility(View.GONE);
                ((ImageView) findViewById(R.id.imageView5)).setVisibility(View.GONE);
                ((ImageView) findViewById(R.id.imageView2)).setVisibility(View.GONE);

            } else {
                //display images
                ((ImageView) findViewById(R.id.imageView2)).setVisibility(View.GONE);
                ((VideoView) findViewById(R.id.videoView5)).setVisibility(View.GONE);
                ((TextView) findViewById(R.id.warningText)).setVisibility(View.GONE);
                ((VideoView) findViewById(R.id.videoView5)).setVisibility(View.GONE);
                ((ImageView) findViewById(R.id.imageView3)).setVisibility(View.GONE);
                ((ImageView) findViewById(R.id.imageView4)).setVisibility(View.GONE);
                ((ImageView) findViewById(R.id.imageView5)).setVisibility(View.GONE);

                //display images
                startAllImages(position);

                //display video
                displayVideo(position);
            }
        }else{
            Log.d("POSITION: ", ""+position);
            ((TextView) findViewById(R.id.description)).setVisibility(View.GONE);
            ((TextView) findViewById(R.id.warningText)).setVisibility(View.GONE);
            ((VideoView) findViewById(R.id.videoView5)).setVisibility(View.GONE);
            ((ImageView) findViewById(R.id.imageView3)).setVisibility(View.GONE);
            ((ImageView) findViewById(R.id.imageView4)).setVisibility(View.GONE);
            ((ImageView) findViewById(R.id.imageView5)).setVisibility(View.GONE);
            ((ImageView) findViewById(R.id.imageView2)).setVisibility(View.VISIBLE);
            Log.d("POSITION: ", ""+position);
        }
    }

    private void startAllImages(final int position){
        Log.d("STARTALLIMAGES","Uploading images..."+position);
        Thread t_imag = new Thread(new Runnable() {
            @Override
            public void run() {

                new DownloadImageTask((ImageView) findViewById(R.id.imageView3)).execute(contentAllHals.get(position-1).get(0).getUrl());
                //new DownloadImageTask((ImageView) findViewById(R.id.imageView4)).execute(contentAllHals.get(position-1).get(1).getUrl());
                //new DownloadImageTask((ImageView) findViewById(R.id.imageView5)).execute(contentAllHals.get(position-1).get(2).getUrl());
            }
        });
        t_imag.start();

        Thread t_imag1 = new Thread(new Runnable() {
            @Override
            public void run() {

                //new DownloadImageTask((ImageView) findViewById(R.id.imageView3)).execute(contentAllHals.get(position-1).get(0).getUrl());
                new DownloadImageTask((ImageView) findViewById(R.id.imageView4)).execute(contentAllHals.get(position-1).get(1).getUrl());
                //new DownloadImageTask((ImageView) findViewById(R.id.imageView5)).execute(contentAllHals.get(position-1).get(2).getUrl());
            }
        });
        t_imag1.start();

        Thread t_imag2 = new Thread(new Runnable() {
            @Override
            public void run() {

                //new DownloadImageTask((ImageView) findViewById(R.id.imageView3)).execute(contentAllHals.get(position-1).get(0).getUrl());
                //new DownloadImageTask((ImageView) findViewById(R.id.imageView4)).execute(contentAllHals.get(position-1).get(1).getUrl());
                new DownloadImageTask((ImageView) findViewById(R.id.imageView5)).execute(contentAllHals.get(position-1).get(2).getUrl());
            }
        });
        t_imag2.start();

        ((ImageView) findViewById(R.id.imageView3)).setVisibility(View.VISIBLE);
        ((ImageView) findViewById(R.id.imageView4)).setVisibility(View.VISIBLE);
        ((ImageView) findViewById(R.id.imageView5)).setVisibility(View.VISIBLE);
    }

    private void displayVideo(final int position){
        System.out.println("Uploading video..."+position);
        video = (VideoView) findViewById(R.id.videoView5);
        video.setVisibility(View.VISIBLE);
        video.setZOrderOnTop(true);
        ctlr = new MediaController(this);
        String path = "http://rfid.rafaelferreira.pt"+contentAllHals.get(position-1).get(3).getUrl();
        video.setVideoPath(path);
        ctlr.setMediaPlayer(video);
        video.setVisibility(View.VISIBLE);
        video.setMediaController(ctlr);
        video.requestFocus();
        video.start();

        ((VideoView) findViewById(R.id.videoView5)).setVisibility(View.VISIBLE);
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


            if(nfcTag.isChecked()) {
                //nfcTag.setChecked(false);
                Log.d("CHECKBOX","is activated");
                Toast.makeText(getApplicationContext(), data, Toast.LENGTH_SHORT).show();
                System.out.println(data);
                if(data.equals("3530044544"))
                    setCategoriesHall(1);   //set massas

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


    /*
     * button
     */
    public void setPathButton(View abc){
        Intent intent = new Intent(this, drawPath.class );
        startActivity(intent);
    }
}

