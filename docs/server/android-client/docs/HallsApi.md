# HallsApi

All URIs are relative to *http://192.168.33.10:8000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hallsContentsHallTagGet**](HallsApi.md#hallsContentsHallTagGet) | **GET** /halls/contents/{hall_tag} | Get the contetns associated with a hall tag
[**hallsDetailsGet**](HallsApi.md#hallsDetailsGet) | **GET** /halls/details | List all the halls in the system
[**hallsDetailsHallTagGet**](HallsApi.md#hallsDetailsHallTagGet) | **GET** /halls/details/{hall_tag} | Details of a hall


<a name="hallsContentsHallTagGet"></a>
# **hallsContentsHallTagGet**
> List&lt;ContentHall&gt; hallsContentsHallTagGet(hallTag)

Get the contetns associated with a hall tag

Given a hall tag get the contents associated in that hall 

### Example
```java
// Import classes:
//import io.swagger.client.api.HallsApi;

HallsApi apiInstance = new HallsApi();
String hallTag = "hallTag_example"; // String | Hall tag.
try {
    List<ContentHall> result = apiInstance.hallsContentsHallTagGet(hallTag);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling HallsApi#hallsContentsHallTagGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hallTag** | **String**| Hall tag. |

### Return type

[**List&lt;ContentHall&gt;**](ContentHall.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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

<a name="hallsDetailsHallTagGet"></a>
# **hallsDetailsHallTagGet**
> Hall hallsDetailsHallTagGet(hallTag)

Details of a hall

The hall details by a tag. 

### Example
```java
// Import classes:
//import io.swagger.client.api.HallsApi;

HallsApi apiInstance = new HallsApi();
String hallTag = "hallTag_example"; // String | Hall tag.
try {
    Hall result = apiInstance.hallsDetailsHallTagGet(hallTag);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling HallsApi#hallsDetailsHallTagGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hallTag** | **String**| Hall tag. |

### Return type

[**Hall**](Hall.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

