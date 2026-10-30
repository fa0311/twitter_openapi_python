# Preroll


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_preroll_type** | **str** |  | 
**media_info** | [**PrerollMediaInfo**](PrerollMediaInfo.md) |  | 
**preroll_id** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.preroll import Preroll

# TODO update the JSON string below
json = "{}"
# create an instance of Preroll from a JSON string
preroll_instance = Preroll.from_json(json)
# print the JSON string representation of the object
print(Preroll.to_json())

# convert the object into a dict
preroll_dict = preroll_instance.to_dict()
# create an instance of Preroll from a dict
preroll_from_dict = Preroll.from_dict(preroll_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


