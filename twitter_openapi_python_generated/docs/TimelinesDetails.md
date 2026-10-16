# TimelinesDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_data** | **str** |  | [optional] 
**injection_type** | **str** |  | [optional] 
**source_data** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.timelines_details import TimelinesDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TimelinesDetails from a JSON string
timelines_details_instance = TimelinesDetails.from_json(json)
# print the JSON string representation of the object
print(TimelinesDetails.to_json())

# convert the object into a dict
timelines_details_dict = timelines_details_instance.to_dict()
# create an instance of TimelinesDetails from a dict
timelines_details_from_dict = TimelinesDetails.from_dict(timelines_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


