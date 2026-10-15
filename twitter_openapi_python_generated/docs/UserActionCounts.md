# UserActionCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorites_count** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_action_counts import UserActionCounts

# TODO update the JSON string below
json = "{}"
# create an instance of UserActionCounts from a JSON string
user_action_counts_instance = UserActionCounts.from_json(json)
# print the JSON string representation of the object
print(UserActionCounts.to_json())

# convert the object into a dict
user_action_counts_dict = user_action_counts_instance.to_dict()
# create an instance of UserActionCounts from a dict
user_action_counts_from_dict = UserActionCounts.from_dict(user_action_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


