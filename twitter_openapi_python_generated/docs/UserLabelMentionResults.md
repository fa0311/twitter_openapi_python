# UserLabelMentionResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**UserLabelMentionUser**](UserLabelMentionUser.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_label_mention_results import UserLabelMentionResults

# TODO update the JSON string below
json = "{}"
# create an instance of UserLabelMentionResults from a JSON string
user_label_mention_results_instance = UserLabelMentionResults.from_json(json)
# print the JSON string representation of the object
print(UserLabelMentionResults.to_json())

# convert the object into a dict
user_label_mention_results_dict = user_label_mention_results_instance.to_dict()
# create an instance of UserLabelMentionResults from a dict
user_label_mention_results_from_dict = UserLabelMentionResults.from_dict(user_label_mention_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


