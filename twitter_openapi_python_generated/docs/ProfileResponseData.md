# ProfileResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_result_by_screen_name** | [**UserResultByScreenName**](UserResultByScreenName.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.profile_response_data import ProfileResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileResponseData from a JSON string
profile_response_data_instance = ProfileResponseData.from_json(json)
# print the JSON string representation of the object
print(ProfileResponseData.to_json())

# convert the object into a dict
profile_response_data_dict = profile_response_data_instance.to_dict()
# create an instance of ProfileResponseData from a dict
profile_response_data_form_dict = profile_response_data.from_dict(profile_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


