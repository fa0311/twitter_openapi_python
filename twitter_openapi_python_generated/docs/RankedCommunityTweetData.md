# RankedCommunityTweetData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**community_results** | [**RankedCommunityResults**](RankedCommunityResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.ranked_community_tweet_data import RankedCommunityTweetData

# TODO update the JSON string below
json = "{}"
# create an instance of RankedCommunityTweetData from a JSON string
ranked_community_tweet_data_instance = RankedCommunityTweetData.from_json(json)
# print the JSON string representation of the object
print(RankedCommunityTweetData.to_json())

# convert the object into a dict
ranked_community_tweet_data_dict = ranked_community_tweet_data_instance.to_dict()
# create an instance of RankedCommunityTweetData from a dict
ranked_community_tweet_data_from_dict = RankedCommunityTweetData.from_dict(ranked_community_tweet_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


