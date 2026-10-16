# UserLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge** | [**UserLabelBadge**](UserLabelBadge.md) |  | 
**description** | **str** |  | 
**long_description** | [**UserLabelText**](UserLabelText.md) |  | [optional] 
**url** | [**UserLabelUrl**](UserLabelUrl.md) |  | [optional] 
**user_label_display_type** | **str** |  | [optional] 
**user_label_type** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_label import UserLabel

# TODO update the JSON string below
json = "{}"
# create an instance of UserLabel from a JSON string
user_label_instance = UserLabel.from_json(json)
# print the JSON string representation of the object
print(UserLabel.to_json())

# convert the object into a dict
user_label_dict = user_label_instance.to_dict()
# create an instance of UserLabel from a dict
user_label_from_dict = UserLabel.from_dict(user_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


