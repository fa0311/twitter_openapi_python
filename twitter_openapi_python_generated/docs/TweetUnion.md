# TweetUnion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**card** | [**TweetCard**](TweetCard.md) |  | [optional] 
**core** | [**UserResultCore**](UserResultCore.md) |  | 
**edit_control** | [**TweetEditControl**](TweetEditControl.md) |  | 
**edit_prespective** | [**TweetEditPrespective**](TweetEditPrespective.md) |  | 
**is_translatable** | **bool** |  | [default to False]
**legacy** | [**TweetLegacy**](TweetLegacy.md) |  | 
**quoted_status_result** | [**ItemResult**](ItemResult.md) |  | [optional] 
**rest_id** | **str** |  | 
**unmention_data** | **object** |  | [optional] 
**views** | [**TweetViews**](TweetViews.md) |  | 
**tweet** | [**Tweet**](Tweet.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_union import TweetUnion

# TODO update the JSON string below
json = "{}"
# create an instance of TweetUnion from a JSON string
tweet_union_instance = TweetUnion.from_json(json)
# print the JSON string representation of the object
print TweetUnion.to_json()

# convert the object into a dict
tweet_union_dict = tweet_union_instance.to_dict()
# create an instance of TweetUnion from a dict
tweet_union_form_dict = tweet_union.from_dict(tweet_union_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


