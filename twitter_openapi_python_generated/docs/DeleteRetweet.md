# DeleteRetweet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[Retweet]**](Retweet.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.delete_retweet import DeleteRetweet

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRetweet from a JSON string
delete_retweet_instance = DeleteRetweet.from_json(json)
# print the JSON string representation of the object
print DeleteRetweet.to_json()

# convert the object into a dict
delete_retweet_dict = delete_retweet_instance.to_dict()
# create an instance of DeleteRetweet from a dict
delete_retweet_form_dict = delete_retweet.from_dict(delete_retweet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


