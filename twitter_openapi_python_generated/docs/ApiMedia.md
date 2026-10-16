# ApiMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**id** | **str** |  | 
**media_id** | **str** |  | 
**media_info** | [**ApiImage**](ApiImage.md) |  | 
**media_key** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.api_media import ApiMedia

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMedia from a JSON string
api_media_instance = ApiMedia.from_json(json)
# print the JSON string representation of the object
print(ApiMedia.to_json())

# convert the object into a dict
api_media_dict = api_media_instance.to_dict()
# create an instance of ApiMedia from a dict
api_media_from_dict = ApiMedia.from_dict(api_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


