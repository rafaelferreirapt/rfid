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

package io.swagger.client.model;


import io.swagger.annotations.*;
import com.google.gson.annotations.SerializedName;


@ApiModel(description = "")
public class ContentHall  {
  
  @SerializedName("media")
  private String media = null;
  @SerializedName("url")
  private String url = null;

  /**
   * Can be \"image\" or \"video\"
   **/
  @ApiModelProperty(value = "Can be \"image\" or \"video\"")
  public String getMedia() {
    return media;
  }
  public void setMedia(String media) {
    this.media = media;
  }

  /**
   * The url of the image or the link of youtube video
   **/
  @ApiModelProperty(value = "The url of the image or the link of youtube video")
  public String getUrl() {
    return url;
  }
  public void setUrl(String url) {
    this.url = url;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ContentHall contentHall = (ContentHall) o;
    return (media == null ? contentHall.media == null : media.equals(contentHall.media)) &&
        (url == null ? contentHall.url == null : url.equals(contentHall.url));
  }

  @Override
  public int hashCode() {
    int result = 17;
    result = 31 * result + (media == null ? 0: media.hashCode());
    result = 31 * result + (url == null ? 0: url.hashCode());
    return result;
  }

  @Override
  public String toString()  {
    StringBuilder sb = new StringBuilder();
    sb.append("class ContentHall {\n");
    
    sb.append("  media: ").append(media).append("\n");
    sb.append("  url: ").append(url).append("\n");
    sb.append("}\n");
    return sb.toString();
  }
}