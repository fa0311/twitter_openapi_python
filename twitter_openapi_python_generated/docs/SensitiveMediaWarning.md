# SensitiveMediaWarning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult_content** | **bool** |  | [optional] 
**graphic_violence** | **bool** |  | [optional] 
**other** | **bool** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.sensitive_media_warning import SensitiveMediaWarning

# TODO update the JSON string below
json = "{}"
# create an instance of SensitiveMediaWarning from a JSON string
sensitive_media_warning_instance = SensitiveMediaWarning.from_json(json)
# print the JSON string representation of the object
print(SensitiveMediaWarning.to_json())

# convert the object into a dict
sensitive_media_warning_dict = sensitive_media_warning_instance.to_dict()
# create an instance of SensitiveMediaWarning from a dict
sensitive_media_warning_from_dict = SensitiveMediaWarning.from_dict(sensitive_media_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


