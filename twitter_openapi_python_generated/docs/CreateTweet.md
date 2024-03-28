# CreateTweet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Tweet**](Tweet.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.create_tweet import CreateTweet

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTweet from a JSON string
create_tweet_instance = CreateTweet.from_json(json)
# print the JSON string representation of the object
print(CreateTweet.to_json())

# convert the object into a dict
create_tweet_dict = create_tweet_instance.to_dict()
# create an instance of CreateTweet from a dict
create_tweet_form_dict = create_tweet.from_dict(create_tweet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


