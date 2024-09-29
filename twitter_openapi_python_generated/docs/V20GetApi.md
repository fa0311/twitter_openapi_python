# twitter_openapi_python_generated.V20GetApi

All URIs are relative to *https://x.com/i/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_search_adaptive**](V20GetApi.md#get_search_adaptive) | **GET** /2/search/adaptive.json | 


# **get_search_adaptive**
> get_search_adaptive(include_profile_interstitial_type, include_blocking, include_blocked_by, include_followed_by, include_want_retweets, include_mute_edge, include_can_dm, include_can_media_tag, include_ext_has_nft_avatar, include_ext_is_blue_verified, include_ext_verified_type, include_ext_profile_image_shape, skip_status, cards_platform, include_cards, include_ext_alt_text, include_ext_limited_action_results, include_quote_count, include_reply_count, tweet_mode, include_ext_views, include_entities, include_user_entities, include_ext_media_color, include_ext_media_availability, include_ext_sensitive_media_warning, include_ext_trusted_friends_metadata, send_error_codes, simple_quoted_tweet, q, query_source, count, request_context, pc, spelling_corrections, include_ext_edit_control, ext)



get search adaptive

### Example

* Api Key Authentication (ClientLanguage):
* Api Key Authentication (Accept):
* Api Key Authentication (Priority):
* Api Key Authentication (SecFetchDest):
* Api Key Authentication (Referer):
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
* Api Key Authentication (SecChUaMobile):
* Api Key Authentication (AcceptEncoding):

