# NoteTweetResultData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_set** | [**Entities**](Entities.md) |  | 
**id** | **str** |  | 
**media** | [**NoteTweetResultMedia**](NoteTweetResultMedia.md) |  | [optional] 
**richtext** | [**NoteTweetResultRichText**](NoteTweetResultRichText.md) |  | [optional] 
**text** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.note_tweet_result_data import NoteTweetResultData

# TODO update the JSON string below
json = "{}"
# create an instance of NoteTweetResultData from a JSON string
note_tweet_result_data_instance = NoteTweetResultData.from_json(json)
# print the JSON string representation of the object
print(NoteTweetResultData.to_json())

# convert the object into a dict
note_tweet_result_data_dict = note_tweet_result_data_instance.to_dict()
# create an instance of NoteTweetResultData from a dict
note_tweet_result_data_from_dict = NoteTweetResultData.from_dict(note_tweet_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


