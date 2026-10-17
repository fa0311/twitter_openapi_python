# twitter_openapi_python_generated.DefaultApi

All URIs are relative to *https://x.com/i/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audio_space_by_id**](DefaultApi.md#get_audio_space_by_id) | **GET** /graphql/{pathQueryId}/AudioSpaceById | 
[**get_authenticate_periscope**](DefaultApi.md#get_authenticate_periscope) | **GET** /graphql/{pathQueryId}/AuthenticatePeriscope | 
[**get_broadcast_query**](DefaultApi.md#get_broadcast_query) | **GET** /graphql/{pathQueryId}/BroadcastQuery | 
[**get_creator_studio_tab_bar_item_query**](DefaultApi.md#get_creator_studio_tab_bar_item_query) | **GET** /graphql/{pathQueryId}/CreatorStudioTabBarItemQuery | 
[**get_data_saver_mode**](DefaultApi.md#get_data_saver_mode) | **GET** /graphql/{pathQueryId}/DataSaverMode | 
[**get_grok_account_jwt_query**](DefaultApi.md#get_grok_account_jwt_query) | **GET** /graphql/{pathQueryId}/grokAccountJwtQuery | 
[**get_grok_home**](DefaultApi.md#get_grok_home) | **GET** /graphql/{pathQueryId}/GrokHome | 
[**get_pinned_timelines**](DefaultApi.md#get_pinned_timelines) | **GET** /graphql/{pathQueryId}/PinnedTimelines | 
[**get_profile_spotlights_query**](DefaultApi.md#get_profile_spotlights_query) | **GET** /graphql/{pathQueryId}/ProfileSpotlightsQuery | 
[**get_tweet_result_by_rest_id**](DefaultApi.md#get_tweet_result_by_rest_id) | **GET** /graphql/{pathQueryId}/TweetResultByRestId | 
[**get_use_story_topic_query**](DefaultApi.md#get_use_story_topic_query) | **GET** /graphql/{pathQueryId}/useStoryTopicQuery | 


# **get_audio_space_by_id**
> AudioSpaceResponse get_audio_space_by_id(path_query_id, variables, features)

a Space by id: metadata, participants and the announcing post

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
from twitter_openapi_python_generated.models.audio_space_response import AudioSpaceResponse
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
    api_instance = twitter_openapi_python_generated.DefaultApi(api_client)
    path_query_id = 'sSuYIbdpe1f2v9AtD-sYeQ' # str |  (default to 'sSuYIbdpe1f2v9AtD-sYeQ')
    variables = '{"id": "1qxoNYAlYMXJv", "isMetatagsQuery": true, "withReplays": true, "withListeners": true}' # str |  (default to '{"id": "1qxoNYAlYMXJv", "isMetatagsQuery": true, "withReplays": true, "withListeners": true}')
    features = '{"spaces_2022_h2_spaces_communities": true, "spaces_2022_h2_clipping": true, "creator_subscriptions_tweet_preview_api_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": true, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "rweb_sports_post_context_enabled": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": false, "rweb_cashtags_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_nested_quote_preview_enabled": true, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true}' # str |  (default to '{"spaces_2022_h2_spaces_communities": true, "spaces_2022_h2_clipping": true, "creator_subscriptions_tweet_preview_api_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": true, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "rweb_sports_post_context_enabled": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": false, "rweb_cashtags_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_nested_quote_preview_enabled": true, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true}')

    try:
        api_response = api_instance.get_audio_space_by_id(path_query_id, variables, features)
        print("The response of DefaultApi->get_audio_space_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_audio_space_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;sSuYIbdpe1f2v9AtD-sYeQ&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;id&quot;: &quot;1qxoNYAlYMXJv&quot;, &quot;isMetatagsQuery&quot;: true, &quot;withReplays&quot;: true, &quot;withListeners&quot;: true}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;spaces_2022_h2_spaces_communities&quot;: true, &quot;spaces_2022_h2_clipping&quot;: true, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;responsive_web_profile_redirect_enabled&quot;: true, &quot;rweb_tipjar_consumption_enabled&quot;: false, &quot;verified_phone_label_enabled&quot;: false, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;rweb_cashtags_composer_attachment_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;rweb_sports_post_context_enabled&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;responsive_web_grok_annotations_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;rweb_conversational_replies_downvote_enabled&quot;: false, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;content_disclosure_indicator_enabled&quot;: true, &quot;content_disclosure_ai_generated_indicator_enabled&quot;: true, &quot;responsive_web_grok_show_grok_translated_post&quot;: true, &quot;responsive_web_grok_analysis_button_from_backend&quot;: true, &quot;post_ctas_fetch_enabled&quot;: false, &quot;rweb_cashtags_enabled&quot;: true, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: false, &quot;responsive_web_nested_quote_preview_enabled&quot;: true, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: true}&#39;]

### Return type

[**AudioSpaceResponse**](AudioSpaceResponse.md)

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

# **get_authenticate_periscope**
> AuthenticatePeriscopeResponse get_authenticate_periscope(path_query_id, variables)

a Periscope (live video) token for the account

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
from twitter_openapi_python_generated.models.authenticate_periscope_response import AuthenticatePeriscopeResponse
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
    api_instance = twitter_openapi_python_generated.DefaultApi(api_client)
    path_query_id = 'r7VUmxbfqNkx7uwjgONSNw' # str |  (default to 'r7VUmxbfqNkx7uwjgONSNw')
    variables = '{}' # str |  (default to '{}')

    try:
        api_response = api_instance.get_authenticate_periscope(path_query_id, variables)
        print("The response of DefaultApi->get_authenticate_periscope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_authenticate_periscope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;r7VUmxbfqNkx7uwjgONSNw&#39;]
 **variables** | **str**|  | [default to &#39;{}&#39;]

### Return type

[**AuthenticatePeriscopeResponse**](AuthenticatePeriscopeResponse.md)

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

# **get_broadcast_query**
> BroadcastResponse get_broadcast_query(path_query_id, variables, features)

a live video broadcast by id

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
from twitter_openapi_python_generated.models.broadcast_response import BroadcastResponse
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
    api_instance = twitter_openapi_python_generated.DefaultApi(api_client)
    path_query_id = 'NtEAlAR40O3S7Lf8s6XUTQ' # str |  (default to 'NtEAlAR40O3S7Lf8s6XUTQ')
    variables = '{"id": "1BRKjmPYymWxw"}' # str |  (default to '{"id": "1BRKjmPYymWxw"}')
    features = '{"creator_subscriptions_tweet_preview_api_enabled": true, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "rweb_sports_post_context_enabled": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": true, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": false, "rweb_cashtags_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_nested_quote_preview_enabled": true, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true}' # str |  (default to '{"creator_subscriptions_tweet_preview_api_enabled": true, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "rweb_sports_post_context_enabled": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": true, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": false, "rweb_cashtags_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_nested_quote_preview_enabled": true, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true}')

    try:
        api_response = api_instance.get_broadcast_query(path_query_id, variables, features)
        print("The response of DefaultApi->get_broadcast_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_broadcast_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;NtEAlAR40O3S7Lf8s6XUTQ&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;id&quot;: &quot;1BRKjmPYymWxw&quot;}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;rweb_cashtags_composer_attachment_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;rweb_sports_post_context_enabled&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;responsive_web_grok_annotations_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;responsive_web_profile_redirect_enabled&quot;: true, &quot;rweb_tipjar_consumption_enabled&quot;: false, &quot;verified_phone_label_enabled&quot;: false, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;rweb_conversational_replies_downvote_enabled&quot;: false, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;content_disclosure_indicator_enabled&quot;: true, &quot;content_disclosure_ai_generated_indicator_enabled&quot;: true, &quot;responsive_web_grok_show_grok_translated_post&quot;: true, &quot;responsive_web_grok_analysis_button_from_backend&quot;: true, &quot;post_ctas_fetch_enabled&quot;: false, &quot;rweb_cashtags_enabled&quot;: true, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: false, &quot;responsive_web_nested_quote_preview_enabled&quot;: true, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true}&#39;]

### Return type

[**BroadcastResponse**](BroadcastResponse.md)

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

# **get_creator_studio_tab_bar_item_query**
> CreatorStudioTabBarItemQueryResponse get_creator_studio_tab_bar_item_query(path_query_id, variables)

audience rewards tasks shown in Creator Studio

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
from twitter_openapi_python_generated.models.creator_studio_tab_bar_item_query_response import CreatorStudioTabBarItemQueryResponse
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
    api_instance = twitter_openapi_python_generated.DefaultApi(api_client)
    path_query_id = '1KZj_GRTxmPaSrk8jIb1Yw' # str |  (default to '1KZj_GRTxmPaSrk8jIb1Yw')
    variables = '{}' # str |  (default to '{}')

    try:
        api_response = api_instance.get_creator_studio_tab_bar_item_query(path_query_id, variables)
        print("The response of DefaultApi->get_creator_studio_tab_bar_item_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_creator_studio_tab_bar_item_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;1KZj_GRTxmPaSrk8jIb1Yw&#39;]
 **variables** | **str**|  | [default to &#39;{}&#39;]

### Return type

[**CreatorStudioTabBarItemQueryResponse**](CreatorStudioTabBarItemQueryResponse.md)

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

# **get_data_saver_mode**
> DataSaverModeResponse get_data_saver_mode(path_query_id, variables)

data saver setting of the account

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
from twitter_openapi_python_generated.models.data_saver_mode_response import DataSaverModeResponse
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
    api_instance = twitter_openapi_python_generated.DefaultApi(api_client)
    path_query_id = 'xF6sXnKJfS2AOylzxRjf6A' # str |  (default to 'xF6sXnKJfS2AOylzxRjf6A')
    variables = '{"device_id": "Windows/Chrome"}' # str |  (default to '{"device_id": "Windows/Chrome"}')

    try:
        api_response = api_instance.get_data_saver_mode(path_query_id, variables)
        print("The response of DefaultApi->get_data_saver_mode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_data_saver_mode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;xF6sXnKJfS2AOylzxRjf6A&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;device_id&quot;: &quot;Windows/Chrome&quot;}&#39;]

### Return type

[**DataSaverModeResponse**](DataSaverModeResponse.md)

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

# **get_grok_account_jwt_query**
> GrokAccountJwtResponse get_grok_account_jwt_query(path_query_id, variables)

whether the account is linked to a Grok account

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
from twitter_openapi_python_generated.models.grok_account_jwt_response import GrokAccountJwtResponse
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
    api_instance = twitter_openapi_python_generated.DefaultApi(api_client)
    path_query_id = 'DIW0leeI6-dvMzdOMJki4w' # str |  (default to 'DIW0leeI6-dvMzdOMJki4w')
    variables = '{}' # str |  (default to '{}')

    try:
        api_response = api_instance.get_grok_account_jwt_query(path_query_id, variables)
        print("The response of DefaultApi->get_grok_account_jwt_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_grok_account_jwt_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;DIW0leeI6-dvMzdOMJki4w&#39;]
 **variables** | **str**|  | [default to &#39;{}&#39;]

### Return type

[**GrokAccountJwtResponse**](GrokAccountJwtResponse.md)

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

# **get_grok_home**
> GrokHomeResponse get_grok_home(path_query_id, variables)

Grok home: model options, prompts and eligibility

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
from twitter_openapi_python_generated.models.grok_home_response import GrokHomeResponse
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
    api_instance = twitter_openapi_python_generated.DefaultApi(api_client)
    path_query_id = 'QAPGIKJVaPXYD-gO9kxc9w' # str |  (default to 'QAPGIKJVaPXYD-gO9kxc9w')
    variables = '{}' # str |  (default to '{}')

    try:
        api_response = api_instance.get_grok_home(path_query_id, variables)
        print("The response of DefaultApi->get_grok_home:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_grok_home: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;QAPGIKJVaPXYD-gO9kxc9w&#39;]
 **variables** | **str**|  | [default to &#39;{}&#39;]

### Return type

[**GrokHomeResponse**](GrokHomeResponse.md)

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

# **get_pinned_timelines**
> PinnedTimelinesResponse get_pinned_timelines(path_query_id, features, variables)

the account's pinned timelines

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
from twitter_openapi_python_generated.models.pinned_timelines_response import PinnedTimelinesResponse
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
    api_instance = twitter_openapi_python_generated.DefaultApi(api_client)
    path_query_id = '8J1r9u3VjUveEdTY4WUTwQ' # str |  (default to '8J1r9u3VjUveEdTY4WUTwQ')
    features = '{"profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": true, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "responsive_web_graphql_timeline_navigation_enabled": true}' # str |  (default to '{"profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": true, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "responsive_web_graphql_timeline_navigation_enabled": true}')
    variables = '{}' # str |  (default to '{}')

    try:
        api_response = api_instance.get_pinned_timelines(path_query_id, features, variables)
        print("The response of DefaultApi->get_pinned_timelines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_pinned_timelines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;8J1r9u3VjUveEdTY4WUTwQ&#39;]
 **features** | **str**|  | [default to &#39;{&quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;responsive_web_profile_redirect_enabled&quot;: true, &quot;rweb_tipjar_consumption_enabled&quot;: false, &quot;verified_phone_label_enabled&quot;: false, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true}&#39;]
 **variables** | **str**|  | [default to &#39;{}&#39;]

### Return type

[**PinnedTimelinesResponse**](PinnedTimelinesResponse.md)

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

# **get_profile_spotlights_query**
> ProfileResponse get_profile_spotlights_query(path_query_id, variables, features)

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
from twitter_openapi_python_generated.models.profile_response import ProfileResponse
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
    api_instance = twitter_openapi_python_generated.DefaultApi(api_client)
    path_query_id = 'mzoqrVGwk-YTSGME1dRfXQ' # str |  (default to 'mzoqrVGwk-YTSGME1dRfXQ')
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
 **path_query_id** | **str**|  | [default to &#39;mzoqrVGwk-YTSGME1dRfXQ&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;screen_name&quot;: &quot;elonmusk&quot;}&#39;]
 **features** | **str**|  | [default to &#39;{}&#39;]

### Return type

[**ProfileResponse**](ProfileResponse.md)

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

# **get_tweet_result_by_rest_id**
> TweetResultByRestIdResponse get_tweet_result_by_rest_id(path_query_id, variables, features, field_toggles)

get TweetResultByRestId

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
from twitter_openapi_python_generated.models.tweet_result_by_rest_id_response import TweetResultByRestIdResponse
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
    api_instance = twitter_openapi_python_generated.DefaultApi(api_client)
    path_query_id = 'xZfFqfOmKQu_OXekGI59mg' # str |  (default to 'xZfFqfOmKQu_OXekGI59mg')
    variables = '{"tweetId": "1349129669258448897", "withCommunity": false, "includePromotedContent": false, "withVoice": false, "withBirdwatchNotes": true}' # str |  (default to '{"tweetId": "1349129669258448897", "withCommunity": false, "includePromotedContent": false, "withVoice": false, "withBirdwatchNotes": true}')
    features = '{"creator_subscriptions_tweet_preview_api_enabled": true, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "rweb_sports_post_context_enabled": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": false, "rweb_cashtags_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": true, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "responsive_web_nested_quote_preview_enabled": true, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true}' # str |  (default to '{"creator_subscriptions_tweet_preview_api_enabled": true, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "rweb_sports_post_context_enabled": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": false, "rweb_cashtags_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": true, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "responsive_web_nested_quote_preview_enabled": true, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true}')
    field_toggles = '{"withArticleRichContentState": true, "withArticlePlainText": false, "withArticleSummaryText": true, "withArticleVoiceOver": true, "withPayments": false}' # str |  (default to '{"withArticleRichContentState": true, "withArticlePlainText": false, "withArticleSummaryText": true, "withArticleVoiceOver": true, "withPayments": false}')

    try:
        api_response = api_instance.get_tweet_result_by_rest_id(path_query_id, variables, features, field_toggles)
        print("The response of DefaultApi->get_tweet_result_by_rest_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_tweet_result_by_rest_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;xZfFqfOmKQu_OXekGI59mg&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;tweetId&quot;: &quot;1349129669258448897&quot;, &quot;withCommunity&quot;: false, &quot;includePromotedContent&quot;: false, &quot;withVoice&quot;: false, &quot;withBirdwatchNotes&quot;: true}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;rweb_cashtags_composer_attachment_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;rweb_sports_post_context_enabled&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;responsive_web_grok_annotations_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;rweb_conversational_replies_downvote_enabled&quot;: false, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;content_disclosure_indicator_enabled&quot;: true, &quot;content_disclosure_ai_generated_indicator_enabled&quot;: true, &quot;responsive_web_grok_show_grok_translated_post&quot;: true, &quot;responsive_web_grok_analysis_button_from_backend&quot;: true, &quot;post_ctas_fetch_enabled&quot;: false, &quot;rweb_cashtags_enabled&quot;: true, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: false, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;responsive_web_profile_redirect_enabled&quot;: true, &quot;rweb_tipjar_consumption_enabled&quot;: false, &quot;verified_phone_label_enabled&quot;: false, &quot;responsive_web_nested_quote_preview_enabled&quot;: true, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true}&#39;]
 **field_toggles** | **str**|  | [default to &#39;{&quot;withArticleRichContentState&quot;: true, &quot;withArticlePlainText&quot;: false, &quot;withArticleSummaryText&quot;: true, &quot;withArticleVoiceOver&quot;: true, &quot;withPayments&quot;: false}&#39;]

### Return type

[**TweetResultByRestIdResponse**](TweetResultByRestIdResponse.md)

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

# **get_use_story_topic_query**
> StoryTopicResponse get_use_story_topic_query(path_query_id, variables)

AI-written stories of an explore topic (rest_id: For You)

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
from twitter_openapi_python_generated.models.story_topic_response import StoryTopicResponse
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
    api_instance = twitter_openapi_python_generated.DefaultApi(api_client)
    path_query_id = 'I3V_Tt32aTZdw7cBdKUJbg' # str |  (default to 'I3V_Tt32aTZdw7cBdKUJbg')
    variables = '{"rest_id": "For You", "limit": 3}' # str |  (default to '{"rest_id": "For You", "limit": 3}')

    try:
        api_response = api_instance.get_use_story_topic_query(path_query_id, variables)
        print("The response of DefaultApi->get_use_story_topic_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_use_story_topic_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;I3V_Tt32aTZdw7cBdKUJbg&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;rest_id&quot;: &quot;For You&quot;, &quot;limit&quot;: 3}&#39;]

### Return type

[**StoryTopicResponse**](StoryTopicResponse.md)

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

