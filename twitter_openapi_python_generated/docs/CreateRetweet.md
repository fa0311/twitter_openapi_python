# CreateRetweet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Retweet**](Retweet.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.create_retweet import CreateRetweet

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRetweet from a JSON string
create_retweet_instance = CreateRetweet.from_json(json)
# print the JSON string representation of the object
print(CreateRetweet.to_json())

# convert the object into a dict
create_retweet_dict = create_retweet_instance.to_dict()
# create an instance of CreateRetweet from a dict
create_retweet_form_dict = create_retweet.from_dict(create_retweet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


