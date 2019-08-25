package com.example.myapplication;


import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.http.Multipart;
import retrofit2.http.POST;
import retrofit2.http.Part;
import retrofit2.http.Body;

public interface DjangoApi {

    String DJANGO_SITE = "http://121.163.61.56:8000/image/";

    @Multipart
    @POST("upload/")
    Call<RequestBody> uploadFile(@Part MultipartBody.Part file);


//    @POST("create/")
//    Call<RequestBody> addPostVoditel(@Body PostModel postModel);

}