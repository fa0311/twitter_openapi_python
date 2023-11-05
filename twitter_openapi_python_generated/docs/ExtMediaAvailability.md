# ExtMediaAvailability


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.ext_media_availability import ExtMediaAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of ExtMediaAvailability from a JSON string
ext_media_availability_instance = ExtMediaAvailability.from_json(json)
# print the JSON string representation of the object
print ExtMediaAvailability.to_json()

# convert the object into a dict
ext_media_availability_dict = ext_media_availability_instance.to_dict()
# create an instance of ExtMediaAvailability from a dict
ext_media_availability_form_dict = ext_media_availability.from_dict(ext_media_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


