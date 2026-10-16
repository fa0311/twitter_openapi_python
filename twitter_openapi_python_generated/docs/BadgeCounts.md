# BadgeCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dm_unread_count** | **int** |  | 
**is_from_urt** | **bool** |  | 
**ntab_unread_count** | **int** |  | 
**total_unread_count** | **int** |  | 
**xchat_unread_count** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.badge_counts import BadgeCounts

# TODO update the JSON string below
json = "{}"
# create an instance of BadgeCounts from a JSON string
badge_counts_instance = BadgeCounts.from_json(json)
# print the JSON string representation of the object
print(BadgeCounts.to_json())

# convert the object into a dict
badge_counts_dict = badge_counts_instance.to_dict()
# create an instance of BadgeCounts from a dict
badge_counts_from_dict = BadgeCounts.from_dict(badge_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


