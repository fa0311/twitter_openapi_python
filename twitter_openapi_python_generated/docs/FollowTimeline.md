# FollowTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeline** | [**Timeline**](Timeline.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.follow_timeline import FollowTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of FollowTimeline from a JSON string
follow_timeline_instance = FollowTimeline.from_json(json)
# print the JSON string representation of the object
print(FollowTimeline.to_json())

# convert the object into a dict
follow_timeline_dict = follow_timeline_instance.to_dict()
# create an instance of FollowTimeline from a dict
follow_timeline_form_dict = follow_timeline.from_dict(follow_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


