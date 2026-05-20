# TweetPostCta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_locations** | **List[str]** |  | 
**post_cta** | [**PostCta**](PostCta.md) |  | 
**scribe_id** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.tweet_post_cta import TweetPostCta

# TODO update the JSON string below
json = "{}"
# create an instance of TweetPostCta from a JSON string
tweet_post_cta_instance = TweetPostCta.from_json(json)
# print the JSON string representation of the object
print(TweetPostCta.to_json())

# convert the object into a dict
tweet_post_cta_dict = tweet_post_cta_instance.to_dict()
# create an instance of TweetPostCta from a dict
tweet_post_cta_from_dict = TweetPostCta.from_dict(tweet_post_cta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


