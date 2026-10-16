# TopicCarouselQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TopicCarouselQueryResponseData**](TopicCarouselQueryResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.topic_carousel_query_response import TopicCarouselQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TopicCarouselQueryResponse from a JSON string
topic_carousel_query_response_instance = TopicCarouselQueryResponse.from_json(json)
# print the JSON string representation of the object
print(TopicCarouselQueryResponse.to_json())

# convert the object into a dict
topic_carousel_query_response_dict = topic_carousel_query_response_instance.to_dict()
# create an instance of TopicCarouselQueryResponse from a dict
topic_carousel_query_response_from_dict = TopicCarouselQueryResponse.from_dict(topic_carousel_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


