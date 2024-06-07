# UserUnavailable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**message** | **str** |  | [optional] 
**reason** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_unavailable import UserUnavailable

# TODO update the JSON string below
json = "{}"
# create an instance of UserUnavailable from a JSON string
user_unavailable_instance = UserUnavailable.from_json(json)
# print the JSON string representation of the object
print(UserUnavailable.to_json())

# convert the object into a dict
user_unavailable_dict = user_unavailable_instance.to_dict()
# create an instance of UserUnavailable from a dict
user_unavailable_from_dict = UserUnavailable.from_dict(user_unavailable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


