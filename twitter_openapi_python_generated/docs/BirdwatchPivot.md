# BirdwatchPivot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_to_action** | [**BirdwatchPivotCallToAction**](BirdwatchPivotCallToAction.md) |  | [optional] 
**destination_url** | **str** |  | 
**footer** | [**BirdwatchPivotFooter**](BirdwatchPivotFooter.md) |  | [optional] 
**icon_type** | **str** |  | 
**note** | [**BirdwatchPivotNote**](BirdwatchPivotNote.md) |  | [optional] 
**shorttitle** | **str** |  | [optional] 
**subtitle** | [**BirdwatchPivotSubtitle**](BirdwatchPivotSubtitle.md) |  | [optional] 
**title** | **str** |  | 
**title_detail** | **str** |  | [optional] 
**visual_style** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.birdwatch_pivot import BirdwatchPivot

# TODO update the JSON string below
json = "{}"
# create an instance of BirdwatchPivot from a JSON string
birdwatch_pivot_instance = BirdwatchPivot.from_json(json)
# print the JSON string representation of the object
print(BirdwatchPivot.to_json())

# convert the object into a dict
birdwatch_pivot_dict = birdwatch_pivot_instance.to_dict()
# create an instance of BirdwatchPivot from a dict
birdwatch_pivot_from_dict = BirdwatchPivot.from_dict(birdwatch_pivot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


