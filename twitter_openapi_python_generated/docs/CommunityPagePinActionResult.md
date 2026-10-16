# CommunityPagePinActionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_community_tweet_pin_action_result** | **str** |  | 
**typename** | [**TypeName**](TypeName.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_page_pin_action_result import CommunityPagePinActionResult

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityPagePinActionResult from a JSON string
community_page_pin_action_result_instance = CommunityPagePinActionResult.from_json(json)
# print the JSON string representation of the object
print(CommunityPagePinActionResult.to_json())

# convert the object into a dict
community_page_pin_action_result_dict = community_page_pin_action_result_instance.to_dict()
# create an instance of CommunityPagePinActionResult from a dict
community_page_pin_action_result_from_dict = CommunityPagePinActionResult.from_dict(community_page_pin_action_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


