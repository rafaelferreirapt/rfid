/**
 * RFID
 * Move into halls in the shopping
 *
 * OpenAPI spec version: 1.0.0
 *
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package io.swagger.client.api;

import io.swagger.client.ApiInvoker;
import io.swagger.client.ApiException;
import io.swagger.client.Pair;

import io.swagger.client.model.*;

import java.util.*;

import com.android.volley.Response;
import com.android.volley.VolleyError;

import io.swagger.client.model.Category;
import io.swagger.client.model.Error;
import java.util.UUID;
import io.swagger.client.model.Hall;

import org.apache.http.HttpEntity;
import org.apache.http.entity.mime.MultipartEntityBuilder;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeoutException;

public class CategoryApi {
  String basePath = "http://rfid.rafaelferreira.pt/api/v1";

    public CategoryApi(){
        ApiInvoker.initializeInstance();
        apiInvoker = ApiInvoker.getInstance();
    }

    ApiInvoker apiInvoker;

  public void addHeader(String key, String value) {
    getInvoker().addDefaultHeader(key, value);
  }

  public ApiInvoker getInvoker() {
    return apiInvoker;
  }

  public void setBasePath(String basePath) {
    this.basePath = basePath;
  }

  public String getBasePath() {
    return basePath;
  }

  /**
  * Details of a category
  * The category details with a category identifier.
   * @param categoryId Category ID.
   * @return Category
  */
  public Category categoryDetailsCategoryIdGet (UUID categoryId) throws TimeoutException, ExecutionException, InterruptedException, ApiException {
     Object postBody = null;

      // verify the required parameter 'categoryId' is set
      if (categoryId == null) {
      VolleyError error = new VolleyError("Missing the required parameter 'categoryId' when calling categoryDetailsCategoryIdGet",
      new ApiException(400, "Missing the required parameter 'categoryId' when calling categoryDetailsCategoryIdGet"));
      }


  // create path and map variables
  String path = "/category/details/{category_id}/".replaceAll("\\{format\\}","json").replaceAll("\\{" + "category_id" + "\\}", apiInvoker.escapeString(categoryId.toString()));

  // query params
  List<Pair> queryParams = new ArrayList<Pair>();
      // header params
      Map<String, String> headerParams = new HashMap<String, String>();
      // form params
      Map<String, String> formParams = new HashMap<String, String>();



      String[] contentTypes = {

      };
      String contentType = contentTypes.length > 0 ? contentTypes[0] : "application/json";

      if (contentType.startsWith("multipart/form-data")) {
      // file uploading
      MultipartEntityBuilder localVarBuilder = MultipartEntityBuilder.create();


      HttpEntity httpEntity = localVarBuilder.build();
      postBody = httpEntity;
      } else {
      // normal form params
        }

      String[] authNames = new String[] {  };

      try {
        String localVarResponse = apiInvoker.invokeAPI (basePath, path, "GET", queryParams, postBody, headerParams, formParams, contentType, authNames);
        if(localVarResponse != null){
           return (Category) ApiInvoker.deserialize(localVarResponse, "", Category.class);
        } else {
           return null;
        }
      } catch (ApiException ex) {
         throw ex;
      } catch (InterruptedException ex) {
         throw ex;
      } catch (ExecutionException ex) {
         if(ex.getCause() instanceof VolleyError) {
	    VolleyError volleyError = (VolleyError)ex.getCause();
	    if (volleyError.networkResponse != null) {
	       throw new ApiException(volleyError.networkResponse.statusCode, volleyError.getMessage());
	    }
         }
         throw ex;
      } catch (TimeoutException ex) {
         throw ex;
      }
  }

      /**
   * Details of a category
   * The category details with a category identifier.
   * @param categoryId Category ID.
  */
  public void categoryDetailsCategoryIdGet (UUID categoryId, final Response.Listener<Category> responseListener, final Response.ErrorListener errorListener) {
    Object postBody = null;


    // verify the required parameter 'categoryId' is set
    if (categoryId == null) {
       VolleyError error = new VolleyError("Missing the required parameter 'categoryId' when calling categoryDetailsCategoryIdGet",
         new ApiException(400, "Missing the required parameter 'categoryId' when calling categoryDetailsCategoryIdGet"));
    }


    // create path and map variables
    String path = "/category/details/{category_id}/".replaceAll("\\{format\\}","json").replaceAll("\\{" + "category_id" + "\\}", apiInvoker.escapeString(categoryId.toString()));

    // query params
    List<Pair> queryParams = new ArrayList<Pair>();
    // header params
    Map<String, String> headerParams = new HashMap<String, String>();
    // form params
    Map<String, String> formParams = new HashMap<String, String>();



    String[] contentTypes = {

    };
    String contentType = contentTypes.length > 0 ? contentTypes[0] : "application/json";

    if (contentType.startsWith("multipart/form-data")) {
      // file uploading
      MultipartEntityBuilder localVarBuilder = MultipartEntityBuilder.create();


      HttpEntity httpEntity = localVarBuilder.build();
      postBody = httpEntity;
    } else {
      // normal form params
          }

      String[] authNames = new String[] {  };

    try {
      apiInvoker.invokeAPI(basePath, path, "GET", queryParams, postBody, headerParams, formParams, contentType, authNames,
        new Response.Listener<String>() {
          @Override
          public void onResponse(String localVarResponse) {
            try {
              responseListener.onResponse((Category) ApiInvoker.deserialize(localVarResponse,  "", Category.class));
            } catch (ApiException exception) {
               errorListener.onErrorResponse(new VolleyError(exception));
            }
          }
      }, new Response.ErrorListener() {
          @Override
          public void onErrorResponse(VolleyError error) {
            errorListener.onErrorResponse(error);
          }
      });
    } catch (ApiException ex) {
      errorListener.onErrorResponse(new VolleyError(ex));
    }
  }
  /**
  * List all the categories in the system
  * This endpoint will display all the categories in the system. Is very important to take care of the \&quot;id\&quot; because that id will be used to request a path to that category.
   * @return List<Category>
  */
  public List<Category> categoryDetailsGet () throws TimeoutException, ExecutionException, InterruptedException, ApiException {
     Object postBody = null;


  // create path and map variables
  String path = "/category/details/".replaceAll("\\{format\\}","json");

  // query params
  List<Pair> queryParams = new ArrayList<Pair>();
      // header params
      Map<String, String> headerParams = new HashMap<String, String>();
      // form params
      Map<String, String> formParams = new HashMap<String, String>();



      String[] contentTypes = {

      };
      String contentType = contentTypes.length > 0 ? contentTypes[0] : "application/json";

      if (contentType.startsWith("multipart/form-data")) {
      // file uploading
      MultipartEntityBuilder localVarBuilder = MultipartEntityBuilder.create();


      HttpEntity httpEntity = localVarBuilder.build();
      postBody = httpEntity;
      } else {
      // normal form params
        }

      String[] authNames = new String[] {  };

      try {
        String localVarResponse = apiInvoker.invokeAPI (basePath, path, "GET", queryParams, postBody, headerParams, formParams, contentType, authNames);
        if(localVarResponse != null){
           return (List<Category>) ApiInvoker.deserialize(localVarResponse, "array", Category.class);
        } else {
           return null;
        }
      } catch (ApiException ex) {
         throw ex;
      } catch (InterruptedException ex) {
         throw ex;
      } catch (ExecutionException ex) {
         if(ex.getCause() instanceof VolleyError) {
	    VolleyError volleyError = (VolleyError)ex.getCause();
	    if (volleyError.networkResponse != null) {
	       throw new ApiException(volleyError.networkResponse.statusCode, volleyError.getMessage());
	    }
         }
         throw ex;
      } catch (TimeoutException ex) {
         throw ex;
      }
  }

      /**
   * List all the categories in the system
   * This endpoint will display all the categories in the system. Is very important to take care of the \&quot;id\&quot; because that id will be used to request a path to that category.

  */
  public void categoryDetailsGet (final Response.Listener<List<Category>> responseListener, final Response.ErrorListener errorListener) {
    Object postBody = null;



    // create path and map variables
    String path = "/category/details/".replaceAll("\\{format\\}","json");

    // query params
    List<Pair> queryParams = new ArrayList<Pair>();
    // header params
    Map<String, String> headerParams = new HashMap<String, String>();
    // form params
    Map<String, String> formParams = new HashMap<String, String>();



    String[] contentTypes = {

    };
    String contentType = contentTypes.length > 0 ? contentTypes[0] : "application/json";

    if (contentType.startsWith("multipart/form-data")) {
      // file uploading
      MultipartEntityBuilder localVarBuilder = MultipartEntityBuilder.create();


      HttpEntity httpEntity = localVarBuilder.build();
      postBody = httpEntity;
    } else {
      // normal form params
          }

      String[] authNames = new String[] {  };

    try {
      apiInvoker.invokeAPI(basePath, path, "GET", queryParams, postBody, headerParams, formParams, contentType, authNames,
        new Response.Listener<String>() {
          @Override
          public void onResponse(String localVarResponse) {
            try {
              responseListener.onResponse((List<Category>) ApiInvoker.deserialize(localVarResponse,  "array", Category.class));
            } catch (ApiException exception) {
               errorListener.onErrorResponse(new VolleyError(exception));
            }
          }
      }, new Response.ErrorListener() {
          @Override
          public void onErrorResponse(VolleyError error) {
            errorListener.onErrorResponse(error);
          }
      });
    } catch (ApiException ex) {
      errorListener.onErrorResponse(new VolleyError(ex));
    }
  }
  /**
  * Get categories associated with a hall
  * Given a hall tag get the categories associated in that sub hall
   * @param subHallTag Sub hall tag.
   * @return List<Category>
  */
  public List<Category> categoryHallSubHallTagGet (String subHallTag) throws TimeoutException, ExecutionException, InterruptedException, ApiException {
     Object postBody = null;

      // verify the required parameter 'subHallTag' is set
      if (subHallTag == null) {
      VolleyError error = new VolleyError("Missing the required parameter 'subHallTag' when calling categoryHallSubHallTagGet",
      new ApiException(400, "Missing the required parameter 'subHallTag' when calling categoryHallSubHallTagGet"));
      }


  // create path and map variables
  String path = "/category/hall/{sub_hall_tag}/".replaceAll("\\{format\\}","json").replaceAll("\\{" + "sub_hall_tag" + "\\}", apiInvoker.escapeString(subHallTag.toString()));

  // query params
  List<Pair> queryParams = new ArrayList<Pair>();
      // header params
      Map<String, String> headerParams = new HashMap<String, String>();
      // form params
      Map<String, String> formParams = new HashMap<String, String>();



      String[] contentTypes = {

      };
      String contentType = contentTypes.length > 0 ? contentTypes[0] : "application/json";

      if (contentType.startsWith("multipart/form-data")) {
      // file uploading
      MultipartEntityBuilder localVarBuilder = MultipartEntityBuilder.create();


      HttpEntity httpEntity = localVarBuilder.build();
      postBody = httpEntity;
      } else {
      // normal form params
        }

      String[] authNames = new String[] {  };

      try {
        String localVarResponse = apiInvoker.invokeAPI (basePath, path, "GET", queryParams, postBody, headerParams, formParams, contentType, authNames);
        if(localVarResponse != null){
           return (List<Category>) ApiInvoker.deserialize(localVarResponse, "array", Category.class);
        } else {
           return null;
        }
      } catch (ApiException ex) {
         throw ex;
      } catch (InterruptedException ex) {
         throw ex;
      } catch (ExecutionException ex) {
         if(ex.getCause() instanceof VolleyError) {
	    VolleyError volleyError = (VolleyError)ex.getCause();
	    if (volleyError.networkResponse != null) {
	       throw new ApiException(volleyError.networkResponse.statusCode, volleyError.getMessage());
	    }
         }
         throw ex;
      } catch (TimeoutException ex) {
         throw ex;
      }
  }

      /**
   * Get categories associated with a hall
   * Given a hall tag get the categories associated in that sub hall
   * @param subHallTag Sub hall tag.
  */
  public void categoryHallSubHallTagGet (String subHallTag, final Response.Listener<List<Category>> responseListener, final Response.ErrorListener errorListener) {
    Object postBody = null;


    // verify the required parameter 'subHallTag' is set
    if (subHallTag == null) {
       VolleyError error = new VolleyError("Missing the required parameter 'subHallTag' when calling categoryHallSubHallTagGet",
         new ApiException(400, "Missing the required parameter 'subHallTag' when calling categoryHallSubHallTagGet"));
    }


    // create path and map variables
    String path = "/category/hall/{sub_hall_tag}/".replaceAll("\\{format\\}","json").replaceAll("\\{" + "sub_hall_tag" + "\\}", apiInvoker.escapeString(subHallTag.toString()));

    // query params
    List<Pair> queryParams = new ArrayList<Pair>();
    // header params
    Map<String, String> headerParams = new HashMap<String, String>();
    // form params
    Map<String, String> formParams = new HashMap<String, String>();



    String[] contentTypes = {

    };
    String contentType = contentTypes.length > 0 ? contentTypes[0] : "application/json";

    if (contentType.startsWith("multipart/form-data")) {
      // file uploading
      MultipartEntityBuilder localVarBuilder = MultipartEntityBuilder.create();


      HttpEntity httpEntity = localVarBuilder.build();
      postBody = httpEntity;
    } else {
      // normal form params
          }

      String[] authNames = new String[] {  };

    try {
      apiInvoker.invokeAPI(basePath, path, "GET", queryParams, postBody, headerParams, formParams, contentType, authNames,
        new Response.Listener<String>() {
          @Override
          public void onResponse(String localVarResponse) {
            try {
              responseListener.onResponse((List<Category>) ApiInvoker.deserialize(localVarResponse,  "array", Category.class));
            } catch (ApiException exception) {
               errorListener.onErrorResponse(new VolleyError(exception));
            }
          }
      }, new Response.ErrorListener() {
          @Override
          public void onErrorResponse(VolleyError error) {
            errorListener.onErrorResponse(error);
          }
      });
    } catch (ApiException ex) {
      errorListener.onErrorResponse(new VolleyError(ex));
    }
  }
  /**
  * Get the path between the hall where the user is and the category that the user wants to go
  *
   * @param subHallTag Sub hall tag. This correspondes to 1, 2, or 3 for example.
   * @param categoryId Category ID.
   * @return List<Hall>
  */
  public List<Hall> categorySearchSubHallTagCategoryIdGet (String subHallTag, UUID categoryId) throws TimeoutException, ExecutionException, InterruptedException, ApiException {
     Object postBody = null;

      // verify the required parameter 'subHallTag' is set
      if (subHallTag == null) {
      VolleyError error = new VolleyError("Missing the required parameter 'subHallTag' when calling categorySearchSubHallTagCategoryIdGet",
      new ApiException(400, "Missing the required parameter 'subHallTag' when calling categorySearchSubHallTagCategoryIdGet"));
      }

      // verify the required parameter 'categoryId' is set
      if (categoryId == null) {
      VolleyError error = new VolleyError("Missing the required parameter 'categoryId' when calling categorySearchSubHallTagCategoryIdGet",
      new ApiException(400, "Missing the required parameter 'categoryId' when calling categorySearchSubHallTagCategoryIdGet"));
      }


  // create path and map variables
  String path = "/category/search/{sub_hall_tag}/{category_id}/".replaceAll("\\{format\\}","json").replaceAll("\\{" + "sub_hall_tag" + "\\}", apiInvoker.escapeString(subHallTag.toString())).replaceAll("\\{" + "category_id" + "\\}", apiInvoker.escapeString(categoryId.toString()));

  // query params
  List<Pair> queryParams = new ArrayList<Pair>();
      // header params
      Map<String, String> headerParams = new HashMap<String, String>();
      // form params
      Map<String, String> formParams = new HashMap<String, String>();



      String[] contentTypes = {

      };
      String contentType = contentTypes.length > 0 ? contentTypes[0] : "application/json";

      if (contentType.startsWith("multipart/form-data")) {
      // file uploading
      MultipartEntityBuilder localVarBuilder = MultipartEntityBuilder.create();


      HttpEntity httpEntity = localVarBuilder.build();
      postBody = httpEntity;
      } else {
      // normal form params
        }

      String[] authNames = new String[] {  };

      try {
        String localVarResponse = apiInvoker.invokeAPI (basePath, path, "GET", queryParams, postBody, headerParams, formParams, contentType, authNames);
        if(localVarResponse != null){
           return (List<Hall>) ApiInvoker.deserialize(localVarResponse, "array", Hall.class);
        } else {
           return null;
        }
      } catch (ApiException ex) {
         throw ex;
      } catch (InterruptedException ex) {
         throw ex;
      } catch (ExecutionException ex) {
         if(ex.getCause() instanceof VolleyError) {
	    VolleyError volleyError = (VolleyError)ex.getCause();
	    if (volleyError.networkResponse != null) {
	       throw new ApiException(volleyError.networkResponse.statusCode, volleyError.getMessage());
	    }
         }
         throw ex;
      } catch (TimeoutException ex) {
         throw ex;
      }
  }

      /**
   * Get the path between the hall where the user is and the category that the user wants to go
   *
   * @param subHallTag Sub hall tag. This correspondes to 1, 2, or 3 for example.   * @param categoryId Category ID.
  */
  public void categorySearchSubHallTagCategoryIdGet (String subHallTag, UUID categoryId, final Response.Listener<List<Hall>> responseListener, final Response.ErrorListener errorListener) {
    Object postBody = null;


    // verify the required parameter 'subHallTag' is set
    if (subHallTag == null) {
       VolleyError error = new VolleyError("Missing the required parameter 'subHallTag' when calling categorySearchSubHallTagCategoryIdGet",
         new ApiException(400, "Missing the required parameter 'subHallTag' when calling categorySearchSubHallTagCategoryIdGet"));
    }

    // verify the required parameter 'categoryId' is set
    if (categoryId == null) {
       VolleyError error = new VolleyError("Missing the required parameter 'categoryId' when calling categorySearchSubHallTagCategoryIdGet",
         new ApiException(400, "Missing the required parameter 'categoryId' when calling categorySearchSubHallTagCategoryIdGet"));
    }


    // create path and map variables
    String path = "/category/search/{sub_hall_tag}/{category_id}/".replaceAll("\\{format\\}","json").replaceAll("\\{" + "sub_hall_tag" + "\\}", apiInvoker.escapeString(subHallTag.toString())).replaceAll("\\{" + "category_id" + "\\}", apiInvoker.escapeString(categoryId.toString()));

    // query params
    List<Pair> queryParams = new ArrayList<Pair>();
    // header params
    Map<String, String> headerParams = new HashMap<String, String>();
    // form params
    Map<String, String> formParams = new HashMap<String, String>();



    String[] contentTypes = {

    };
    String contentType = contentTypes.length > 0 ? contentTypes[0] : "application/json";

    if (contentType.startsWith("multipart/form-data")) {
      // file uploading
      MultipartEntityBuilder localVarBuilder = MultipartEntityBuilder.create();


      HttpEntity httpEntity = localVarBuilder.build();
      postBody = httpEntity;
    } else {
      // normal form params
          }

      String[] authNames = new String[] {  };

    try {
      apiInvoker.invokeAPI(basePath, path, "GET", queryParams, postBody, headerParams, formParams, contentType, authNames,
        new Response.Listener<String>() {
          @Override
          public void onResponse(String localVarResponse) {
            try {
              responseListener.onResponse((List<Hall>) ApiInvoker.deserialize(localVarResponse,  "array", Hall.class));
            } catch (ApiException exception) {
               errorListener.onErrorResponse(new VolleyError(exception));
            }
          }
      }, new Response.ErrorListener() {
          @Override
          public void onErrorResponse(VolleyError error) {
            errorListener.onErrorResponse(error);
          }
      });
    } catch (ApiException ex) {
      errorListener.onErrorResponse(new VolleyError(ex));
    }
  }
}
