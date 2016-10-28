# HallsApi

All URIs are relative to *http://rfid.rafaelferreira.pt/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hallsDetailsGet**](HallsApi.md#hallsDetailsGet) | **GET** /halls/details/ | List all the halls in the system
[**hallsDetailsHallNameGet**](HallsApi.md#hallsDetailsHallNameGet) | **GET** /halls/details/{hall_name}/ | Details of a hall
[**hallsSubHallsContentsSubHallTagGet**](HallsApi.md#hallsSubHallsContentsSubHallTagGet) | **GET** /halls/sub_halls/contents/{sub_hall_tag}/ | Get the contetns associated with a sub hall tag


<a name="hallsDetailsGet"></a>
# **hallsDetailsGet**
> List&lt;Hall&gt; hallsDetailsGet()

List all the halls in the system

This endpoint will display all the halls in the system. 

### Example
```java
// Import classes:
//import io.swagger.client.api.HallsApi;

HallsApi apiInstance = new HallsApi();
try {
    List<Hall> result = apiInstance.hallsDetailsGet();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling HallsApi#hallsDetailsGet");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Hall&gt;**](Hall.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="hallsDetailsHallNameGet"></a>
# **hallsDetailsHallNameGet**
> Hall hallsDetailsHallNameGet(hallName)

Details of a hall

The hall details by a tag. 

### Example
```java
// Import classes:
//import io.swagger.client.api.HallsApi;

HallsApi apiInstance = new HallsApi();
String hallName = "hallName_example"; // String | Hall name.
try {
    Hall result = apiInstance.hallsDetailsHallNameGet(hallName);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling HallsApi#hallsDetailsHallNameGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hallName** | **String**| Hall name. |

### Return type

[**Hall**](Hall.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="hallsSubHallsContentsSubHallTagGet"></a>
# **hallsSubHallsContentsSubHallTagGet**
> List&lt;ContentHall&gt; hallsSubHallsContentsSubHallTagGet(subHallTag)

Get the contetns associated with a sub hall tag

Given a hall tag get the contents associated in that sub hall 

### Example
```java
// Import classes:
//import io.swagger.client.api.HallsApi;

HallsApi apiInstance = new HallsApi();
String subHallTag = "subHallTag_example"; // String | Sub Hall tag.
try {
    List<ContentHall> result = apiInstance.hallsSubHallsContentsSubHallTagGet(subHallTag);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling HallsApi#hallsSubHallsContentsSubHallTagGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subHallTag** | **String**| Sub Hall tag. |

### Return type

[**List&lt;ContentHall&gt;**](ContentHall.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

