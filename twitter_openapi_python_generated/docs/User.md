# User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**affiliates_highlighted_label** | **Dict[str, object]** |  | 
**business_account** | **Dict[str, object]** |  | [optional] 
**has_graduated_access** | **bool** |  | [optional] 
**has_nft_avatar** | **bool** |  | [optional] [default to False]
**id** | **str** |  | 
**is_blue_verified** | **bool** |  | [default to False]
**legacy** | [**UserLegacy**](UserLegacy.md) |  | 
**rest_id** | **str** |  | 
**super_follow_eligible** | **bool** |  | [default to False]
**super_followed_by** | **bool** |  | [default to False]
**super_following** | **bool** |  | [default to False]

## Example

```python
from twitter_openapi_python_generated.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


