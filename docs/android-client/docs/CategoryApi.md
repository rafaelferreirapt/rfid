# CategoryApi

All URIs are relative to *http://rfid.rafaelferreira.pt/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categoryDetailsCategoryIdGet**](CategoryApi.md#categoryDetailsCategoryIdGet) | **GET** /category/details/{category_id}/ | Details of a category
[**categoryDetailsGet**](CategoryApi.md#categoryDetailsGet) | **GET** /category/details/ | List all the categories in the system
[**categoryHallSubHallTagGet**](CategoryApi.md#categoryHallSubHallTagGet) | **GET** /category/hall/{sub_hall_tag}/ | Get categories associated with a hall
[**categorySearchSubHallTagCategoryIdGet**](CategoryApi.md#categorySearchSubHallTagCategoryIdGet) | **GET** /category/search/{sub_hall_tag}/{category_id}/ | Get the path between the hall where the user is and the category that the user wants to go


<a name="categoryDetailsCategoryIdGet"></a>
# **categoryDetailsCategoryIdGet**
> Category categoryDetailsCategoryIdGet(categoryId)

Details of a category

The category details with a category identifier. 

### Example
```java
// Import classes:
//import io.swagger.client.api.CategoryApi;

CategoryApi apiInstance = new CategoryApi();
UUID categoryId = new UUID(); // UUID | Category ID.
try {
    Category result = apiInstance.categoryDetailsCategoryIdGet(categoryId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling CategoryApi#categoryDetailsCategoryIdGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categoryId** | **UUID**| Category ID. |

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="categoryDetailsGet"></a>
# **categoryDetailsGet**
> List&lt;Category&gt; categoryDetailsGet()

List all the categories in the system

This endpoint will display all the categories in the system. Is very important to take care of the \&quot;id\&quot; because that id will be used to request a path to that category. 

### Example
```java
// Import classes:
//import io.swagger.client.api.CategoryApi;

CategoryApi apiInstance = new CategoryApi();
try {
    List<Category> result = apiInstance.categoryDetailsGet();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling CategoryApi#categoryDetailsGet");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Category&gt;**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="categoryHallSubHallTagGet"></a>
# **categoryHallSubHallTagGet**
> List&lt;Category&gt; categoryHallSubHallTagGet(subHallTag)

Get categories associated with a hall

Given a hall tag get the categories associated in that sub hall 

### Example
```java
// Import classes:
//import io.swagger.client.api.CategoryApi;

CategoryApi apiInstance = new CategoryApi();
String subHallTag = "subHallTag_example"; // String | Sub hall tag.
try {
    List<Category> result = apiInstance.categoryHallSubHallTagGet(subHallTag);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling CategoryApi#categoryHallSubHallTagGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subHallTag** | **String**| Sub hall tag. |

### Return type

[**List&lt;Category&gt;**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="categorySearchSubHallTagCategoryIdGet"></a>
# **categorySearchSubHallTagCategoryIdGet**
> List&lt;Hall&gt; categorySearchSubHallTagCategoryIdGet(subHallTag, categoryId)

Get the path between the hall where the user is and the category that the user wants to go



### Example
```java
// Import classes:
//import io.swagger.client.api.CategoryApi;

CategoryApi apiInstance = new CategoryApi();
String subHallTag = "subHallTag_example"; // String | Sub hall tag. This correspondes to 1, 2, or 3 for example.
UUID categoryId = new UUID(); // UUID | Category ID.
try {
    List<Hall> result = apiInstance.categorySearchSubHallTagCategoryIdGet(subHallTag, categoryId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling CategoryApi#categorySearchSubHallTagCategoryIdGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subHallTag** | **String**| Sub hall tag. This correspondes to 1, 2, or 3 for example. |
 **categoryId** | **UUID**| Category ID. |

### Return type

[**List&lt;Hall&gt;**](Hall.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

