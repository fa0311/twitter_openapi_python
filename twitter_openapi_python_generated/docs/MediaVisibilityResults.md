# MediaVisibilityResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blurred_image_interstitial** | [**MediaVisibilityResultsBlurredImageInterstitial**](MediaVisibilityResultsBlurredImageInterstitial.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.media_visibility_results import MediaVisibilityResults

# TODO update the JSON string below
json = "{}"
# create an instance of MediaVisibilityResults from a JSON string
media_visibility_results_instance = MediaVisibilityResults.from_json(json)
# print the JSON string representation of the object
print(MediaVisibilityResults.to_json())

# convert the object into a dict
media_visibility_results_dict = media_visibility_results_instance.to_dict()
# create an instance of MediaVisibilityResults from a dict
media_visibility_results_from_dict = MediaVisibilityResults.from_dict(media_visibility_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


