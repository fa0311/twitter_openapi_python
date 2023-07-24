# ItemResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | [optional] 
**result** | [**TweetUnion**](TweetUnion.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.item_result import ItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of ItemResult from a JSON string
item_result_instance = ItemResult.from_json(json)
# print the JSON string representation of the object
print ItemResult.to_json()

# convert the object into a dict
item_result_dict = item_result_instance.to_dict()
# create an instance of ItemResult from a dict
item_result_form_dict = item_result.from_dict(item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


