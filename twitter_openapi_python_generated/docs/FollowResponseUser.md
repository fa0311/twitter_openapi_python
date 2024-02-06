# FollowResponseUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**FollowResponseResult**](FollowResponseResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.follow_response_user import FollowResponseUser

# TODO update the JSON string below
json = "{}"
# create an instance of FollowResponseUser from a JSON string
follow_response_user_instance = FollowResponseUser.from_json(json)
# print the JSON string representation of the object
print FollowResponseUser.to_json()

# convert the object into a dict
follow_response_user_dict = follow_response_user_instance.to_dict()
# create an instance of FollowResponseUser from a dict
follow_response_user_form_dict = follow_response_user.from_dict(follow_response_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


