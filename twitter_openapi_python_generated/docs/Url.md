# Url


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_url** | **str** |  | 
**expanded_url** | **str** |  | 
**indices** | **List[int]** |  | 
**url** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.url import Url

# TODO update the JSON string below
json = "{}"
# create an instance of Url from a JSON string
url_instance = Url.from_json(json)
# print the JSON string representation of the object
print Url.to_json()

# convert the object into a dict
url_dict = url_instance.to_dict()
# create an instance of Url from a dict
url_form_dict = url.from_dict(url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


