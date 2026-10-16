# ListSubscribersList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscribers_timeline** | [**TimelineResult**](TimelineResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.list_subscribers_list import ListSubscribersList

# TODO update the JSON string below
json = "{}"
# create an instance of ListSubscribersList from a JSON string
list_subscribers_list_instance = ListSubscribersList.from_json(json)
# print the JSON string representation of the object
print(ListSubscribersList.to_json())

# convert the object into a dict
list_subscribers_list_dict = list_subscribers_list_instance.to_dict()
# create an instance of ListSubscribersList from a dict
list_subscribers_list_from_dict = ListSubscribersList.from_dict(list_subscribers_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


