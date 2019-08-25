package com.example.myapplication;

import android.os.Environment;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import java.io.File;

import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
//        Button button = (Button)findViewById(R.id.button);
//        View.OnClickListener listener = new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                uploadFoto();
//            }
//        };
//        button.setOnClickListener(listener);

        uploadFoto();
    }

//    public void AddPostServer() {
//
//        Retrofit retrofit = new Retrofit.Builder()
//                .baseUrl(DjangoApi.DJANGO_SITE)
//                .addConverterFactory(GsonConverterFactory.create())
//                .build();
//
//        DjangoApi postApi= retrofit.create(DjangoApi.class);
//
//
//        PostModel postModel = new PostModel(
//                "android title",
//                "android text"
//        );
//
//
//        Call<RequestBody> call = postApi.addPostVoditel(postModel);
//
//        call.enqueue(new Callback<RequestBody>() {
//            @Override
//            public void onResponse(Call<RequestBody> call, Response<RequestBody> response) {
//                Log.d("good", "good");
//            }
//            @Override
//            public void onFailure(Call<RequestBody> call, Throwable t) {
//                Log.d("fail", "fail");
//            }
//        });
//
//    }
    private void uploadFoto() {

        String image_path = "/storage/emulated/0/download/11.jpg";
        File imageFile = new File(image_path);
        Log.d("isFile : ", "" + imageFile.isFile());

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl(DjangoApi.DJANGO_SITE)
                .addConverterFactory(GsonConverterFactory.create())
                .build();


        DjangoApi postApi= retrofit.create(DjangoApi.class);

        RequestBody requestBody = RequestBody.create(MediaType.parse("multipart/data"), imageFile);

        MultipartBody.Part multiPartBody = MultipartBody.Part
                .createFormData("model_pic", imageFile.getName(), requestBody);

        Log.d("multiPartBody : ", "" + multiPartBody.headers());

        Call<RequestBody> call = postApi.uploadFile(multiPartBody);

        Log.d("Call", "" + call.request());

        call.enqueue(new Callback<RequestBody>() {
            @Override
            public void onResponse(Call<RequestBody> call, Response<RequestBody> response) {
                Log.d("good", "good");
            }

            @Override
            public void onFailure(Call<RequestBody> call, Throwable t) {
                Log.d("fail", "fail" + t);
            }
        });


    }


}
