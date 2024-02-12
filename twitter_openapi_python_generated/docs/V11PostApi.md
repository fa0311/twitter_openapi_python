# twitter_openapi_python_generated.V11PostApi

All URIs are relative to *https://twitter.com/i/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_create_friendships**](V11PostApi.md#post_create_friendships) | **POST** /1.1/friendships/create.json | 
[**post_destroy_friendships**](V11PostApi.md#post_destroy_friendships) | **POST** /1.1/friendships/destroy.json | 


# **post_create_friendships**
> post_create_friendships(include_blocked_by, include_blocking, include_can_dm, include_can_media_tag, include_ext_has_nft_avatar, include_ext_is_blue_verified, include_ext_profile_image_shape, include_ext_verified_type, include_followed_by, include_mute_edge, include_profile_interstitial_type, include_want_retweets, skip_status, user_id)



post create friendships

### Example

* Api Key Authentication (ClientLanguage):
* Api Key Authentication (Accept):
* Api Key Authentication (SecFetchDest):
* Api Key Authentication (Pragma):
* Api Key Authentication (SecChUaPlatform):
* Api Key Authentication (SecFetchMode):
* Api Key Authentication (CsrfToken):
* Api Key Authentication (GuestToken):
* Bearer Authentication (BearerAuth):
* Api Key Authentication (SecChUa):
* Api Key Authentication (CookieCt0):
* Api Key Authentication (ActiveUser):
* Api Key Authentication (UserAgent):
* Api Key Authentication (AcceptLanguage):
* Api Key Authentication (SecFetchSite):
* Api Key Authentication (CookieAuthToken):
* Api Key Authentication (AuthType):
* Api Key Authentication (CacheControl):
* Api Key Authentication (SecChUaMobile):
* Api Key Authentication (AcceptEncoding):

```python
import twitter_openapi_python_generated
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

# Configure API key authorization: Accept
configuration.api_key['Accept'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Accept'] = 'Bearer'

# Configure API key authorization: SecFetchDest
configuration.api_key['SecFetchDest'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecFetchDest'] = 'Bearer'

# Configure API key authorization: Pragma
configuration.api_key['Pragma'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Pragma'] = 'Bearer'

# Configure API key authorization: SecChUaPlatform
configuration.api_key['SecChUaPlatform'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecChUaPlatform'] = 'Bearer'

# Configure API key authorization: SecFetchMode
configuration.api_key['SecFetchMode'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecFetchMode'] = 'Bearer'

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

# Configure API key authorization: SecChUa
configuration.api_key['SecChUa'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecChUa'] = 'Bearer'

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

# Configure API key authorization: AcceptLanguage
configuration.api_key['AcceptLanguage'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AcceptLanguage'] = 'Bearer'

# Configure API key authorization: SecFetchSite
configuration.api_key['SecFetchSite'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecFetchSite'] = 'Bearer'

# Configure API key authorization: CookieAuthToken
configuration.api_key['CookieAuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieAuthToken'] = 'Bearer'

# Configure API key authorization: AuthType
configuration.api_key['AuthType'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthType'] = 'Bearer'

# Configure API key authorization: CacheControl
configuration.api_key['CacheControl'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CacheControl'] = 'Bearer'

# Configure API key authorization: SecChUaMobile
configuration.api_key['SecChUaMobile'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecChUaMobile'] = 'Bearer'

# Configure API key authorization: AcceptEncoding
configuration.api_key['AcceptEncoding'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AcceptEncoding'] = 'Bearer'

# Enter a context with an instance of the API client
with twitter_openapi_python_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = twitter_openapi_python_generated.V11PostApi(api_client)
    include_blocked_by = 1 # int |  (default to 1)
    include_blocking = 1 # int |  (default to 1)
    include_can_dm = 1 # int |  (default to 1)
    include_can_media_tag = 1 # int |  (default to 1)
    include_ext_has_nft_avatar = 1 # int |  (default to 1)
    include_ext_is_blue_verified = 1 # int |  (default to 1)
    include_ext_profile_image_shape = 1 # int |  (default to 1)
    include_ext_verified_type = 1 # int |  (default to 1)
    include_followed_by = 1 # int |  (default to 1)
    include_mute_edge = 1 # int |  (default to 1)
    include_profile_interstitial_type = 1 # int |  (default to 1)
    include_want_retweets = 1 # int |  (default to 1)
    skip_status = 1 # int |  (default to 1)
    user_id = '44196397' # str |  (default to '44196397')

    try:
        api_instance.post_create_friendships(include_blocked_by, include_blocking, include_can_dm, include_can_media_tag, include_ext_has_nft_avatar, include_ext_is_blue_verified, include_ext_profile_image_shape, include_ext_verified_type, include_followed_by, include_mute_edge, include_profile_interstitial_type, include_want_retweets, skip_status, user_id)
    except Exception as e:
        print("Exception when calling V11PostApi->post_create_friendships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_blocked_by** | **int**|  | [default to 1]
 **include_blocking** | **int**|  | [default to 1]
 **include_can_dm** | **int**|  | [default to 1]
 **include_can_media_tag** | **int**|  | [default to 1]
 **include_ext_has_nft_avatar** | **int**|  | [default to 1]
 **include_ext_is_blue_verified** | **int**|  | [default to 1]
 **include_ext_profile_image_shape** | **int**|  | [default to 1]
 **include_ext_verified_type** | **int**|  | [default to 1]
 **include_followed_by** | **int**|  | [default to 1]
 **include_mute_edge** | **int**|  | [default to 1]
 **include_profile_interstitial_type** | **int**|  | [default to 1]
 **include_want_retweets** | **int**|  | [default to 1]
 **skip_status** | **int**|  | [default to 1]
 **user_id** | **str**|  | [default to &#39;44196397&#39;]

### Return type

void (empty response body)

### Authorization

[ClientLanguage](../README.md#ClientLanguage), [Accept](../README.md#Accept), [SecFetchDest](../README.md#SecFetchDest), [Pragma](../README.md#Pragma), [SecChUaPlatform](../README.md#SecChUaPlatform), [SecFetchMode](../README.md#SecFetchMode), [CsrfToken](../README.md#CsrfToken), [GuestToken](../README.md#GuestToken), [BearerAuth](../README.md#BearerAuth), [SecChUa](../README.md#SecChUa), [CookieCt0](../README.md#CookieCt0), [ActiveUser](../README.md#ActiveUser), [UserAgent](../README.md#UserAgent), [AcceptLanguage](../README.md#AcceptLanguage), [SecFetchSite](../README.md#SecFetchSite), [CookieAuthToken](../README.md#CookieAuthToken), [AuthType](../README.md#AuthType), [CacheControl](../README.md#CacheControl), [SecChUaMobile](../README.md#SecChUaMobile), [AcceptEncoding](../README.md#AcceptEncoding)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * status -  <br>  * x-access-level -  <br>  * x-client-event-enabled -  <br>  * x-connection-hash -  <br>  * x-content-type-options -  <br>  * x-response-time -  <br>  * x-transaction -  <br>  * x-transaction-id -  <br>  * x-twitter-response-tags -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_destroy_friendships**
> post_destroy_friendships(include_blocked_by, include_blocking, include_can_dm, include_can_media_tag, include_ext_has_nft_avatar, include_ext_is_blue_verified, include_ext_profile_image_shape, include_ext_verified_type, include_followed_by, include_mute_edge, include_profile_interstitial_type, include_want_retweets, skip_status, user_id)



post destroy friendships

### Example

* Api Key Authentication (ClientLanguage):
* Api Key Authentication (Accept):
* Api Key Authentication (SecFetchDest):
* Api Key Authentication (Pragma):
* Api Key Authentication (SecChUaPlatform):
* Api Key Authentication (SecFetchMode):
* Api Key Authentication (CsrfToken):
* Api Key Authentication (GuestToken):
* Bearer Authentication (BearerAuth):
* Api Key Authentication (SecChUa):
* Api Key Authentication (CookieCt0):
* Api Key Authentication (ActiveUser):
* Api Key Authentication (UserAgent):
* Api Key Authentication (AcceptLanguage):
* Api Key Authentication (SecFetchSite):
* Api Key Authentication (CookieAuthToken):
* Api Key Authentication (AuthType):
* Api Key Authentication (CacheControl):
* Api Key Authentication (SecChUaMobile):
* Api Key Authentication (AcceptEncoding):

```python
import twitter_openapi_python_generated
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

# Configure API key authorization: Accept
configuration.api_key['Accept'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Accept'] = 'Bearer'

# Configure API key authorization: SecFetchDest
configuration.api_key['SecFetchDest'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecFetchDest'] = 'Bearer'

# Configure API key authorization: Pragma
configuration.api_key['Pragma'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Pragma'] = 'Bearer'

# Configure API key authorization: SecChUaPlatform
configuration.api_key['SecChUaPlatform'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecChUaPlatform'] = 'Bearer'

# Configure API key authorization: SecFetchMode
configuration.api_key['SecFetchMode'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecFetchMode'] = 'Bearer'

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

# Configure API key authorization: SecChUa
configuration.api_key['SecChUa'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecChUa'] = 'Bearer'

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

# Configure API key authorization: AcceptLanguage
configuration.api_key['AcceptLanguage'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AcceptLanguage'] = 'Bearer'

# Configure API key authorization: SecFetchSite
configuration.api_key['SecFetchSite'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecFetchSite'] = 'Bearer'

# Configure API key authorization: CookieAuthToken
configuration.api_key['CookieAuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieAuthToken'] = 'Bearer'

# Configure API key authorization: AuthType
configuration.api_key['AuthType'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthType'] = 'Bearer'

# Configure API key authorization: CacheControl
configuration.api_key['CacheControl'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CacheControl'] = 'Bearer'

# Configure API key authorization: SecChUaMobile
configuration.api_key['SecChUaMobile'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecChUaMobile'] = 'Bearer'

# Configure API key authorization: AcceptEncoding
configuration.api_key['AcceptEncoding'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AcceptEncoding'] = 'Bearer'

# Enter a context with an instance of the API client
with twitter_openapi_python_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = twitter_openapi_python_generated.V11PostApi(api_client)
    include_blocked_by = 1 # int |  (default to 1)
    include_blocking = 1 # int |  (default to 1)
    include_can_dm = 1 # int |  (default to 1)
    include_can_media_tag = 1 # int |  (default to 1)
    include_ext_has_nft_avatar = 1 # int |  (default to 1)
    include_ext_is_blue_verified = 1 # int |  (default to 1)
    include_ext_profile_image_shape = 1 # int |  (default to 1)
    include_ext_verified_type = 1 # int |  (default to 1)
    include_followed_by = 1 # int |  (default to 1)
    include_mute_edge = 1 # int |  (default to 1)
    include_profile_interstitial_type = 1 # int |  (default to 1)
    include_want_retweets = 1 # int |  (default to 1)
    skip_status = 1 # int |  (default to 1)
    user_id = '44196397' # str |  (default to '44196397')

    try:
        api_instance.post_destroy_friendships(include_blocked_by, include_blocking, include_can_dm, include_can_media_tag, include_ext_has_nft_avatar, include_ext_is_blue_verified, include_ext_profile_image_shape, include_ext_verified_type, include_followed_by, include_mute_edge, include_profile_interstitial_type, include_want_retweets, skip_status, user_id)
    except Exception as e:
        print("Exception when calling V11PostApi->post_destroy_friendships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_blocked_by** | **int**|  | [default to 1]
 **include_blocking** | **int**|  | [default to 1]
 **include_can_dm** | **int**|  | [default to 1]
 **include_can_media_tag** | **int**|  | [default to 1]
 **include_ext_has_nft_avatar** | **int**|  | [default to 1]
 **include_ext_is_blue_verified** | **int**|  | [default to 1]
 **include_ext_profile_image_shape** | **int**|  | [default to 1]
 **include_ext_verified_type** | **int**|  | [default to 1]
 **include_followed_by** | **int**|  | [default to 1]
 **include_mute_edge** | **int**|  | [default to 1]
 **include_profile_interstitial_type** | **int**|  | [default to 1]
 **include_want_retweets** | **int**|  | [default to 1]
 **skip_status** | **int**|  | [default to 1]
 **user_id** | **str**|  | [default to &#39;44196397&#39;]

### Return type

void (empty response body)

### Authorization

[ClientLanguage](../README.md#ClientLanguage), [Accept](../README.md#Accept), [SecFetchDest](../README.md#SecFetchDest), [Pragma](../README.md#Pragma), [SecChUaPlatform](../README.md#SecChUaPlatform), [SecFetchMode](../README.md#SecFetchMode), [CsrfToken](../README.md#CsrfToken), [GuestToken](../README.md#GuestToken), [BearerAuth](../README.md#BearerAuth), [SecChUa](../README.md#SecChUa), [CookieCt0](../README.md#CookieCt0), [ActiveUser](../README.md#ActiveUser), [UserAgent](../README.md#UserAgent), [AcceptLanguage](../README.md#AcceptLanguage), [SecFetchSite](../README.md#SecFetchSite), [CookieAuthToken](../README.md#CookieAuthToken), [AuthType](../README.md#AuthType), [CacheControl](../README.md#CacheControl), [SecChUaMobile](../README.md#SecChUaMobile), [AcceptEncoding](../README.md#AcceptEncoding)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * status -  <br>  * x-access-level -  <br>  * x-client-event-enabled -  <br>  * x-connection-hash -  <br>  * x-content-type-options -  <br>  * x-response-time -  <br>  * x-transaction -  <br>  * x-transaction-id -  <br>  * x-twitter-response-tags -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

