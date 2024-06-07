# BirdwatchPivotFooter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[BirdwatchEntity]**](BirdwatchEntity.md) |  | 
**text** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.birdwatch_pivot_footer import BirdwatchPivotFooter

# TODO update the JSON string below
json = "{}"
# create an instance of BirdwatchPivotFooter from a JSON string
birdwatch_pivot_footer_instance = BirdwatchPivotFooter.from_json(json)
# print the JSON string representation of the object
print(BirdwatchPivotFooter.to_json())

# convert the object into a dict
birdwatch_pivot_footer_dict = birdwatch_pivot_footer_instance.to_dict()
# create an instance of BirdwatchPivotFooter from a dict
birdwatch_pivot_footer_from_dict = BirdwatchPivotFooter.from_dict(birdwatch_pivot_footer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


