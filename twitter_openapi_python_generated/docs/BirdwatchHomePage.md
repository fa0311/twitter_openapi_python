# BirdwatchHomePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**BirdwatchHomePageBody**](BirdwatchHomePageBody.md) |  | 
**id** | **str** |  | 
**scribe_config** | [**ScribeConfig**](ScribeConfig.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.birdwatch_home_page import BirdwatchHomePage

# TODO update the JSON string below
json = "{}"
# create an instance of BirdwatchHomePage from a JSON string
birdwatch_home_page_instance = BirdwatchHomePage.from_json(json)
# print the JSON string representation of the object
print(BirdwatchHomePage.to_json())

# convert the object into a dict
birdwatch_home_page_dict = birdwatch_home_page_instance.to_dict()
# create an instance of BirdwatchHomePage from a dict
birdwatch_home_page_from_dict = BirdwatchHomePage.from_dict(birdwatch_home_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


