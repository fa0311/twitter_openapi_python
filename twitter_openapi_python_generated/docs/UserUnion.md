# UserUnion


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
**reason** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_union import UserUnion

# TODO update the JSON string below
json = "{}"
# create an instance of UserUnion from a JSON string
user_union_instance = UserUnion.from_json(json)
# print the JSON string representation of the object
print UserUnion.to_json()

# convert the object into a dict
user_union_dict = user_union_instance.to_dict()
# create an instance of UserUnion from a dict
user_union_form_dict = user_union.from_dict(user_union_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


