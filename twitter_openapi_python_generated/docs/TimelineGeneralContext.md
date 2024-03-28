# TimelineGeneralContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** |  | [optional] 
**landing_url** | [**SocialContextLandingUrl**](SocialContextLandingUrl.md) |  | [optional] 
**text** | **str** |  | [optional] 
**type** | [**SocialContextUnionType**](SocialContextUnionType.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.timeline_general_context import TimelineGeneralContext

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineGeneralContext from a JSON string
timeline_general_context_instance = TimelineGeneralContext.from_json(json)
# print the JSON string representation of the object
print(TimelineGeneralContext.to_json())

# convert the object into a dict
timeline_general_context_dict = timeline_general_context_instance.to_dict()
# create an instance of TimelineGeneralContext from a dict
timeline_general_context_form_dict = timeline_general_context.from_dict(timeline_general_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


