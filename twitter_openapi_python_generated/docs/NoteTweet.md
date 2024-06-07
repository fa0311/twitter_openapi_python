# NoteTweet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_expandable** | **bool** |  | 
**note_tweet_results** | [**NoteTweetResult**](NoteTweetResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.note_tweet import NoteTweet

# TODO update the JSON string below
json = "{}"
# create an instance of NoteTweet from a JSON string
note_tweet_instance = NoteTweet.from_json(json)
# print the JSON string representation of the object
print(NoteTweet.to_json())

# convert the object into a dict
note_tweet_dict = note_tweet_instance.to_dict()
# create an instance of NoteTweet from a dict
note_tweet_from_dict = NoteTweet.from_dict(note_tweet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


