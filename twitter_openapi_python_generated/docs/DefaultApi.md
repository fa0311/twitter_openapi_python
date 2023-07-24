# twitter_openapi_python_generated.DefaultApi

All URIs are relative to *https://twitter.com/i/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_profile_spotlights_query**](DefaultApi.md#get_profile_spotlights_query) | **GET** /graphql/{pathQueryId}/ProfileSpotlightsQuery | 


# **get_profile_spotlights_query**
> ProfileResponse get_profile_spotlights_query(path_query_id, variables, features)



get user by screen name

### Example

* Api Key Authentication (ClientLanguage):
* Api Key Authentication (CookieCt0):
* Api Key Authentication (ActiveUser):
* Api Key Authentication (UserAgent):
* Api Key Authentication (CookieAuthToken):
* Api Key Authentication (AuthType):
* Api Key Authentication (CsrfToken):
* Api Key Authentication (GuestToken):
* Bearer Authentication (BearerAuth):
```python
import time
import os
import twitter_openapi_python_generated
from twitter_openapi_python_generated.models.profile_response import ProfileResponse
from twitter_openapi_python_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://twitter.com/i/api
# See configuration.py for a list of all supported configuration parameters.
configuration = twitter_openapi_python_generated.Configuration(
    host = "https://twitter.com/i/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ClientLanguage
configuration.api_key['ClientLanguage'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ClientLanguage'] = 'Bearer'

# Configure API key authorization: CookieCt0
configuration.api_key['CookieCt0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieCt0'] = 'Bearer'

# Configure API key authorization: ActiveUser
configuration.api_key['ActiveUser'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ActiveUser'] = 'Bearer'

# Configure API key authorization: UserAgent
configuration.api_key['UserAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['UserAgent'] = 'Bearer'

# Configure API key authorization: CookieAuthToken
configuration.api_key['CookieAuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieAuthToken'] = 'Bearer'

# Configure API key authorization: AuthType
configuration.api_key['AuthType'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthType'] = 'Bearer'

# Configure API key authorization: CsrfToken
configuration.api_key['CsrfToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CsrfToken'] = 'Bearer'

# Configure API key authorization: GuestToken
configuration.api_key['GuestToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GuestToken'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = twitter_openapi_python_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with twitter_openapi_python_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = twitter_openapi_python_generated.DefaultApi(api_client)
    path_query_id = '9zwVLJ48lmVUk8u_Gh9DmA' # str |  (default to '9zwVLJ48lmVUk8u_Gh9DmA')
    variables = '{"screen_name": "elonmusk"}' # str |  (default to '{"screen_name": "elonmusk"}')
    features = '{}' # str |  (default to '{}')

    try:
        api_response = api_instance.get_profile_spotlights_query(path_query_id, variables, features)
        print("The response of DefaultApi->get_profile_spotlights_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_profile_spotlights_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;9zwVLJ48lmVUk8u_Gh9DmA&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;screen_name&quot;: &quot;elonmusk&quot;}&#39;]
 **features** | **str**|  | [default to &#39;{}&#39;]

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

[ClientLanguage](../README.md#ClientLanguage), [CookieCt0](../README.md#CookieCt0), [ActiveUser](../README.md#ActiveUser), [UserAgent](../README.md#UserAgent), [CookieAuthToken](../README.md#CookieAuthToken), [AuthType](../README.md#AuthType), [CsrfToken](../README.md#CsrfToken), [GuestToken](../README.md#GuestToken), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * x-connection-hash -  <br>  * x-rate-limit-limit -  <br>  * x-rate-limit-remaining -  <br>  * x-rate-limit-reset -  <br>  * x-response-time -  <br>  * x-tfe-preserve-body -  <br>  * x-transaction-id -  <br>  * x-twitter-response-tags -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

