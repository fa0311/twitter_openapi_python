# Entities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hashtags** | **List[Dict[str, object]]** |  | [optional] 
**media** | [**List[Media]**](Media.md) |  | [optional] 
**smarttags** | [**List[Smarttag]**](Smarttag.md) |  | [optional] 
**symbols** | **List[Dict[str, object]]** |  | [optional] 
**timestamps** | [**List[Timestamp]**](Timestamp.md) |  | [optional] 
**urls** | [**List[Url]**](Url.md) |  | [optional] 
**user_mentions** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.entities import Entities

# TODO update the JSON string below
json = "{}"
# create an instance of Entities from a JSON string
entities_instance = Entities.from_json(json)
# print the JSON string representation of the object
print(Entities.to_json())

# convert the object into a dict
entities_dict = entities_instance.to_dict()
# create an instance of Entities from a dict
entities_from_dict = Entities.from_dict(entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


