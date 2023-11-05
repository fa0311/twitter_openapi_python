# BirdwatchPivot


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_url** | **str** |  | 
**footer** | [**BirdwatchPivotFooter**](BirdwatchPivotFooter.md) |  | 
**icon_type** | **str** |  | 
**note** | [**BirdwatchPivotNote**](BirdwatchPivotNote.md) |  | 
**shorttitle** | **str** |  | 
**subtitle** | [**BirdwatchPivotSubtitle**](BirdwatchPivotSubtitle.md) |  | 
**title** | **str** |  | 
**visual_style** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.birdwatch_pivot import BirdwatchPivot

# TODO update the JSON string below
json = "{}"
# create an instance of BirdwatchPivot from a JSON string
birdwatch_pivot_instance = BirdwatchPivot.from_json(json)
# print the JSON string representation of the object
print BirdwatchPivot.to_json()

# convert the object into a dict
birdwatch_pivot_dict = birdwatch_pivot_instance.to_dict()
# create an instance of BirdwatchPivot from a dict
birdwatch_pivot_form_dict = birdwatch_pivot.from_dict(birdwatch_pivot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


