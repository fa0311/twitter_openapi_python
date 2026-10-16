# DeepsearchStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**web_results** | [**List[DeepsearchWebResult]**](DeepsearchWebResult.md) |  | 
**x_post_ids** | **List[str]** |  | 

## Example

```python
from twitter_openapi_python_generated.models.deepsearch_step import DeepsearchStep

# TODO update the JSON string below
json = "{}"
# create an instance of DeepsearchStep from a JSON string
deepsearch_step_instance = DeepsearchStep.from_json(json)
# print the JSON string representation of the object
print(DeepsearchStep.to_json())

# convert the object into a dict
deepsearch_step_dict = deepsearch_step_instance.to_dict()
# create an instance of DeepsearchStep from a dict
deepsearch_step_from_dict = DeepsearchStep.from_dict(deepsearch_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


