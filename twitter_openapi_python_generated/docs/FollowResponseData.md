# FollowResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**FollowResponseUser**](FollowResponseUser.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.follow_response_data import FollowResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of FollowResponseData from a JSON string
follow_response_data_instance = FollowResponseData.from_json(json)
# print the JSON string representation of the object
print FollowResponseData.to_json()

# convert the object into a dict
follow_response_data_dict = follow_response_data_instance.to_dict()
# create an instance of FollowResponseData from a dict
follow_response_data_form_dict = follow_response_data.from_dict(follow_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


