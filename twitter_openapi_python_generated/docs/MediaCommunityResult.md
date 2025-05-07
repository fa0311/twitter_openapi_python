# MediaCommunityResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**community_media_timeline** | [**TimelineResult**](TimelineResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.media_community_result import MediaCommunityResult

# TODO update the JSON string below
json = "{}"
# create an instance of MediaCommunityResult from a JSON string
media_community_result_instance = MediaCommunityResult.from_json(json)
# print the JSON string representation of the object
print(MediaCommunityResult.to_json())

# convert the object into a dict
media_community_result_dict = media_community_result_instance.to_dict()
# create an instance of MediaCommunityResult from a dict
media_community_result_from_dict = MediaCommunityResult.from_dict(media_community_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


