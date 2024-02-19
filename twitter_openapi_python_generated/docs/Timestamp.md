# Timestamp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **List[int]** |  | 
**seconds** | **int** |  | 
**text** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.timestamp import Timestamp

# TODO update the JSON string below
json = "{}"
# create an instance of Timestamp from a JSON string
timestamp_instance = Timestamp.from_json(json)
# print the JSON string representation of the object
print Timestamp.to_json()

# convert the object into a dict
timestamp_dict = timestamp_instance.to_dict()
# create an instance of Timestamp from a dict
timestamp_form_dict = timestamp.from_dict(timestamp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


