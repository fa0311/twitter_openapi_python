# MediaSize


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**h** | **int** |  | 
**resize** | **str** |  | 
**w** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.media_size import MediaSize

# TODO update the JSON string below
json = "{}"
# create an instance of MediaSize from a JSON string
media_size_instance = MediaSize.from_json(json)
# print the JSON string representation of the object
print MediaSize.to_json()

# convert the object into a dict
media_size_dict = media_size_instance.to_dict()
# create an instance of MediaSize from a dict
media_size_form_dict = media_size.from_dict(media_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


