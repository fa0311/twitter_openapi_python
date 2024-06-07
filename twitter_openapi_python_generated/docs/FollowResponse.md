# FollowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FollowResponseData**](FollowResponseData.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.follow_response import FollowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FollowResponse from a JSON string
follow_response_instance = FollowResponse.from_json(json)
# print the JSON string representation of the object
print(FollowResponse.to_json())

# convert the object into a dict
follow_response_dict = follow_response_instance.to_dict()
# create an instance of FollowResponse from a dict
follow_response_from_dict = FollowResponse.from_dict(follow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


