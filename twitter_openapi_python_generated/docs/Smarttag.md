# Smarttag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **List[int]** |  | 
**tag** | [**SmarttagTag**](SmarttagTag.md) |  | 
**text** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.smarttag import Smarttag

# TODO update the JSON string below
json = "{}"
# create an instance of Smarttag from a JSON string
smarttag_instance = Smarttag.from_json(json)
# print the JSON string representation of the object
print(Smarttag.to_json())

# convert the object into a dict
smarttag_dict = smarttag_instance.to_dict()
# create an instance of Smarttag from a dict
smarttag_from_dict = Smarttag.from_dict(smarttag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


