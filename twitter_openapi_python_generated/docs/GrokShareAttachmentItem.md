# GrokShareAttachmentItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_urls** | **List[str]** |  | 
**message** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.grok_share_attachment_item import GrokShareAttachmentItem

# TODO update the JSON string below
json = "{}"
# create an instance of GrokShareAttachmentItem from a JSON string
grok_share_attachment_item_instance = GrokShareAttachmentItem.from_json(json)
# print the JSON string representation of the object
print(GrokShareAttachmentItem.to_json())

# convert the object into a dict
grok_share_attachment_item_dict = grok_share_attachment_item_instance.to_dict()
# create an instance of GrokShareAttachmentItem from a dict
grok_share_attachment_item_from_dict = GrokShareAttachmentItem.from_dict(grok_share_attachment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


