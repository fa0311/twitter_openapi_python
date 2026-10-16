# ExplorePageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ExplorePageResponseData**](ExplorePageResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.explore_page_response import ExplorePageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExplorePageResponse from a JSON string
explore_page_response_instance = ExplorePageResponse.from_json(json)
# print the JSON string representation of the object
print(ExplorePageResponse.to_json())

# convert the object into a dict
explore_page_response_dict = explore_page_response_instance.to_dict()
# create an instance of ExplorePageResponse from a dict
explore_page_response_from_dict = ExplorePageResponse.from_dict(explore_page_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


