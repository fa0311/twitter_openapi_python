# TopicCarouselQueryResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**community_topic_results** | [**CommunityTopicResults**](CommunityTopicResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.topic_carousel_query_response_data import TopicCarouselQueryResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TopicCarouselQueryResponseData from a JSON string
topic_carousel_query_response_data_instance = TopicCarouselQueryResponseData.from_json(json)
# print the JSON string representation of the object
print(TopicCarouselQueryResponseData.to_json())

# convert the object into a dict
topic_carousel_query_response_data_dict = topic_carousel_query_response_data_instance.to_dict()
# create an instance of TopicCarouselQueryResponseData from a dict
topic_carousel_query_response_data_from_dict = TopicCarouselQueryResponseData.from_dict(topic_carousel_query_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


