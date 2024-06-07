# NoteTweetResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**NoteTweetResultData**](NoteTweetResultData.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.note_tweet_result import NoteTweetResult

# TODO update the JSON string below
json = "{}"
# create an instance of NoteTweetResult from a JSON string
note_tweet_result_instance = NoteTweetResult.from_json(json)
# print the JSON string representation of the object
print(NoteTweetResult.to_json())

# convert the object into a dict
note_tweet_result_dict = note_tweet_result_instance.to_dict()
# create an instance of NoteTweetResult from a dict
note_tweet_result_from_dict = NoteTweetResult.from_dict(note_tweet_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


