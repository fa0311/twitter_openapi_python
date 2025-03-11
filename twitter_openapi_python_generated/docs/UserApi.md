# twitter_openapi_python_generated.UserApi

All URIs are relative to *https://x.com/i/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_by_rest_id**](UserApi.md#get_user_by_rest_id) | **GET** /graphql/{pathQueryId}/UserByRestId | 
[**get_user_by_screen_name**](UserApi.md#get_user_by_screen_name) | **GET** /graphql/{pathQueryId}/UserByScreenName | 


# **get_user_by_rest_id**
> UserResponse get_user_by_rest_id(path_query_id, variables, features)

get user by rest id

### Example

* Api Key Authentication (Accept):
* Api Key Authentication (ClientLanguage):
* Api Key Authentication (Priority):
* Api Key Authentication (Referer):
* Api Key Authentication (SecFetchDest):
* Api Key Authentication (SecChUaPlatform):
* Api Key Authentication (SecFetchMode):
* Api Key Authentication (CsrfToken):
* Api Key Authentication (ClientUuid):
* Bearer Authentication (BearerAuth):
* Api Key Authentication (GuestToken):
* Api Key Authentication (SecChUa):
* Api Key Authentication (CookieGt0):
* Api Key Authentication (ClientTransactionId):
* Api Key Authentication (ActiveUser):
* Api Key Authentication (CookieCt0):
* Api Key Authentication (UserAgent):
* Api Key Authentication (AcceptLanguage):
* Api Key Authentication (SecFetchSite):
* Api Key Authentication (AuthType):
* Api Key Authentication (CookieAuthToken):
* Api Key Authentication (SecChUaMobile):
* Api Key Authentication (AcceptEncoding):

```python
import twitter_openapi_python_generated
from twitter_openapi_python_generated.models.user_response import UserResponse
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

# Configure API key authorization: Accept
configuration.api_key['Accept'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Accept'] = 'Bearer'

# Configure API key authorization: ClientLanguage
configuration.api_key['ClientLanguage'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ClientLanguage'] = 'Bearer'

# Configure API key authorization: Priority
configuration.api_key['Priority'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Priority'] = 'Bearer'

# Configure API key authorization: Referer
configuration.api_key['Referer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Referer'] = 'Bearer'

# Configure API key authorization: SecFetchDest
configuration.api_key['SecFetchDest'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecFetchDest'] = 'Bearer'

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

# Configure API key authorization: ClientUuid
configuration.api_key['ClientUuid'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ClientUuid'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = twitter_openapi_python_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: GuestToken
configuration.api_key['GuestToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GuestToken'] = 'Bearer'

# Configure API key authorization: SecChUa
configuration.api_key['SecChUa'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecChUa'] = 'Bearer'

# Configure API key authorization: CookieGt0
configuration.api_key['CookieGt0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieGt0'] = 'Bearer'

# Configure API key authorization: ClientTransactionId
configuration.api_key['ClientTransactionId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ClientTransactionId'] = 'Bearer'

# Configure API key authorization: ActiveUser
configuration.api_key['ActiveUser'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ActiveUser'] = 'Bearer'

# Configure API key authorization: CookieCt0
configuration.api_key['CookieCt0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieCt0'] = 'Bearer'

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

# Configure API key authorization: AuthType
configuration.api_key['AuthType'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthType'] = 'Bearer'

# Configure API key authorization: CookieAuthToken
configuration.api_key['CookieAuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieAuthToken'] = 'Bearer'

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
    api_instance = twitter_openapi_python_generated.UserApi(api_client)
    path_query_id = 'tD8zKvQzwY3kdx5yz6YmOw' # str |  (default to 'tD8zKvQzwY3kdx5yz6YmOw')
    variables = '{"userId": "44196397", "withSafetyModeUserFields": true}' # str |  (default to '{"userId": "44196397", "withSafetyModeUserFields": true}')
    features = '{"hidden_profile_likes_enabled": true, "hidden_profile_subscriptions_enabled": true, "responsive_web_graphql_exclude_directive_enabled": true, "verified_phone_label_enabled": false, "highlights_tweets_tab_ui_enabled": true, "responsive_web_twitter_article_notes_tab_enabled": true, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "responsive_web_graphql_timeline_navigation_enabled": true}' # str |  (default to '{"hidden_profile_likes_enabled": true, "hidden_profile_subscriptions_enabled": true, "responsive_web_graphql_exclude_directive_enabled": true, "verified_phone_label_enabled": false, "highlights_tweets_tab_ui_enabled": true, "responsive_web_twitter_article_notes_tab_enabled": true, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "responsive_web_graphql_timeline_navigation_enabled": true}')

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
 **path_query_id** | **str**|  | [default to &#39;tD8zKvQzwY3kdx5yz6YmOw&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;userId&quot;: &quot;44196397&quot;, &quot;withSafetyModeUserFields&quot;: true}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;hidden_profile_likes_enabled&quot;: true, &quot;hidden_profile_subscriptions_enabled&quot;: true, &quot;responsive_web_graphql_exclude_directive_enabled&quot;: true, &quot;verified_phone_label_enabled&quot;: false, &quot;highlights_tweets_tab_ui_enabled&quot;: true, &quot;responsive_web_twitter_article_notes_tab_enabled&quot;: true, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true}&#39;]

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[Accept](../README.md#Accept), [ClientLanguage](../README.md#ClientLanguage), [Priority](../README.md#Priority), [Referer](../README.md#Referer), [SecFetchDest](../README.md#SecFetchDest), [SecChUaPlatform](../README.md#SecChUaPlatform), [SecFetchMode](../README.md#SecFetchMode), [CsrfToken](../README.md#CsrfToken), [ClientUuid](../README.md#ClientUuid), [BearerAuth](../README.md#BearerAuth), [GuestToken](../README.md#GuestToken), [SecChUa](../README.md#SecChUa), [CookieGt0](../README.md#CookieGt0), [ClientTransactionId](../README.md#ClientTransactionId), [ActiveUser](../README.md#ActiveUser), [CookieCt0](../README.md#CookieCt0), [UserAgent](../README.md#UserAgent), [AcceptLanguage](../README.md#AcceptLanguage), [SecFetchSite](../README.md#SecFetchSite), [AuthType](../README.md#AuthType), [CookieAuthToken](../README.md#CookieAuthToken), [SecChUaMobile](../README.md#SecChUaMobile), [AcceptEncoding](../README.md#AcceptEncoding)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * x-connection-hash -  <br>  * x-rate-limit-limit -  <br>  * x-rate-limit-remaining -  <br>  * x-rate-limit-reset -  <br>  * x-response-time -  <br>  * x-tfe-preserve-body -  <br>  * x-transaction-id -  <br>  * x-twitter-response-tags -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_screen_name**
> UserResponse get_user_by_screen_name(path_query_id, variables, features, field_toggles)

get user by screen name

### Example

* Api Key Authentication (Accept):
* Api Key Authentication (ClientLanguage):
* Api Key Authentication (Priority):
* Api Key Authentication (Referer):
* Api Key Authentication (SecFetchDest):
* Api Key Authentication (SecChUaPlatform):
* Api Key Authentication (SecFetchMode):
* Api Key Authentication (CsrfToken):
* Api Key Authentication (ClientUuid):
* Bearer Authentication (BearerAuth):
* Api Key Authentication (GuestToken):
* Api Key Authentication (SecChUa):
* Api Key Authentication (CookieGt0):
* Api Key Authentication (ClientTransactionId):
* Api Key Authentication (ActiveUser):
* Api Key Authentication (CookieCt0):
* Api Key Authentication (UserAgent):
* Api Key Authentication (AcceptLanguage):
* Api Key Authentication (SecFetchSite):
* Api Key Authentication (AuthType):
* Api Key Authentication (CookieAuthToken):
* Api Key Authentication (SecChUaMobile):
* Api Key Authentication (AcceptEncoding):

```python
import twitter_openapi_python_generated
from twitter_openapi_python_generated.models.user_response import UserResponse
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

# Configure API key authorization: Accept
configuration.api_key['Accept'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Accept'] = 'Bearer'

# Configure API key authorization: ClientLanguage
configuration.api_key['ClientLanguage'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ClientLanguage'] = 'Bearer'

# Configure API key authorization: Priority
configuration.api_key['Priority'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Priority'] = 'Bearer'

# Configure API key authorization: Referer
configuration.api_key['Referer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Referer'] = 'Bearer'

# Configure API key authorization: SecFetchDest
configuration.api_key['SecFetchDest'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecFetchDest'] = 'Bearer'

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

# Configure API key authorization: ClientUuid
configuration.api_key['ClientUuid'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ClientUuid'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = twitter_openapi_python_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: GuestToken
configuration.api_key['GuestToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['GuestToken'] = 'Bearer'

# Configure API key authorization: SecChUa
configuration.api_key['SecChUa'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SecChUa'] = 'Bearer'

# Configure API key authorization: CookieGt0
configuration.api_key['CookieGt0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieGt0'] = 'Bearer'

# Configure API key authorization: ClientTransactionId
configuration.api_key['ClientTransactionId'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ClientTransactionId'] = 'Bearer'

# Configure API key authorization: ActiveUser
configuration.api_key['ActiveUser'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ActiveUser'] = 'Bearer'

# Configure API key authorization: CookieCt0
configuration.api_key['CookieCt0'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieCt0'] = 'Bearer'

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

# Configure API key authorization: AuthType
configuration.api_key['AuthType'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthType'] = 'Bearer'

# Configure API key authorization: CookieAuthToken
configuration.api_key['CookieAuthToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieAuthToken'] = 'Bearer'

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
    api_instance = twitter_openapi_python_generated.UserApi(api_client)
    path_query_id = '32pL5BWe9WKeSK1MoPvFQQ' # str |  (default to '32pL5BWe9WKeSK1MoPvFQQ')
    variables = '{"screen_name": "elonmusk"}' # str |  (default to '{"screen_name": "elonmusk"}')
    features = '{"hidden_profile_subscriptions_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "rweb_tipjar_consumption_enabled": true, "responsive_web_graphql_exclude_directive_enabled": true, "verified_phone_label_enabled": false, "subscriptions_verification_info_is_identity_verified_enabled": true, "subscriptions_verification_info_verified_since_enabled": true, "highlights_tweets_tab_ui_enabled": true, "responsive_web_twitter_article_notes_tab_enabled": true, "subscriptions_feature_can_gift_premium": true, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "responsive_web_graphql_timeline_navigation_enabled": true}' # str |  (default to '{"hidden_profile_subscriptions_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "rweb_tipjar_consumption_enabled": true, "responsive_web_graphql_exclude_directive_enabled": true, "verified_phone_label_enabled": false, "subscriptions_verification_info_is_identity_verified_enabled": true, "subscriptions_verification_info_verified_since_enabled": true, "highlights_tweets_tab_ui_enabled": true, "responsive_web_twitter_article_notes_tab_enabled": true, "subscriptions_feature_can_gift_premium": true, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "responsive_web_graphql_timeline_navigation_enabled": true}')
    field_toggles = '{"withAuxiliaryUserLabels": false}' # str |  (default to '{"withAuxiliaryUserLabels": false}')

    try:
        api_response = api_instance.get_user_by_screen_name(path_query_id, variables, features, field_toggles)
        print("The response of UserApi->get_user_by_screen_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_by_screen_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;32pL5BWe9WKeSK1MoPvFQQ&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;screen_name&quot;: &quot;elonmusk&quot;}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;hidden_profile_subscriptions_enabled&quot;: true, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;rweb_tipjar_consumption_enabled&quot;: true, &quot;responsive_web_graphql_exclude_directive_enabled&quot;: true, &quot;verified_phone_label_enabled&quot;: false, &quot;subscriptions_verification_info_is_identity_verified_enabled&quot;: true, &quot;subscriptions_verification_info_verified_since_enabled&quot;: true, &quot;highlights_tweets_tab_ui_enabled&quot;: true, &quot;responsive_web_twitter_article_notes_tab_enabled&quot;: true, &quot;subscriptions_feature_can_gift_premium&quot;: true, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true}&#39;]
 **field_toggles** | **str**|  | [default to &#39;{&quot;withAuxiliaryUserLabels&quot;: false}&#39;]

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[Accept](../README.md#Accept), [ClientLanguage](../README.md#ClientLanguage), [Priority](../README.md#Priority), [Referer](../README.md#Referer), [SecFetchDest](../README.md#SecFetchDest), [SecChUaPlatform](../README.md#SecChUaPlatform), [SecFetchMode](../README.md#SecFetchMode), [CsrfToken](../README.md#CsrfToken), [ClientUuid](../README.md#ClientUuid), [BearerAuth](../README.md#BearerAuth), [GuestToken](../README.md#GuestToken), [SecChUa](../README.md#SecChUa), [CookieGt0](../README.md#CookieGt0), [ClientTransactionId](../README.md#ClientTransactionId), [ActiveUser](../README.md#ActiveUser), [CookieCt0](../README.md#CookieCt0), [UserAgent](../README.md#UserAgent), [AcceptLanguage](../README.md#AcceptLanguage), [SecFetchSite](../README.md#SecFetchSite), [AuthType](../README.md#AuthType), [CookieAuthToken](../README.md#CookieAuthToken), [SecChUaMobile](../README.md#SecChUaMobile), [AcceptEncoding](../README.md#AcceptEncoding)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * x-connection-hash -  <br>  * x-rate-limit-limit -  <br>  * x-rate-limit-remaining -  <br>  * x-rate-limit-reset -  <br>  * x-response-time -  <br>  * x-tfe-preserve-body -  <br>  * x-transaction-id -  <br>  * x-twitter-response-tags -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

