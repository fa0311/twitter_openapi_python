# TweetLegacyPlace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounding_box** | [**TweetLegacyPlaceBoundingBox**](TweetLegacyPlaceBoundingBox.md) |  | 
**country** | **str** |  | 
**country_code** | **str** |  | 
**full_name** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**place_type** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_legacy_place import TweetLegacyPlace

# TODO update the JSON string below
json = "{}"
# create an instance of TweetLegacyPlace from a JSON string
tweet_legacy_place_instance = TweetLegacyPlace.from_json(json)
# print the JSON string representation of the object
print(TweetLegacyPlace.to_json())

# convert the object into a dict
tweet_legacy_place_dict = tweet_legacy_place_instance.to_dict()
# create an instance of TweetLegacyPlace from a dict
tweet_legacy_place_from_dict = TweetLegacyPlace.from_dict(tweet_legacy_place_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


