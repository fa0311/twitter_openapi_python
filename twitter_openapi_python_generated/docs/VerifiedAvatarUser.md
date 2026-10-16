# VerifiedAvatarUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**affiliates_highlighted_label** | [**AffiliatesHighlightedLabel**](AffiliatesHighlightedLabel.md) |  | 
**is_blue_verified** | **bool** |  | 
**profile_image_shape** | **str** |  | 
**rest_id** | **str** |  | 
**verification** | **object** |  | 

## Example

```python
from twitter_openapi_python_generated.models.verified_avatar_user import VerifiedAvatarUser

# TODO update the JSON string below
json = "{}"
# create an instance of VerifiedAvatarUser from a JSON string
verified_avatar_user_instance = VerifiedAvatarUser.from_json(json)
# print the JSON string representation of the object
print(VerifiedAvatarUser.to_json())

# convert the object into a dict
verified_avatar_user_dict = verified_avatar_user_instance.to_dict()
# create an instance of VerifiedAvatarUser from a dict
verified_avatar_user_from_dict = VerifiedAvatarUser.from_dict(verified_avatar_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


