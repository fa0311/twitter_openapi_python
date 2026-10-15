# UserPinnedItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tweet_ids_str** | **List[str]** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.user_pinned_items import UserPinnedItems

# TODO update the JSON string below
json = "{}"
# create an instance of UserPinnedItems from a JSON string
user_pinned_items_instance = UserPinnedItems.from_json(json)
# print the JSON string representation of the object
print(UserPinnedItems.to_json())

# convert the object into a dict
user_pinned_items_dict = user_pinned_items_instance.to_dict()
# create an instance of UserPinnedItems from a dict
user_pinned_items_from_dict = UserPinnedItems.from_dict(user_pinned_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


