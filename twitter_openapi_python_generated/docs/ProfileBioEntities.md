# ProfileBioEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**ProfileBioEntitiesUrls**](ProfileBioEntitiesUrls.md) |  | 
**url** | [**ProfileBioEntitiesUrls**](ProfileBioEntitiesUrls.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.profile_bio_entities import ProfileBioEntities

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileBioEntities from a JSON string
profile_bio_entities_instance = ProfileBioEntities.from_json(json)
# print the JSON string representation of the object
print(ProfileBioEntities.to_json())

# convert the object into a dict
profile_bio_entities_dict = profile_bio_entities_instance.to_dict()
# create an instance of ProfileBioEntities from a dict
profile_bio_entities_from_dict = ProfileBioEntities.from_dict(profile_bio_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


