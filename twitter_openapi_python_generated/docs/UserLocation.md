# UserLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_location import UserLocation

# TODO update the JSON string below
json = "{}"
# create an instance of UserLocation from a JSON string
user_location_instance = UserLocation.from_json(json)
# print the JSON string representation of the object
print(UserLocation.to_json())

# convert the object into a dict
user_location_dict = user_location_instance.to_dict()
# create an instance of UserLocation from a dict
user_location_from_dict = UserLocation.from_dict(user_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


