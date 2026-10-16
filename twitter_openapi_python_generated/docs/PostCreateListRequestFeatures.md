# PostCreateListRequestFeatures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_label_improvements_pcf_label_in_post_enabled** | **bool** |  | [default to True]
**responsive_web_graphql_timeline_navigation_enabled** | **bool** |  | [default to True]
**responsive_web_profile_redirect_enabled** | **bool** |  | [default to True]
**rweb_tipjar_consumption_enabled** | **bool** |  | [default to False]
**verified_phone_label_enabled** | **bool** |  | [default to False]

## Example

```python
from twitter_openapi_python_generated.models.post_create_list_request_features import PostCreateListRequestFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateListRequestFeatures from a JSON string
post_create_list_request_features_instance = PostCreateListRequestFeatures.from_json(json)
# print the JSON string representation of the object
print(PostCreateListRequestFeatures.to_json())

# convert the object into a dict
post_create_list_request_features_dict = post_create_list_request_features_instance.to_dict()
# create an instance of PostCreateListRequestFeatures from a dict
post_create_list_request_features_from_dict = PostCreateListRequestFeatures.from_dict(post_create_list_request_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


