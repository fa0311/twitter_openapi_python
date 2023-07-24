# TweetEditPrespective


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorited** | **bool** |  | [optional] 
**retweeted** | **bool** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.tweet_edit_prespective import TweetEditPrespective

# TODO update the JSON string below
json = "{}"
# create an instance of TweetEditPrespective from a JSON string
tweet_edit_prespective_instance = TweetEditPrespective.from_json(json)
# print the JSON string representation of the object
print TweetEditPrespective.to_json()

# convert the object into a dict
tweet_edit_prespective_dict = tweet_edit_prespective_instance.to_dict()
# create an instance of TweetEditPrespective from a dict
tweet_edit_prespective_form_dict = tweet_edit_prespective.from_dict(tweet_edit_prespective_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


