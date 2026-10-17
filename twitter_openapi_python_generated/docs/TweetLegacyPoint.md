# TweetLegacyPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[float]** |  | 
**type** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_legacy_point import TweetLegacyPoint

# TODO update the JSON string below
json = "{}"
# create an instance of TweetLegacyPoint from a JSON string
tweet_legacy_point_instance = TweetLegacyPoint.from_json(json)
# print the JSON string representation of the object
print(TweetLegacyPoint.to_json())

# convert the object into a dict
tweet_legacy_point_dict = tweet_legacy_point_instance.to_dict()
# create an instance of TweetLegacyPoint from a dict
tweet_legacy_point_from_dict = TweetLegacyPoint.from_dict(tweet_legacy_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


