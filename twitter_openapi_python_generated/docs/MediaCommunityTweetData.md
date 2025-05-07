# MediaCommunityTweetData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**community_results** | [**MediaCommunityResults**](MediaCommunityResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.media_community_tweet_data import MediaCommunityTweetData

# TODO update the JSON string below
json = "{}"
# create an instance of MediaCommunityTweetData from a JSON string
media_community_tweet_data_instance = MediaCommunityTweetData.from_json(json)
# print the JSON string representation of the object
print(MediaCommunityTweetData.to_json())

# convert the object into a dict
media_community_tweet_data_dict = media_community_tweet_data_instance.to_dict()
# create an instance of MediaCommunityTweetData from a dict
media_community_tweet_data_from_dict = MediaCommunityTweetData.from_dict(media_community_tweet_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


