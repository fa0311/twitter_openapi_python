# TweetViews


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.tweet_views import TweetViews

# TODO update the JSON string below
json = "{}"
# create an instance of TweetViews from a JSON string
tweet_views_instance = TweetViews.from_json(json)
# print the JSON string representation of the object
print TweetViews.to_json()

# convert the object into a dict
tweet_views_dict = tweet_views_instance.to_dict()
# create an instance of TweetViews from a dict
tweet_views_form_dict = tweet_views.from_dict(tweet_views_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