```python
import twitter_openapi_python_generated
from twitter_openapi_python_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://x.com/i/api
# See configuration.py for a list of all supported configuration parameters.
configuration = twitter_openapi_python_generated.Configuration(
    host = "https://x.com/i/api"
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

# Configure API key authorization: Priority
configuration.api_key['Priority'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Priority'] = 'Bearer'

# Configure API key authorization: SecFetchDest
configuration.api_key['SecFetchDest'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecFetchDest'] = 'Bearer'

# Configure API key authorization: Referer
configuration.api_key['Referer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Referer'] = 'Bearer'

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
    api_instance = twitter_openapi_python_generated.V20GetApi(api_client)
    include_profile_interstitial_type = 1 # int |  (default to 1)
    include_blocking = 1 # int |  (default to 1)
    include_blocked_by = 1 # int |  (default to 1)
    include_followed_by = 1 # int |  (default to 1)
    include_want_retweets = 1 # int |  (default to 1)
    include_mute_edge = 1 # int |  (default to 1)
    include_can_dm = 1 # int |  (default to 1)
    include_can_media_tag = 1 # int |  (default to 1)
    include_ext_has_nft_avatar = 1 # int |  (default to 1)
    include_ext_is_blue_verified = 1 # int |  (default to 1)
    include_ext_verified_type = 1 # int |  (default to 1)
    include_ext_profile_image_shape = 1 # int |  (default to 1)
    skip_status = 1 # int |  (default to 1)
    cards_platform = 'Web-12' # str |  (default to 'Web-12')
    include_cards = 1 # int |  (default to 1)
    include_ext_alt_text = True # bool |  (default to True)
    include_ext_limited_action_results = False # bool |  (default to False)
    include_quote_count = True # bool |  (default to True)
    include_reply_count = 1 # int |  (default to 1)
    tweet_mode = 'extended' # str |  (default to 'extended')
    include_ext_views = True # bool |  (default to True)
    include_entities = True # bool |  (default to True)
    include_user_entities = True # bool |  (default to True)
    include_ext_media_color = True # bool |  (default to True)
    include_ext_media_availability = True # bool |  (default to True)
    include_ext_sensitive_media_warning = True # bool |  (default to True)
    include_ext_trusted_friends_metadata = True # bool |  (default to True)
    send_error_codes = True # bool |  (default to True)
    simple_quoted_tweet = True # bool |  (default to True)
    q = 'elon musk' # str |  (default to 'elon musk')
    query_source = 'trend_click' # str |  (default to 'trend_click')
    count = 20 # int |  (default to 20)
    request_context = 'launch' # str |  (default to 'launch')
    pc = 1 # int |  (default to 1)
    spelling_corrections = 1 # int |  (default to 1)
    include_ext_edit_control = True # bool |  (default to True)
    ext = 'mediaStats,highlightedLabel,hasNftAvatar,voiceInfo,birdwatchPivot,enrichments,superFollowMetadata,unmentionInfo,editControl,vibe' # str |  (default to 'mediaStats,highlightedLabel,hasNftAvatar,voiceInfo,birdwatchPivot,enrichments,superFollowMetadata,unmentionInfo,editControl,vibe')

    try:
        api_instance.get_search_adaptive(include_profile_interstitial_type, include_blocking, include_blocked_by, include_followed_by, include_want_retweets, include_mute_edge, include_can_dm, include_can_media_tag, include_ext_has_nft_avatar, include_ext_is_blue_verified, include_ext_verified_type, include_ext_profile_image_shape, skip_status, cards_platform, include_cards, include_ext_alt_text, include_ext_limited_action_results, include_quote_count, include_reply_count, tweet_mode, include_ext_views, include_entities, include_user_entities, include_ext_media_color, include_ext_media_availability, include_ext_sensitive_media_warning, include_ext_trusted_friends_metadata, send_error_codes, simple_quoted_tweet, q, query_source, count, request_context, pc, spelling_corrections, include_ext_edit_control, ext)
    except Exception as e:
        print("Exception when calling V20GetApi->get_search_adaptive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_profile_interstitial_type** | **int**|  | [default to 1]
 **include_blocking** | **int**|  | [default to 1]
 **include_blocked_by** | **int**|  | [default to 1]
 **include_followed_by** | **int**|  | [default to 1]
 **include_want_retweets** | **int**|  | [default to 1]
 **include_mute_edge** | **int**|  | [default to 1]
 **include_can_dm** | **int**|  | [default to 1]
 **include_can_media_tag** | **int**|  | [default to 1]
 **include_ext_has_nft_avatar** | **int**|  | [default to 1]
 **include_ext_is_blue_verified** | **int**|  | [default to 1]
 **include_ext_verified_type** | **int**|  | [default to 1]
 **include_ext_profile_image_shape** | **int**|  | [default to 1]
 **skip_status** | **int**|  | [default to 1]
 **cards_platform** | **str**|  | [default to &#39;Web-12&#39;]
 **include_cards** | **int**|  | [default to 1]
 **include_ext_alt_text** | **bool**|  | [default to True]
 **include_ext_limited_action_results** | **bool**|  | [default to False]
 **include_quote_count** | **bool**|  | [default to True]
 **include_reply_count** | **int**|  | [default to 1]
 **tweet_mode** | **str**|  | [default to &#39;extended&#39;]
 **include_ext_views** | **bool**|  | [default to True]
 **include_entities** | **bool**|  | [default to True]
 **include_user_entities** | **bool**|  | [default to True]
 **include_ext_media_color** | **bool**|  | [default to True]
 **include_ext_media_availability** | **bool**|  | [default to True]
 **include_ext_sensitive_media_warning** | **bool**|  | [default to True]
 **include_ext_trusted_friends_metadata** | **bool**|  | [default to True]
 **send_error_codes** | **bool**|  | [default to True]
 **simple_quoted_tweet** | **bool**|  | [default to True]
 **q** | **str**|  | [default to &#39;elon musk&#39;]
 **query_source** | **str**|  | [default to &#39;trend_click&#39;]
 **count** | **int**|  | [default to 20]
 **request_context** | **str**|  | [default to &#39;launch&#39;]
 **pc** | **int**|  | [default to 1]
 **spelling_corrections** | **int**|  | [default to 1]
 **include_ext_edit_control** | **bool**|  | [default to True]
 **ext** | **str**|  | [default to &#39;mediaStats,highlightedLabel,hasNftAvatar,voiceInfo,birdwatchPivot,enrichments,superFollowMetadata,unmentionInfo,editControl,vibe&#39;]

### Return type

void (empty response body)

### Authorization

[ClientLanguage](../README.md#ClientLanguage), [Accept](../README.md#Accept), [Priority](../README.md#Priority), [SecFetchDest](../README.md#SecFetchDest), [Referer](../README.md#Referer), [SecChUaPlatform](../README.md#SecChUaPlatform), [SecFetchMode](../README.md#SecFetchMode), [CsrfToken](../README.md#CsrfToken), [GuestToken](../README.md#GuestToken), [BearerAuth](../README.md#BearerAuth), [SecChUa](../README.md#SecChUa), [CookieCt0](../README.md#CookieCt0), [ActiveUser](../README.md#ActiveUser), [UserAgent](../README.md#UserAgent), [AcceptLanguage](../README.md#AcceptLanguage), [SecFetchSite](../README.md#SecFetchSite), [CookieAuthToken](../README.md#CookieAuthToken), [AuthType](../README.md#AuthType), [SecChUaMobile](../README.md#SecChUaMobile), [AcceptEncoding](../README.md#AcceptEncoding)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * status -  <br>  * x-access-level -  <br>  * x-client-event-enabled -  <br>  * x-connection-hash -  <br>  * x-content-type-options -  <br>  * x-response-time -  <br>  * x-transaction -  <br>  * x-transaction-id -  <br>  * x-twitter-response-tags -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

