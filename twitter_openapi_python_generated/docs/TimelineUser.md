# TimelineUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**item_type** | [**ContentItemType**](ContentItemType.md) |  | 
**social_context** | [**SocialContextUnion**](SocialContextUnion.md) |  | [optional] 
**user_display_type** | **str** |  | 
**user_results** | [**UserResults**](UserResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_user import TimelineUser

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineUser from a JSON string
timeline_user_instance = TimelineUser.from_json(json)
# print the JSON string representation of the object
print(TimelineUser.to_json())

# convert the object into a dict
timeline_user_dict = timeline_user_instance.to_dict()
# create an instance of TimelineUser from a dict
timeline_user_from_dict = TimelineUser.from_dict(timeline_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


