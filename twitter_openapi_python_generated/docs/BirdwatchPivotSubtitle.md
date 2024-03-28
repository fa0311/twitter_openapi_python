# BirdwatchPivotSubtitle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[BirdwatchEntity]**](BirdwatchEntity.md) |  | 
**text** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.birdwatch_pivot_subtitle import BirdwatchPivotSubtitle

# TODO update the JSON string below
json = "{}"
# create an instance of BirdwatchPivotSubtitle from a JSON string
birdwatch_pivot_subtitle_instance = BirdwatchPivotSubtitle.from_json(json)
# print the JSON string representation of the object
print(BirdwatchPivotSubtitle.to_json())

# convert the object into a dict
birdwatch_pivot_subtitle_dict = birdwatch_pivot_subtitle_instance.to_dict()
# create an instance of BirdwatchPivotSubtitle from a dict
birdwatch_pivot_subtitle_form_dict = birdwatch_pivot_subtitle.from_dict(birdwatch_pivot_subtitle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


