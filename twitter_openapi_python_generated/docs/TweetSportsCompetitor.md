# TweetSportsCompetitor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbreviation** | **str** |  | 
**dark_logo_url** | **str** |  | 
**is_active** | **bool** |  | 
**is_winner** | **bool** |  | 
**logo_url** | **str** |  | 
**name** | **str** |  | 
**score** | **str** |  | 
**team_rest_id** | [**TweetSportsRestId**](TweetSportsRestId.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_sports_competitor import TweetSportsCompetitor

# TODO update the JSON string below
json = "{}"
# create an instance of TweetSportsCompetitor from a JSON string
tweet_sports_competitor_instance = TweetSportsCompetitor.from_json(json)
# print the JSON string representation of the object
print(TweetSportsCompetitor.to_json())

# convert the object into a dict
tweet_sports_competitor_dict = tweet_sports_competitor_instance.to_dict()
# create an instance of TweetSportsCompetitor from a dict
tweet_sports_competitor_from_dict = TweetSportsCompetitor.from_dict(tweet_sports_competitor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


