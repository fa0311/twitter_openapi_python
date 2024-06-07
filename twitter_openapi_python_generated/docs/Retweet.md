# Retweet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legacy** | [**RetweetLegacy**](RetweetLegacy.md) |  | 
**rest_id** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.retweet import Retweet

# TODO update the JSON string below
json = "{}"
# create an instance of Retweet from a JSON string
retweet_instance = Retweet.from_json(json)
# print the JSON string representation of the object
print(Retweet.to_json())

# convert the object into a dict
retweet_dict = retweet_instance.to_dict()
# create an instance of Retweet from a dict
retweet_from_dict = Retweet.from_dict(retweet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


