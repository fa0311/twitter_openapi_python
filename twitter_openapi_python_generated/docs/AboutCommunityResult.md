# AboutCommunityResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**about_timeline** | [**TimelineResult**](TimelineResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.about_community_result import AboutCommunityResult

# TODO update the JSON string below
json = "{}"
# create an instance of AboutCommunityResult from a JSON string
about_community_result_instance = AboutCommunityResult.from_json(json)
# print the JSON string representation of the object
print(AboutCommunityResult.to_json())

# convert the object into a dict
about_community_result_dict = about_community_result_instance.to_dict()
# create an instance of AboutCommunityResult from a dict
about_community_result_from_dict = AboutCommunityResult.from_dict(about_community_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


