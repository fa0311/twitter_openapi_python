# CreateBookmarkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateBookmarkResponseData**](CreateBookmarkResponseData.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.create_bookmark_response import CreateBookmarkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBookmarkResponse from a JSON string
create_bookmark_response_instance = CreateBookmarkResponse.from_json(json)
# print the JSON string representation of the object
print(CreateBookmarkResponse.to_json())

# convert the object into a dict
create_bookmark_response_dict = create_bookmark_response_instance.to_dict()
# create an instance of CreateBookmarkResponse from a dict
create_bookmark_response_from_dict = CreateBookmarkResponse.from_dict(create_bookmark_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


