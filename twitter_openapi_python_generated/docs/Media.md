# Media


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_url** | **str** |  | 
**expanded_url** | **str** |  | 
**ext_media_availability** | **Dict[str, object]** |  | [optional] 
**id_str** | **str** |  | 
**indices** | **List[int]** |  | 
**media_key** | **str** |  | [optional] 
**media_url_https** | **str** |  | 
**original_info** | [**MediaOriginalInfo**](MediaOriginalInfo.md) |  | 
**sizes** | **Dict[str, object]** |  | 
**type** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.media import Media

# TODO update the JSON string below
json = "{}"
# create an instance of Media from a JSON string
media_instance = Media.from_json(json)
# print the JSON string representation of the object
print Media.to_json()

# convert the object into a dict
media_dict = media_instance.to_dict()
# create an instance of Media from a dict
media_form_dict = media.from_dict(media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


