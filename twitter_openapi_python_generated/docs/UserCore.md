# UserCore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | 
**name** | **str** |  | 
**screen_name** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_core import UserCore

# TODO update the JSON string below
json = "{}"
# create an instance of UserCore from a JSON string
user_core_instance = UserCore.from_json(json)
# print the JSON string representation of the object
print(UserCore.to_json())

# convert the object into a dict
user_core_dict = user_core_instance.to_dict()
# create an instance of UserCore from a dict
user_core_from_dict = UserCore.from_dict(user_core_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


