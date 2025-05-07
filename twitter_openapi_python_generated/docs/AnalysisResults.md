# AnalysisResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Tweet**](Tweet.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.analysis_results import AnalysisResults

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisResults from a JSON string
analysis_results_instance = AnalysisResults.from_json(json)
# print the JSON string representation of the object
print(AnalysisResults.to_json())

# convert the object into a dict
analysis_results_dict = analysis_results_instance.to_dict()
# create an instance of AnalysisResults from a dict
analysis_results_from_dict = AnalysisResults.from_dict(analysis_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


