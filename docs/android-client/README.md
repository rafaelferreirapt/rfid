# swagger-android-client

## Requirements

Building the API client library requires [Maven](https://maven.apache.org/) to be installed.

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn deploy
```

Refer to the [official documentation](https://maven.apache.org/plugins/maven-deploy-plugin/usage.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
    <groupId>io.swagger</groupId>
    <artifactId>swagger-android-client</artifactId>
    <version>1.0.0</version>
    <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
compile "io.swagger:swagger-android-client:1.0.0"
```

### Others

At first generate the JAR by executing:

    mvn package

Then manually install the following JARs:

* target/swagger-android-client-1.0.0.jar
* target/lib/*.jar

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

import io.swagger.client.api.CategoryApi;

public class CategoryApiExample {

    public static void main(String[] args) {
        CategoryApi apiInstance = new CategoryApi();
        UUID categoryId = new UUID(); // UUID | Category ID.
        try {
            Category result = apiInstance.categoryDetailsCategoryIdGet(categoryId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CategoryApi#categoryDetailsCategoryIdGet");
            e.printStackTrace();
        }
    }
}

```

## Documentation for API Endpoints

All URIs are relative to *http://rfid.rafaelferreira.pt/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CategoryApi* | [**categoryDetailsCategoryIdGet**](docs/CategoryApi.md#categoryDetailsCategoryIdGet) | **GET** /category/details/{category_id}/ | Details of a category
*CategoryApi* | [**categoryDetailsGet**](docs/CategoryApi.md#categoryDetailsGet) | **GET** /category/details/ | List all the categories in the system
*CategoryApi* | [**categoryHallHallTagGet**](docs/CategoryApi.md#categoryHallHallTagGet) | **GET** /category/hall/{hall_tag}/ | Get categories associated with a hall
*CategoryApi* | [**categorySearchHallTagCategoryIdGet**](docs/CategoryApi.md#categorySearchHallTagCategoryIdGet) | **GET** /category/search/{hall_tag}/{category_id}/ | Get the path between the hall where the user is and the category that the user wants to go
*HallsApi* | [**hallsContentsHallTagGet**](docs/HallsApi.md#hallsContentsHallTagGet) | **GET** /halls/contents/{hall_tag}/ | Get the contetns associated with a hall tag
*HallsApi* | [**hallsDetailsGet**](docs/HallsApi.md#hallsDetailsGet) | **GET** /halls/details/ | List all the halls in the system
*HallsApi* | [**hallsDetailsHallTagGet**](docs/HallsApi.md#hallsDetailsHallTagGet) | **GET** /halls/details/{hall_tag}/ | Details of a hall


## Documentation for Models

 - [Category](docs/Category.md)
 - [ContentHall](docs/ContentHall.md)
 - [Error](docs/Error.md)
 - [Hall](docs/Hall.md)


## Documentation for Authorization

All endpoints do not require authorization.
Authentication schemes defined for the API:

## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issue.

## Author



