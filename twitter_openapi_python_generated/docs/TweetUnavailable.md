# TweetUnavailable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.tweet_unavailable import TweetUnavailable

# TODO update the JSON string below
json = "{}"
# create an instance of TweetUnavailable from a JSON string
tweet_unavailable_instance = TweetUnavailable.from_json(json)
# print the JSON string representation of the object
print(TweetUnavailable.to_json())

# convert the object into a dict
tweet_unavailable_dict = tweet_unavailable_instance.to_dict()
# create an instance of TweetUnavailable from a dict
tweet_unavailable_from_dict = TweetUnavailable.from_dict(tweet_unavailable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


