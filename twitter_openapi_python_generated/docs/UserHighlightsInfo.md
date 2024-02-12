# UserHighlightsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_highlight_tweets** | **bool** |  | 
**highlighted_tweets** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_highlights_info import UserHighlightsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserHighlightsInfo from a JSON string
user_highlights_info_instance = UserHighlightsInfo.from_json(json)
# print the JSON string representation of the object
print UserHighlightsInfo.to_json()

# convert the object into a dict
user_highlights_info_dict = user_highlights_info_instance.to_dict()
# create an instance of UserHighlightsInfo from a dict
user_highlights_info_form_dict = user_highlights_info.from_dict(user_highlights_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


