# CashtagInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**ticker** | **str** |  | 
**tradable_platforms** | **List[str]** |  | 

## Example

```python
from twitter_openapi_python_generated.models.cashtag_info import CashtagInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CashtagInfo from a JSON string
cashtag_info_instance = CashtagInfo.from_json(json)
# print the JSON string representation of the object
print(CashtagInfo.to_json())

# convert the object into a dict
cashtag_info_dict = cashtag_info_instance.to_dict()
# create an instance of CashtagInfo from a dict
cashtag_info_from_dict = CashtagInfo.from_dict(cashtag_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


