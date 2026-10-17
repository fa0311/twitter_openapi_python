# AboutAccountUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**about_profile** | [**AboutProfile**](AboutProfile.md) |  | 
**affiliates_highlighted_label** | [**AffiliatesHighlightedLabel**](AffiliatesHighlightedLabel.md) |  | 
**avatar** | [**UserAvatar**](UserAvatar.md) |  | 
**core** | [**UserCore**](UserCore.md) |  | 
**id** | **str** |  | 
**identity_profile_labels_highlighted_label** | [**IdentityProfileLabelsHighlightedLabel**](IdentityProfileLabelsHighlightedLabel.md) |  | 
**is_blue_verified** | **bool** |  | 
**privacy** | [**UserPrivacy**](UserPrivacy.md) |  | 
**profile_image_shape** | **str** |  | 
**rest_id** | **str** |  | 
**verification** | [**UserVerification**](UserVerification.md) |  | 
**verification_info** | [**AboutAccountVerificationInfo**](AboutAccountVerificationInfo.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.about_account_user import AboutAccountUser

# TODO update the JSON string below
json = "{}"
# create an instance of AboutAccountUser from a JSON string
about_account_user_instance = AboutAccountUser.from_json(json)
# print the JSON string representation of the object
print(AboutAccountUser.to_json())

# convert the object into a dict
about_account_user_dict = about_account_user_instance.to_dict()
# create an instance of AboutAccountUser from a dict
about_account_user_from_dict = AboutAccountUser.from_dict(about_account_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


