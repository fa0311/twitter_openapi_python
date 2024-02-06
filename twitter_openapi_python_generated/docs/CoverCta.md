# CoverCta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**button_style** | **str** |  | [optional] 
**callbacks** | [**List[Callback]**](Callback.md) |  | 
**client_event_info** | [**CtaClientEventInfo**](CtaClientEventInfo.md) |  | 
**cta_behavior** | [**TimelineCoverBehavior**](TimelineCoverBehavior.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.cover_cta import CoverCta

# TODO update the JSON string below
json = "{}"
# create an instance of CoverCta from a JSON string
cover_cta_instance = CoverCta.from_json(json)
# print the JSON string representation of the object
print CoverCta.to_json()

# convert the object into a dict
cover_cta_dict = cover_cta_instance.to_dict()
# create an instance of CoverCta from a dict
cover_cta_form_dict = cover_cta.from_dict(cover_cta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


