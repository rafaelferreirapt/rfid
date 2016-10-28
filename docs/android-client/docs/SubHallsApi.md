# SubHallsApi

All URIs are relative to *http://rfid.rafaelferreira.pt/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hallsSubHallsDetailsGet**](SubHallsApi.md#hallsSubHallsDetailsGet) | **GET** /halls/sub_halls/details/ | List all the sub halls in the system
[**hallsSubHallsDetailsSubHallNameGet**](SubHallsApi.md#hallsSubHallsDetailsSubHallNameGet) | **GET** /halls/sub_halls/details/{sub_hall_name}/ | Details of a sub hall


<a name="hallsSubHallsDetailsGet"></a>
# **hallsSubHallsDetailsGet**
> List&lt;SubHall&gt; hallsSubHallsDetailsGet()

List all the sub halls in the system

This endpoint will display all the sub halls in the system. 

### Example
```java
// Import classes:
//import io.swagger.client.api.SubHallsApi;

SubHallsApi apiInstance = new SubHallsApi();
try {
    List<SubHall> result = apiInstance.hallsSubHallsDetailsGet();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling SubHallsApi#hallsSubHallsDetailsGet");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;SubHall&gt;**](SubHall.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="hallsSubHallsDetailsSubHallNameGet"></a>
# **hallsSubHallsDetailsSubHallNameGet**
> SubHall hallsSubHallsDetailsSubHallNameGet(subHallName)

Details of a sub hall

The sub hall details by a tag. 

### Example
```java
// Import classes:
//import io.swagger.client.api.SubHallsApi;

SubHallsApi apiInstance = new SubHallsApi();
String subHallName = "subHallName_example"; // String | Sub hall name.
try {
    SubHall result = apiInstance.hallsSubHallsDetailsSubHallNameGet(subHallName);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling SubHallsApi#hallsSubHallsDetailsSubHallNameGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subHallName** | **String**| Sub hall name. |

### Return type

[**SubHall**](SubHall.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

