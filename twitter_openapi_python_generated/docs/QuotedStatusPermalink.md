# QuotedStatusPermalink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | **str** |  | 
**expanded** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.quoted_status_permalink import QuotedStatusPermalink

# TODO update the JSON string below
json = "{}"
# create an instance of QuotedStatusPermalink from a JSON string
quoted_status_permalink_instance = QuotedStatusPermalink.from_json(json)
# print the JSON string representation of the object
print QuotedStatusPermalink.to_json()

# convert the object into a dict
quoted_status_permalink_dict = quoted_status_permalink_instance.to_dict()
# create an instance of QuotedStatusPermalink from a dict
quoted_status_permalink_form_dict = quoted_status_permalink.from_dict(quoted_status_permalink_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


