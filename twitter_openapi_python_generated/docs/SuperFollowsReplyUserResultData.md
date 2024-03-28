# SuperFollowsReplyUserResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**legacy** | [**SuperFollowsReplyUserResultLegacy**](SuperFollowsReplyUserResultLegacy.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.super_follows_reply_user_result_data import SuperFollowsReplyUserResultData

# TODO update the JSON string below
json = "{}"
# create an instance of SuperFollowsReplyUserResultData from a JSON string
super_follows_reply_user_result_data_instance = SuperFollowsReplyUserResultData.from_json(json)
# print the JSON string representation of the object
print(SuperFollowsReplyUserResultData.to_json())

# convert the object into a dict
super_follows_reply_user_result_data_dict = super_follows_reply_user_result_data_instance.to_dict()
# create an instance of SuperFollowsReplyUserResultData from a dict
super_follows_reply_user_result_data_form_dict = super_follows_reply_user_result_data.from_dict(super_follows_reply_user_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


