# SmarttagTagInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**CashtagInfo**](CashtagInfo.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.smarttag_tag_info import SmarttagTagInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SmarttagTagInfo from a JSON string
smarttag_tag_info_instance = SmarttagTagInfo.from_json(json)
# print the JSON string representation of the object
print(SmarttagTagInfo.to_json())

# convert the object into a dict
smarttag_tag_info_dict = smarttag_tag_info_instance.to_dict()
# create an instance of SmarttagTagInfo from a dict
smarttag_tag_info_from_dict = SmarttagTagInfo.from_dict(smarttag_tag_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


