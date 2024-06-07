# GetSearchTimeline200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SearchTimelineData**](SearchTimelineData.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.get_search_timeline200_response import GetSearchTimeline200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSearchTimeline200Response from a JSON string
get_search_timeline200_response_instance = GetSearchTimeline200Response.from_json(json)
# print the JSON string representation of the object
print(GetSearchTimeline200Response.to_json())

# convert the object into a dict
get_search_timeline200_response_dict = get_search_timeline200_response_instance.to_dict()
# create an instance of GetSearchTimeline200Response from a dict
get_search_timeline200_response_from_dict = GetSearchTimeline200Response.from_dict(get_search_timeline200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


