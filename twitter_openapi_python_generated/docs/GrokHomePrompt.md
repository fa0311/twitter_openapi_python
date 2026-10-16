# GrokHomePrompt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_body** | **str** |  | 
**display_label** | **str** |  | 
**filter_key** | **str** |  | 
**icon_name** | **str** |  | 
**prompt** | **str** |  | 
**prompt_id** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.grok_home_prompt import GrokHomePrompt

# TODO update the JSON string below
json = "{}"
# create an instance of GrokHomePrompt from a JSON string
grok_home_prompt_instance = GrokHomePrompt.from_json(json)
# print the JSON string representation of the object
print(GrokHomePrompt.to_json())

# convert the object into a dict
grok_home_prompt_dict = grok_home_prompt_instance.to_dict()
# create an instance of GrokHomePrompt from a dict
grok_home_prompt_from_dict = GrokHomePrompt.from_dict(grok_home_prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


