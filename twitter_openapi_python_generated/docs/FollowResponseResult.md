# FollowResponseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**timeline** | [**FollowTimeline**](FollowTimeline.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.follow_response_result import FollowResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of FollowResponseResult from a JSON string
follow_response_result_instance = FollowResponseResult.from_json(json)
# print the JSON string representation of the object
print FollowResponseResult.to_json()

# convert the object into a dict
follow_response_result_dict = follow_response_result_instance.to_dict()
# create an instance of FollowResponseResult from a dict
follow_response_result_form_dict = follow_response_result.from_dict(follow_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


