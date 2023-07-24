# Session


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sso_init_tokens** | **object** |  | [optional] 
**communities_actions** | [**CommunitiesActions**](CommunitiesActions.md) |  | 
**country** | **str** |  | 
**guest_id** | **str** |  | 
**has_community_memberships** | **bool** |  | 
**is_active_creator** | **bool** |  | 
**is_restricted_session** | **bool** |  | 
**is_super_follow_subscriber** | **bool** |  | 
**language** | **str** |  | 
**one_factor_login_eligibility** | [**OneFactorLoginEligibility**](OneFactorLoginEligibility.md) |  | 
**super_followers_count** | **int** |  | 
**super_follows_application_status** | **str** |  | 
**user_features** | [**UserFeatures**](UserFeatures.md) |  | 
**user_id** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.session import Session

# TODO update the JSON string below
json = "{}"
# create an instance of Session from a JSON string
session_instance = Session.from_json(json)
# print the JSON string representation of the object
print Session.to_json()

# convert the object into a dict
session_dict = session_instance.to_dict()
# create an instance of Session from a dict
session_form_dict = session.from_dict(session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


