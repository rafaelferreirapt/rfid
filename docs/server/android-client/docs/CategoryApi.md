# CategoryApi

All URIs are relative to *http://192.168.33.10:8000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categoryDetailsCategoryIdGet**](CategoryApi.md#categoryDetailsCategoryIdGet) | **GET** /category/details/{category_id} | Details of a category
[**categoryDetailsGet**](CategoryApi.md#categoryDetailsGet) | **GET** /category/details | List all the categories in the system
[**categoryHallHallTagGet**](CategoryApi.md#categoryHallHallTagGet) | **GET** /category/hall/{hall_tag} | Get categories associated with a hall
[**categorySearchHallTagCategoryIdGet**](CategoryApi.md#categorySearchHallTagCategoryIdGet) | **GET** /category/search/{hall_tag}/{category_id} | Get the path between the hall where the user is and the category that the user wants to go


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

This endpoint will display all the categories in the system. Is very important to take care of the \&quot;id\&quot; because that id will be used to  request a path to that category. 

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

<a name="categoryHallHallTagGet"></a>
# **categoryHallHallTagGet**
> List&lt;Category&gt; categoryHallHallTagGet(hallTag)

Get categories associated with a hall

Given a hall tag get the categories associated in that hall 

### Example
```java
// Import classes:
//import io.swagger.client.api.CategoryApi;

CategoryApi apiInstance = new CategoryApi();
String hallTag = "hallTag_example"; // String | Hall tag.
try {
    List<Category> result = apiInstance.categoryHallHallTagGet(hallTag);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling CategoryApi#categoryHallHallTagGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hallTag** | **String**| Hall tag. |

### Return type

[**List&lt;Category&gt;**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="categorySearchHallTagCategoryIdGet"></a>
# **categorySearchHallTagCategoryIdGet**
> List&lt;Hall&gt; categorySearchHallTagCategoryIdGet(hallTag, categoryId)

Get the path between the hall where the user is and the category that the user wants to go



### Example
```java
// Import classes:
//import io.swagger.client.api.CategoryApi;

CategoryApi apiInstance = new CategoryApi();
String hallTag = "hallTag_example"; // String | Hall tag.
UUID categoryId = new UUID(); // UUID | Category ID.
try {
    List<Hall> result = apiInstance.categorySearchHallTagCategoryIdGet(hallTag, categoryId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling CategoryApi#categorySearchHallTagCategoryIdGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hallTag** | **String**| Hall tag. |
 **categoryId** | **UUID**| Category ID. |

### Return type

[**List&lt;Hall&gt;**](Hall.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

