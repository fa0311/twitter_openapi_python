# QuotedRefResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**QuotedRefResultData**](QuotedRefResultData.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.quoted_ref_result import QuotedRefResult

# TODO update the JSON string below
json = "{}"
# create an instance of QuotedRefResult from a JSON string
quoted_ref_result_instance = QuotedRefResult.from_json(json)
# print the JSON string representation of the object
print QuotedRefResult.to_json()

# convert the object into a dict
quoted_ref_result_dict = quoted_ref_result_instance.to_dict()
# create an instance of QuotedRefResult from a dict
quoted_ref_result_form_dict = quoted_ref_result.from_dict(quoted_ref_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


