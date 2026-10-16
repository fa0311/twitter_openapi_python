# DraftTweetsViewer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft_list** | [**DraftList**](DraftList.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.draft_tweets_viewer import DraftTweetsViewer

# TODO update the JSON string below
json = "{}"
# create an instance of DraftTweetsViewer from a JSON string
draft_tweets_viewer_instance = DraftTweetsViewer.from_json(json)
# print the JSON string representation of the object
print(DraftTweetsViewer.to_json())

# convert the object into a dict
draft_tweets_viewer_dict = draft_tweets_viewer_instance.to_dict()
# create an instance of DraftTweetsViewer from a dict
draft_tweets_viewer_from_dict = DraftTweetsViewer.from_dict(draft_tweets_viewer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


