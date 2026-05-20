# PostCtaUserResultsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**avatar** | [**PostCtaUserResultsAvatar**](PostCtaUserResultsAvatar.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_cta_user_results_result import PostCtaUserResultsResult

# TODO update the JSON string below
json = "{}"
# create an instance of PostCtaUserResultsResult from a JSON string
post_cta_user_results_result_instance = PostCtaUserResultsResult.from_json(json)
# print the JSON string representation of the object
print(PostCtaUserResultsResult.to_json())

# convert the object into a dict
post_cta_user_results_result_dict = post_cta_user_results_result_instance.to_dict()
# create an instance of PostCtaUserResultsResult from a dict
post_cta_user_results_result_from_dict = PostCtaUserResultsResult.from_dict(post_cta_user_results_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


