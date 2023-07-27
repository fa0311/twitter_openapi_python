# twitter_openapi_python_generated.UserApi

All URIs are relative to *https://twitter.com/i/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_by_rest_id**](UserApi.md#get_user_by_rest_id) | **GET** /graphql/{pathQueryId}/UserByRestId | 
[**get_user_by_screen_name**](UserApi.md#get_user_by_screen_name) | **GET** /graphql/{pathQueryId}/UserByScreenName | 
[**get_users_by_rest_ids**](UserApi.md#get_users_by_rest_ids) | **GET** /graphql/{pathQueryId}/UsersByRestIds | 


# **get_user_by_rest_id**
> UserResponse get_user_by_rest_id(path_query_id, variables, features)



get user by rest id

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
from twitter_openapi_python_generated.models.user_response import UserResponse
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
    api_instance = twitter_openapi_python_generated.UserApi(api_client)
    path_query_id = 'Lxg1V9AiIzzXEiP2c8dRnw' # str |  (default to 'Lxg1V9AiIzzXEiP2c8dRnw')
    variables = '{"userId": "44196397", "withSafetyModeUserFields": true}' # str |  (default to '{"userId": "44196397", "withSafetyModeUserFields": true}')
    features = '{"hidden_profile_likes_enabled": false, "responsive_web_graphql_exclude_directive_enabled": true, "verified_phone_label_enabled": false, "highlights_tweets_tab_ui_enabled": true, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "responsive_web_graphql_timeline_navigation_enabled": true}' # str |  (default to '{"hidden_profile_likes_enabled": false, "responsive_web_graphql_exclude_directive_enabled": true, "verified_phone_label_enabled": false, "highlights_tweets_tab_ui_enabled": true, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "responsive_web_graphql_timeline_navigation_enabled": true}')

    try:
        api_response = api_instance.get_user_by_rest_id(path_query_id, variables, features)
        print("The response of UserApi->get_user_by_rest_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_by_rest_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;Lxg1V9AiIzzXEiP2c8dRnw&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;userId&quot;: &quot;44196397&quot;, &quot;withSafetyModeUserFields&quot;: true}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;hidden_profile_likes_enabled&quot;: false, &quot;responsive_web_graphql_exclude_directive_enabled&quot;: true, &quot;verified_phone_label_enabled&quot;: false, &quot;highlights_tweets_tab_ui_enabled&quot;: true, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true}&#39;]

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_user_by_screen_name**
> UserResponse get_user_by_screen_name(path_query_id, variables, features)



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
from twitter_openapi_python_generated.models.user_response import UserResponse
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
    api_instance = twitter_openapi_python_generated.UserApi(api_client)
    path_query_id = 'sLVLhk0bGj3MVFEKTdax1w' # str |  (default to 'sLVLhk0bGj3MVFEKTdax1w')
    variables = '{"screen_name": "elonmusk", "withSafetyModeUserFields": true}' # str |  (default to '{"screen_name": "elonmusk", "withSafetyModeUserFields": true}')
    features = '{"blue_business_profile_image_shape_enabled": true, "responsive_web_graphql_exclude_directive_enabled": true, "verified_phone_label_enabled": false, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "responsive_web_graphql_timeline_navigation_enabled": true}' # str |  (default to '{"blue_business_profile_image_shape_enabled": true, "responsive_web_graphql_exclude_directive_enabled": true, "verified_phone_label_enabled": false, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "responsive_web_graphql_timeline_navigation_enabled": true}')

    try:
        api_response = api_instance.get_user_by_screen_name(path_query_id, variables, features)
        print("The response of UserApi->get_user_by_screen_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_by_screen_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;sLVLhk0bGj3MVFEKTdax1w&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;screen_name&quot;: &quot;elonmusk&quot;, &quot;withSafetyModeUserFields&quot;: true}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;blue_business_profile_image_shape_enabled&quot;: true, &quot;responsive_web_graphql_exclude_directive_enabled&quot;: true, &quot;verified_phone_label_enabled&quot;: false, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true}&#39;]

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_users_by_rest_ids**
> UsersResponse get_users_by_rest_ids(path_query_id, variables, features)



get users by rest ids

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
from twitter_openapi_python_generated.models.users_response import UsersResponse
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
    api_instance = twitter_openapi_python_generated.UserApi(api_client)
    path_query_id = 'GD4q8bBE2i6cqWw2iT74Gg' # str |  (default to 'GD4q8bBE2i6cqWw2iT74Gg')
    variables = '{"userIds": ["44196397"]}' # str |  (default to '{"userIds": ["44196397"]}')
    features = '{"responsive_web_graphql_exclude_directive_enabled": true, "verified_phone_label_enabled": false, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "responsive_web_graphql_timeline_navigation_enabled": true}' # str |  (default to '{"responsive_web_graphql_exclude_directive_enabled": true, "verified_phone_label_enabled": false, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "responsive_web_graphql_timeline_navigation_enabled": true}')

    try:
        api_response = api_instance.get_users_by_rest_ids(path_query_id, variables, features)
        print("The response of UserApi->get_users_by_rest_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_users_by_rest_ids: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;GD4q8bBE2i6cqWw2iT74Gg&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;userIds&quot;: [&quot;44196397&quot;]}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;responsive_web_graphql_exclude_directive_enabled&quot;: true, &quot;verified_phone_label_enabled&quot;: false, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true}&#39;]

### Return type

[**UsersResponse**](UsersResponse.md)

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

