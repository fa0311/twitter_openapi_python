# PostCreateTweetRequestVariablesMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_entities** | [**List[PostCreateTweetRequestVariablesMediaMediaEntitiesInner]**](PostCreateTweetRequestVariablesMediaMediaEntitiesInner.md) |  | 
**possibly_sensitive** | **bool** |  | [default to False]

## Example

```python
from twitter_openapi_python_generated.models.post_create_tweet_request_variables_media import PostCreateTweetRequestVariablesMedia

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateTweetRequestVariablesMedia from a JSON string
post_create_tweet_request_variables_media_instance = PostCreateTweetRequestVariablesMedia.from_json(json)
# print the JSON string representation of the object
print PostCreateTweetRequestVariablesMedia.to_json()

# convert the object into a dict
post_create_tweet_request_variables_media_dict = post_create_tweet_request_variables_media_instance.to_dict()
# create an instance of PostCreateTweetRequestVariablesMedia from a dict
post_create_tweet_request_variables_media_form_dict = post_create_tweet_request_variables_media.from_dict(post_create_tweet_request_variables_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


