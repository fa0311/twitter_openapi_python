# TimelineNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**id** | **str** |  | 
**item_type** | [**ContentItemType**](ContentItemType.md) |  | 
**notification_icon** | **str** |  | 
**notification_url** | [**SocialContextLandingUrl**](SocialContextLandingUrl.md) |  | 
**rich_message** | [**RichMessage**](RichMessage.md) |  | 
**template** | [**NotificationTemplate**](NotificationTemplate.md) |  | 
**timestamp_ms** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_notification import TimelineNotification

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineNotification from a JSON string
timeline_notification_instance = TimelineNotification.from_json(json)
# print the JSON string representation of the object
print(TimelineNotification.to_json())

# convert the object into a dict
timeline_notification_dict = timeline_notification_instance.to_dict()
# create an instance of TimelineNotification from a dict
timeline_notification_from_dict = TimelineNotification.from_dict(timeline_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


