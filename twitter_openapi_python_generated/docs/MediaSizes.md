# MediaSizes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**large** | [**MediaSize**](MediaSize.md) |  | 
**medium** | [**MediaSize**](MediaSize.md) |  | 
**small** | [**MediaSize**](MediaSize.md) |  | 
**thumb** | [**MediaSize**](MediaSize.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.media_sizes import MediaSizes

# TODO update the JSON string below
json = "{}"
# create an instance of MediaSizes from a JSON string
media_sizes_instance = MediaSizes.from_json(json)
# print the JSON string representation of the object
print(MediaSizes.to_json())

# convert the object into a dict
media_sizes_dict = media_sizes_instance.to_dict()
# create an instance of MediaSizes from a dict
media_sizes_form_dict = media_sizes.from_dict(media_sizes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


