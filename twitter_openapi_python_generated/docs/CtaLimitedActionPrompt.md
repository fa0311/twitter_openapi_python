# CtaLimitedActionPrompt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**cta_type** | **str** |  | 
**headline** | [**CtaLimitedActionPromptText**](CtaLimitedActionPromptText.md) |  | 
**subtext** | [**CtaLimitedActionPromptText**](CtaLimitedActionPromptText.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.cta_limited_action_prompt import CtaLimitedActionPrompt

# TODO update the JSON string below
json = "{}"
# create an instance of CtaLimitedActionPrompt from a JSON string
cta_limited_action_prompt_instance = CtaLimitedActionPrompt.from_json(json)
# print the JSON string representation of the object
print(CtaLimitedActionPrompt.to_json())

# convert the object into a dict
cta_limited_action_prompt_dict = cta_limited_action_prompt_instance.to_dict()
# create an instance of CtaLimitedActionPrompt from a dict
cta_limited_action_prompt_from_dict = CtaLimitedActionPrompt.from_dict(cta_limited_action_prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


