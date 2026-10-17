# CashtagAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rest_id** | **str** |  | 
**size_variant** | **int** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.cashtag_attachment import CashtagAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of CashtagAttachment from a JSON string
cashtag_attachment_instance = CashtagAttachment.from_json(json)
# print the JSON string representation of the object
print(CashtagAttachment.to_json())

# convert the object into a dict
cashtag_attachment_dict = cashtag_attachment_instance.to_dict()
# create an instance of CashtagAttachment from a dict
cashtag_attachment_from_dict = CashtagAttachment.from_dict(cashtag_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


