# TweetLegacyPlaceBoundingBox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[List[List[float]]]** |  | 
**type** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_legacy_place_bounding_box import TweetLegacyPlaceBoundingBox

# TODO update the JSON string below
json = "{}"
# create an instance of TweetLegacyPlaceBoundingBox from a JSON string
tweet_legacy_place_bounding_box_instance = TweetLegacyPlaceBoundingBox.from_json(json)
# print the JSON string representation of the object
print(TweetLegacyPlaceBoundingBox.to_json())

# convert the object into a dict
tweet_legacy_place_bounding_box_dict = tweet_legacy_place_bounding_box_instance.to_dict()
# create an instance of TweetLegacyPlaceBoundingBox from a dict
tweet_legacy_place_bounding_box_from_dict = TweetLegacyPlaceBoundingBox.from_dict(tweet_legacy_place_bounding_box_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


