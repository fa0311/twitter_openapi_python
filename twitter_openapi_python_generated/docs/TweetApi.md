# twitter_openapi_python_generated.TweetApi

All URIs are relative to *https://x.com/i/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bookmarks**](TweetApi.md#get_bookmarks) | **GET** /graphql/{pathQueryId}/Bookmarks | 
[**get_community_about_timeline**](TweetApi.md#get_community_about_timeline) | **GET** /graphql/{pathQueryId}/CommunityAboutTimeline | 
[**get_community_media_timeline**](TweetApi.md#get_community_media_timeline) | **GET** /graphql/{pathQueryId}/CommunityMediaTimeline | 
[**get_community_tweets_timeline**](TweetApi.md#get_community_tweets_timeline) | **GET** /graphql/{pathQueryId}/CommunityTweetsTimeline | 
[**get_home_latest_timeline**](TweetApi.md#get_home_latest_timeline) | **GET** /graphql/{pathQueryId}/HomeLatestTimeline | 
[**get_home_timeline**](TweetApi.md#get_home_timeline) | **GET** /graphql/{pathQueryId}/HomeTimeline | 
[**get_likes**](TweetApi.md#get_likes) | **GET** /graphql/{pathQueryId}/Likes | 
[**get_list_latest_tweets_timeline**](TweetApi.md#get_list_latest_tweets_timeline) | **GET** /graphql/{pathQueryId}/ListLatestTweetsTimeline | 
[**get_notifications_timeline**](TweetApi.md#get_notifications_timeline) | **GET** /graphql/{pathQueryId}/NotificationsTimeline | 
[**get_search_timeline**](TweetApi.md#get_search_timeline) | **GET** /graphql/{pathQueryId}/SearchTimeline | 
[**get_tweet_detail**](TweetApi.md#get_tweet_detail) | **GET** /graphql/{pathQueryId}/TweetDetail | 
[**get_user_highlights_tweets**](TweetApi.md#get_user_highlights_tweets) | **GET** /graphql/{pathQueryId}/UserHighlightsTweets | 
[**get_user_media**](TweetApi.md#get_user_media) | **GET** /graphql/{pathQueryId}/UserMedia | 
[**get_user_tweets**](TweetApi.md#get_user_tweets) | **GET** /graphql/{pathQueryId}/UserTweets | 
[**get_user_tweets_and_replies**](TweetApi.md#get_user_tweets_and_replies) | **GET** /graphql/{pathQueryId}/UserTweetsAndReplies | 


# **get_bookmarks**
> BookmarksResponse get_bookmarks(path_query_id, variables, features)

get bookmarks

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
from twitter_openapi_python_generated.models.bookmarks_response import BookmarksResponse
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
    api_instance = twitter_openapi_python_generated.TweetApi(api_client)
    path_query_id = 'XD0ViOeSOW4YoeNTGjVaYw' # str |  (default to 'XD0ViOeSOW4YoeNTGjVaYw')
    variables = '{"count": 20, "includePromotedContent": true}' # str |  (default to '{"count": 20, "includePromotedContent": true}')
    features = '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}' # str |  (default to '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}')

    try:
        api_response = api_instance.get_bookmarks(path_query_id, variables, features)
        print("The response of TweetApi->get_bookmarks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TweetApi->get_bookmarks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;XD0ViOeSOW4YoeNTGjVaYw&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;count&quot;: 20, &quot;includePromotedContent&quot;: true}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;rweb_video_screen_enabled&quot;: false, &quot;rweb_cashtags_enabled&quot;: true, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;responsive_web_profile_redirect_enabled&quot;: false, &quot;rweb_tipjar_consumption_enabled&quot;: false, &quot;verified_phone_label_enabled&quot;: false, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;rweb_cashtags_composer_attachment_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;responsive_web_grok_annotations_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;rweb_conversational_replies_downvote_enabled&quot;: false, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;content_disclosure_indicator_enabled&quot;: true, &quot;content_disclosure_ai_generated_indicator_enabled&quot;: true, &quot;responsive_web_grok_show_grok_translated_post&quot;: true, &quot;responsive_web_grok_analysis_button_from_backend&quot;: true, &quot;post_ctas_fetch_enabled&quot;: true, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: false, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: true, &quot;responsive_web_enhance_cards_enabled&quot;: false}&#39;]

### Return type

[**BookmarksResponse**](BookmarksResponse.md)

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

# **get_community_about_timeline**
> CommunityAboutTimelineResponse get_community_about_timeline(path_query_id, variables, features)

get about of community

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
from twitter_openapi_python_generated.models.community_about_timeline_response import CommunityAboutTimelineResponse
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
    api_instance = twitter_openapi_python_generated.TweetApi(api_client)
    path_query_id = '2k_fZ9eubu6wh1mk-zcHYg' # str |  (default to '2k_fZ9eubu6wh1mk-zcHYg')
    variables = '{"communityId": "1489422448332197888", "withCommunity": true}' # str |  (default to '{"communityId": "1489422448332197888", "withCommunity": true}')
    features = '{"rweb_video_screen_enabled": false, "payments_enabled": false, "rweb_xchat_enabled": false, "profile_label_improvements_pcf_label_in_post_enabled": true, "rweb_tipjar_consumption_enabled": true, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "tweet_awards_web_tipping_enabled": false, "responsive_web_grok_show_grok_translated_post": false, "responsive_web_grok_analysis_button_from_backend": false, "creator_subscriptions_quote_tweet_preview_enabled": false, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": true, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": false, "responsive_web_enhance_cards_enabled": false}' # str |  (default to '{"rweb_video_screen_enabled": false, "payments_enabled": false, "rweb_xchat_enabled": false, "profile_label_improvements_pcf_label_in_post_enabled": true, "rweb_tipjar_consumption_enabled": true, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "tweet_awards_web_tipping_enabled": false, "responsive_web_grok_show_grok_translated_post": false, "responsive_web_grok_analysis_button_from_backend": false, "creator_subscriptions_quote_tweet_preview_enabled": false, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": true, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": false, "responsive_web_enhance_cards_enabled": false}')

    try:
        api_response = api_instance.get_community_about_timeline(path_query_id, variables, features)
        print("The response of TweetApi->get_community_about_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TweetApi->get_community_about_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;2k_fZ9eubu6wh1mk-zcHYg&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;communityId&quot;: &quot;1489422448332197888&quot;, &quot;withCommunity&quot;: true}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;rweb_video_screen_enabled&quot;: false, &quot;payments_enabled&quot;: false, &quot;rweb_xchat_enabled&quot;: false, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;rweb_tipjar_consumption_enabled&quot;: true, &quot;verified_phone_label_enabled&quot;: false, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;tweet_awards_web_tipping_enabled&quot;: false, &quot;responsive_web_grok_show_grok_translated_post&quot;: false, &quot;responsive_web_grok_analysis_button_from_backend&quot;: false, &quot;creator_subscriptions_quote_tweet_preview_enabled&quot;: false, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: true, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: false, &quot;responsive_web_enhance_cards_enabled&quot;: false}&#39;]

### Return type

[**CommunityAboutTimelineResponse**](CommunityAboutTimelineResponse.md)

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

# **get_community_media_timeline**
> CommunityMediaTimelineResponse get_community_media_timeline(path_query_id, variables, features)

get media list of community

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
from twitter_openapi_python_generated.models.community_media_timeline_response import CommunityMediaTimelineResponse
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
    api_instance = twitter_openapi_python_generated.TweetApi(api_client)
    path_query_id = 'ZniZ7AAK_VVu1xtSx1V-gQ' # str |  (default to 'ZniZ7AAK_VVu1xtSx1V-gQ')
    variables = '{"communityId": "1489422448332197888", "count": 20, "withCommunity": true}' # str |  (default to '{"communityId": "1489422448332197888", "count": 20, "withCommunity": true}')
    features = '{"rweb_video_screen_enabled": false, "payments_enabled": false, "rweb_xchat_enabled": false, "profile_label_improvements_pcf_label_in_post_enabled": true, "rweb_tipjar_consumption_enabled": true, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "tweet_awards_web_tipping_enabled": false, "responsive_web_grok_show_grok_translated_post": false, "responsive_web_grok_analysis_button_from_backend": false, "creator_subscriptions_quote_tweet_preview_enabled": false, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": true, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": false, "responsive_web_enhance_cards_enabled": false}' # str |  (default to '{"rweb_video_screen_enabled": false, "payments_enabled": false, "rweb_xchat_enabled": false, "profile_label_improvements_pcf_label_in_post_enabled": true, "rweb_tipjar_consumption_enabled": true, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "tweet_awards_web_tipping_enabled": false, "responsive_web_grok_show_grok_translated_post": false, "responsive_web_grok_analysis_button_from_backend": false, "creator_subscriptions_quote_tweet_preview_enabled": false, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": true, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": false, "responsive_web_enhance_cards_enabled": false}')

    try:
        api_response = api_instance.get_community_media_timeline(path_query_id, variables, features)
        print("The response of TweetApi->get_community_media_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TweetApi->get_community_media_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;ZniZ7AAK_VVu1xtSx1V-gQ&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;communityId&quot;: &quot;1489422448332197888&quot;, &quot;count&quot;: 20, &quot;withCommunity&quot;: true}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;rweb_video_screen_enabled&quot;: false, &quot;payments_enabled&quot;: false, &quot;rweb_xchat_enabled&quot;: false, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;rweb_tipjar_consumption_enabled&quot;: true, &quot;verified_phone_label_enabled&quot;: false, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;tweet_awards_web_tipping_enabled&quot;: false, &quot;responsive_web_grok_show_grok_translated_post&quot;: false, &quot;responsive_web_grok_analysis_button_from_backend&quot;: false, &quot;creator_subscriptions_quote_tweet_preview_enabled&quot;: false, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: true, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: false, &quot;responsive_web_enhance_cards_enabled&quot;: false}&#39;]

### Return type

[**CommunityMediaTimelineResponse**](CommunityMediaTimelineResponse.md)

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

# **get_community_tweets_timeline**
> CommunityTweetsTimelineResponse get_community_tweets_timeline(path_query_id, variables, features)

get tweet list of community. rankingMode:[Recency, Relevance]

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
from twitter_openapi_python_generated.models.community_tweets_timeline_response import CommunityTweetsTimelineResponse
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
    api_instance = twitter_openapi_python_generated.TweetApi(api_client)
    path_query_id = 'PUinTHtCGWmECLX57lhRHA' # str |  (default to 'PUinTHtCGWmECLX57lhRHA')
    variables = '{"communityId": "1489422448332197888", "count": 20, "displayLocation": "Community", "rankingMode": "Relevance", "withCommunity": true}' # str |  (default to '{"communityId": "1489422448332197888", "count": 20, "displayLocation": "Community", "rankingMode": "Relevance", "withCommunity": true}')
    features = '{"rweb_video_screen_enabled": false, "payments_enabled": false, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": true, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "tweet_awards_web_tipping_enabled": false, "responsive_web_grok_show_grok_translated_post": false, "responsive_web_grok_analysis_button_from_backend": true, "creator_subscriptions_quote_tweet_preview_enabled": false, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": true, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": false, "responsive_web_enhance_cards_enabled": false}' # str |  (default to '{"rweb_video_screen_enabled": false, "payments_enabled": false, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": true, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "tweet_awards_web_tipping_enabled": false, "responsive_web_grok_show_grok_translated_post": false, "responsive_web_grok_analysis_button_from_backend": true, "creator_subscriptions_quote_tweet_preview_enabled": false, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": true, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": false, "responsive_web_enhance_cards_enabled": false}')

    try:
        api_response = api_instance.get_community_tweets_timeline(path_query_id, variables, features)
        print("The response of TweetApi->get_community_tweets_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TweetApi->get_community_tweets_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;PUinTHtCGWmECLX57lhRHA&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;communityId&quot;: &quot;1489422448332197888&quot;, &quot;count&quot;: 20, &quot;displayLocation&quot;: &quot;Community&quot;, &quot;rankingMode&quot;: &quot;Relevance&quot;, &quot;withCommunity&quot;: true}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;rweb_video_screen_enabled&quot;: false, &quot;payments_enabled&quot;: false, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;responsive_web_profile_redirect_enabled&quot;: false, &quot;rweb_tipjar_consumption_enabled&quot;: true, &quot;verified_phone_label_enabled&quot;: false, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;tweet_awards_web_tipping_enabled&quot;: false, &quot;responsive_web_grok_show_grok_translated_post&quot;: false, &quot;responsive_web_grok_analysis_button_from_backend&quot;: true, &quot;creator_subscriptions_quote_tweet_preview_enabled&quot;: false, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: true, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: false, &quot;responsive_web_enhance_cards_enabled&quot;: false}&#39;]

### Return type

[**CommunityTweetsTimelineResponse**](CommunityTweetsTimelineResponse.md)

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

# **get_home_latest_timeline**
> TimelineResponse get_home_latest_timeline(path_query_id, variables, features)

get tweet list of timeline

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
from twitter_openapi_python_generated.models.timeline_response import TimelineResponse
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
    api_instance = twitter_openapi_python_generated.TweetApi(api_client)
    path_query_id = '0dateTVgvXjpkf7kyBZy0g' # str |  (default to '0dateTVgvXjpkf7kyBZy0g')
    variables = '{"count": 20, "includePromotedContent": true, "latestControlAvailable": true, "requestContext": "launch", "seenTweetIds": ["1349129669258448897"]}' # str |  (default to '{"count": 20, "includePromotedContent": true, "latestControlAvailable": true, "requestContext": "launch", "seenTweetIds": ["1349129669258448897"]}')
    features = '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}' # str |  (default to '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}')

    try:
        api_response = api_instance.get_home_latest_timeline(path_query_id, variables, features)
        print("The response of TweetApi->get_home_latest_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TweetApi->get_home_latest_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;0dateTVgvXjpkf7kyBZy0g&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;count&quot;: 20, &quot;includePromotedContent&quot;: true, &quot;latestControlAvailable&quot;: true, &quot;requestContext&quot;: &quot;launch&quot;, &quot;seenTweetIds&quot;: [&quot;1349129669258448897&quot;]}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;rweb_video_screen_enabled&quot;: false, &quot;rweb_cashtags_enabled&quot;: true, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;responsive_web_profile_redirect_enabled&quot;: false, &quot;rweb_tipjar_consumption_enabled&quot;: false, &quot;verified_phone_label_enabled&quot;: false, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;rweb_cashtags_composer_attachment_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;responsive_web_grok_annotations_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;rweb_conversational_replies_downvote_enabled&quot;: false, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;content_disclosure_indicator_enabled&quot;: true, &quot;content_disclosure_ai_generated_indicator_enabled&quot;: true, &quot;responsive_web_grok_show_grok_translated_post&quot;: true, &quot;responsive_web_grok_analysis_button_from_backend&quot;: true, &quot;post_ctas_fetch_enabled&quot;: true, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: false, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: true, &quot;responsive_web_enhance_cards_enabled&quot;: false}&#39;]

### Return type

[**TimelineResponse**](TimelineResponse.md)

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

# **get_home_timeline**
> TimelineResponse get_home_timeline(path_query_id, variables, features)

get tweet list of timeline

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
from twitter_openapi_python_generated.models.timeline_response import TimelineResponse
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
    api_instance = twitter_openapi_python_generated.TweetApi(api_client)
    path_query_id = '7zlnp2TxC044W4C1ZUJMHw' # str |  (default to '7zlnp2TxC044W4C1ZUJMHw')
    variables = '{"count": 20, "includePromotedContent": true, "latestControlAvailable": true, "requestContext": "launch", "seenTweetIds": ["1349129669258448897"], "withCommunity": true}' # str |  (default to '{"count": 20, "includePromotedContent": true, "latestControlAvailable": true, "requestContext": "launch", "seenTweetIds": ["1349129669258448897"], "withCommunity": true}')
    features = '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}' # str |  (default to '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}')

    try:
        api_response = api_instance.get_home_timeline(path_query_id, variables, features)
        print("The response of TweetApi->get_home_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TweetApi->get_home_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;7zlnp2TxC044W4C1ZUJMHw&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;count&quot;: 20, &quot;includePromotedContent&quot;: true, &quot;latestControlAvailable&quot;: true, &quot;requestContext&quot;: &quot;launch&quot;, &quot;seenTweetIds&quot;: [&quot;1349129669258448897&quot;], &quot;withCommunity&quot;: true}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;rweb_video_screen_enabled&quot;: false, &quot;rweb_cashtags_enabled&quot;: true, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;responsive_web_profile_redirect_enabled&quot;: false, &quot;rweb_tipjar_consumption_enabled&quot;: false, &quot;verified_phone_label_enabled&quot;: false, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;rweb_cashtags_composer_attachment_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;responsive_web_grok_annotations_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;rweb_conversational_replies_downvote_enabled&quot;: false, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;content_disclosure_indicator_enabled&quot;: true, &quot;content_disclosure_ai_generated_indicator_enabled&quot;: true, &quot;responsive_web_grok_show_grok_translated_post&quot;: true, &quot;responsive_web_grok_analysis_button_from_backend&quot;: true, &quot;post_ctas_fetch_enabled&quot;: true, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: false, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: true, &quot;responsive_web_enhance_cards_enabled&quot;: false}&#39;]

### Return type

[**TimelineResponse**](TimelineResponse.md)

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

# **get_likes**
> UserTweetsResponse get_likes(path_query_id, variables, features, field_toggles)

get user likes tweets

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
from twitter_openapi_python_generated.models.user_tweets_response import UserTweetsResponse
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
    api_instance = twitter_openapi_python_generated.TweetApi(api_client)
    path_query_id = 'rk2aeVVvKsyUdG3jf5uiLw' # str |  (default to 'rk2aeVVvKsyUdG3jf5uiLw')
    variables = '{"userId": "44196397", "count": 20, "includePromotedContent": false, "withClientEventToken": false, "withBirdwatchNotes": false, "withVoice": true}' # str |  (default to '{"userId": "44196397", "count": 20, "includePromotedContent": false, "withClientEventToken": false, "withBirdwatchNotes": false, "withVoice": true}')
    features = '{"rweb_video_screen_enabled": false, "payments_enabled": false, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": true, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "tweet_awards_web_tipping_enabled": false, "responsive_web_grok_show_grok_translated_post": false, "responsive_web_grok_analysis_button_from_backend": true, "creator_subscriptions_quote_tweet_preview_enabled": false, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": true, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": false, "responsive_web_enhance_cards_enabled": false}' # str |  (default to '{"rweb_video_screen_enabled": false, "payments_enabled": false, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": true, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "tweet_awards_web_tipping_enabled": false, "responsive_web_grok_show_grok_translated_post": false, "responsive_web_grok_analysis_button_from_backend": true, "creator_subscriptions_quote_tweet_preview_enabled": false, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": true, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": false, "responsive_web_enhance_cards_enabled": false}')
    field_toggles = '{"withArticlePlainText": false}' # str |  (default to '{"withArticlePlainText": false}')

    try:
        api_response = api_instance.get_likes(path_query_id, variables, features, field_toggles)
        print("The response of TweetApi->get_likes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TweetApi->get_likes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;rk2aeVVvKsyUdG3jf5uiLw&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;userId&quot;: &quot;44196397&quot;, &quot;count&quot;: 20, &quot;includePromotedContent&quot;: false, &quot;withClientEventToken&quot;: false, &quot;withBirdwatchNotes&quot;: false, &quot;withVoice&quot;: true}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;rweb_video_screen_enabled&quot;: false, &quot;payments_enabled&quot;: false, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;responsive_web_profile_redirect_enabled&quot;: false, &quot;rweb_tipjar_consumption_enabled&quot;: true, &quot;verified_phone_label_enabled&quot;: false, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;tweet_awards_web_tipping_enabled&quot;: false, &quot;responsive_web_grok_show_grok_translated_post&quot;: false, &quot;responsive_web_grok_analysis_button_from_backend&quot;: true, &quot;creator_subscriptions_quote_tweet_preview_enabled&quot;: false, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: true, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: false, &quot;responsive_web_enhance_cards_enabled&quot;: false}&#39;]
 **field_toggles** | **str**|  | [default to &#39;{&quot;withArticlePlainText&quot;: false}&#39;]

### Return type

[**UserTweetsResponse**](UserTweetsResponse.md)

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

# **get_list_latest_tweets_timeline**
> ListLatestTweetsTimelineResponse get_list_latest_tweets_timeline(path_query_id, variables, features)

get tweet list of timeline

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
from twitter_openapi_python_generated.models.list_latest_tweets_timeline_response import ListLatestTweetsTimelineResponse
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
    api_instance = twitter_openapi_python_generated.TweetApi(api_client)
    path_query_id = 'FVWmROVvhgjRPC-4jAUh8A' # str |  (default to 'FVWmROVvhgjRPC-4jAUh8A')
    variables = '{"listId": "1539453138322673664", "count": 20}' # str |  (default to '{"listId": "1539453138322673664", "count": 20}')
    features = '{"rweb_video_screen_enabled": false, "payments_enabled": false, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": true, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "tweet_awards_web_tipping_enabled": false, "responsive_web_grok_show_grok_translated_post": false, "responsive_web_grok_analysis_button_from_backend": true, "creator_subscriptions_quote_tweet_preview_enabled": false, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": true, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": false, "responsive_web_enhance_cards_enabled": false}' # str |  (default to '{"rweb_video_screen_enabled": false, "payments_enabled": false, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": true, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "tweet_awards_web_tipping_enabled": false, "responsive_web_grok_show_grok_translated_post": false, "responsive_web_grok_analysis_button_from_backend": true, "creator_subscriptions_quote_tweet_preview_enabled": false, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": true, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": false, "responsive_web_enhance_cards_enabled": false}')

    try:
        api_response = api_instance.get_list_latest_tweets_timeline(path_query_id, variables, features)
        print("The response of TweetApi->get_list_latest_tweets_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TweetApi->get_list_latest_tweets_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;FVWmROVvhgjRPC-4jAUh8A&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;listId&quot;: &quot;1539453138322673664&quot;, &quot;count&quot;: 20}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;rweb_video_screen_enabled&quot;: false, &quot;payments_enabled&quot;: false, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;responsive_web_profile_redirect_enabled&quot;: false, &quot;rweb_tipjar_consumption_enabled&quot;: true, &quot;verified_phone_label_enabled&quot;: false, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;tweet_awards_web_tipping_enabled&quot;: false, &quot;responsive_web_grok_show_grok_translated_post&quot;: false, &quot;responsive_web_grok_analysis_button_from_backend&quot;: true, &quot;creator_subscriptions_quote_tweet_preview_enabled&quot;: false, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: true, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: false, &quot;responsive_web_enhance_cards_enabled&quot;: false}&#39;]

### Return type

[**ListLatestTweetsTimelineResponse**](ListLatestTweetsTimelineResponse.md)

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

# **get_notifications_timeline**
> NotificationsTimelineResponse get_notifications_timeline(path_query_id, variables, features)

get notification list. timeline_type:[All, Verified, Mentions]

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
from twitter_openapi_python_generated.models.notifications_timeline_response import NotificationsTimelineResponse
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
    api_instance = twitter_openapi_python_generated.TweetApi(api_client)
    path_query_id = 'gzC0OYBCnfdYS4M4Gue7BA' # str |  (default to 'gzC0OYBCnfdYS4M4Gue7BA')
    variables = '{"timeline_type": "All", "count": 20}' # str |  (default to '{"timeline_type": "All", "count": 20}')
    features = '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}' # str |  (default to '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}')

    try:
        api_response = api_instance.get_notifications_timeline(path_query_id, variables, features)
        print("The response of TweetApi->get_notifications_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TweetApi->get_notifications_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;gzC0OYBCnfdYS4M4Gue7BA&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;timeline_type&quot;: &quot;All&quot;, &quot;count&quot;: 20}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;rweb_video_screen_enabled&quot;: false, &quot;rweb_cashtags_enabled&quot;: true, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;responsive_web_profile_redirect_enabled&quot;: false, &quot;rweb_tipjar_consumption_enabled&quot;: false, &quot;verified_phone_label_enabled&quot;: false, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;rweb_cashtags_composer_attachment_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;responsive_web_grok_annotations_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;rweb_conversational_replies_downvote_enabled&quot;: false, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;content_disclosure_indicator_enabled&quot;: true, &quot;content_disclosure_ai_generated_indicator_enabled&quot;: true, &quot;responsive_web_grok_show_grok_translated_post&quot;: true, &quot;responsive_web_grok_analysis_button_from_backend&quot;: true, &quot;post_ctas_fetch_enabled&quot;: true, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: false, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: true, &quot;responsive_web_enhance_cards_enabled&quot;: false}&#39;]

### Return type

[**NotificationsTimelineResponse**](NotificationsTimelineResponse.md)

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

# **get_search_timeline**
> SearchTimelineResponse get_search_timeline(path_query_id, variables, features)

search tweet list. product:[Top, Latest, People, Photos, Videos]

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
from twitter_openapi_python_generated.models.search_timeline_response import SearchTimelineResponse
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
    api_instance = twitter_openapi_python_generated.TweetApi(api_client)
    path_query_id = 'Yw6L66Pw54NHKuq4Dp7b4Q' # str |  (default to 'Yw6L66Pw54NHKuq4Dp7b4Q')
    variables = '{"rawQuery": "elonmusk", "count": 20, "querySource": "typed_query", "product": "Top"}' # str |  (default to '{"rawQuery": "elonmusk", "count": 20, "querySource": "typed_query", "product": "Top"}')
    features = '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}' # str |  (default to '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}')

    try:
        api_response = api_instance.get_search_timeline(path_query_id, variables, features)
        print("The response of TweetApi->get_search_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TweetApi->get_search_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;Yw6L66Pw54NHKuq4Dp7b4Q&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;rawQuery&quot;: &quot;elonmusk&quot;, &quot;count&quot;: 20, &quot;querySource&quot;: &quot;typed_query&quot;, &quot;product&quot;: &quot;Top&quot;}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;rweb_video_screen_enabled&quot;: false, &quot;rweb_cashtags_enabled&quot;: true, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;responsive_web_profile_redirect_enabled&quot;: false, &quot;rweb_tipjar_consumption_enabled&quot;: false, &quot;verified_phone_label_enabled&quot;: false, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;rweb_cashtags_composer_attachment_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;responsive_web_grok_annotations_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;rweb_conversational_replies_downvote_enabled&quot;: false, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;content_disclosure_indicator_enabled&quot;: true, &quot;content_disclosure_ai_generated_indicator_enabled&quot;: true, &quot;responsive_web_grok_show_grok_translated_post&quot;: true, &quot;responsive_web_grok_analysis_button_from_backend&quot;: true, &quot;post_ctas_fetch_enabled&quot;: true, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: false, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: true, &quot;responsive_web_enhance_cards_enabled&quot;: false}&#39;]

### Return type

[**SearchTimelineResponse**](SearchTimelineResponse.md)

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

# **get_tweet_detail**
> TweetDetailResponse get_tweet_detail(path_query_id, variables, features, field_toggles)

get TweetDetail

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
from twitter_openapi_python_generated.models.tweet_detail_response import TweetDetailResponse
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
    api_instance = twitter_openapi_python_generated.TweetApi(api_client)
    path_query_id = 'oCon7R-cgWRFy6EfZjaKfg' # str |  (default to 'oCon7R-cgWRFy6EfZjaKfg')
    variables = '{"focalTweetId": "1349129669258448897", "referrer": "home", "with_rux_injections": false, "rankingMode": "Relevance", "includePromotedContent": true, "withCommunity": true, "withQuickPromoteEligibilityTweetFields": true, "withBirdwatchNotes": true, "withVoice": true}' # str |  (default to '{"focalTweetId": "1349129669258448897", "referrer": "home", "with_rux_injections": false, "rankingMode": "Relevance", "includePromotedContent": true, "withCommunity": true, "withQuickPromoteEligibilityTweetFields": true, "withBirdwatchNotes": true, "withVoice": true}')
    features = '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}' # str |  (default to '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}')
    field_toggles = '{"withArticleRichContentState": true, "withArticlePlainText": false, "withArticleSummaryText": true, "withArticleVoiceOver": true, "withGrokAnalyze": false, "withDisallowedReplyControls": false}' # str |  (default to '{"withArticleRichContentState": true, "withArticlePlainText": false, "withArticleSummaryText": true, "withArticleVoiceOver": true, "withGrokAnalyze": false, "withDisallowedReplyControls": false}')

    try:
        api_response = api_instance.get_tweet_detail(path_query_id, variables, features, field_toggles)
        print("The response of TweetApi->get_tweet_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TweetApi->get_tweet_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;oCon7R-cgWRFy6EfZjaKfg&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;focalTweetId&quot;: &quot;1349129669258448897&quot;, &quot;referrer&quot;: &quot;home&quot;, &quot;with_rux_injections&quot;: false, &quot;rankingMode&quot;: &quot;Relevance&quot;, &quot;includePromotedContent&quot;: true, &quot;withCommunity&quot;: true, &quot;withQuickPromoteEligibilityTweetFields&quot;: true, &quot;withBirdwatchNotes&quot;: true, &quot;withVoice&quot;: true}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;rweb_video_screen_enabled&quot;: false, &quot;rweb_cashtags_enabled&quot;: true, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;responsive_web_profile_redirect_enabled&quot;: false, &quot;rweb_tipjar_consumption_enabled&quot;: false, &quot;verified_phone_label_enabled&quot;: false, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;rweb_cashtags_composer_attachment_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;responsive_web_grok_annotations_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;rweb_conversational_replies_downvote_enabled&quot;: false, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;content_disclosure_indicator_enabled&quot;: true, &quot;content_disclosure_ai_generated_indicator_enabled&quot;: true, &quot;responsive_web_grok_show_grok_translated_post&quot;: true, &quot;responsive_web_grok_analysis_button_from_backend&quot;: true, &quot;post_ctas_fetch_enabled&quot;: true, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: false, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: true, &quot;responsive_web_enhance_cards_enabled&quot;: false}&#39;]
 **field_toggles** | **str**|  | [default to &#39;{&quot;withArticleRichContentState&quot;: true, &quot;withArticlePlainText&quot;: false, &quot;withArticleSummaryText&quot;: true, &quot;withArticleVoiceOver&quot;: true, &quot;withGrokAnalyze&quot;: false, &quot;withDisallowedReplyControls&quot;: false}&#39;]

### Return type

[**TweetDetailResponse**](TweetDetailResponse.md)

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

# **get_user_highlights_tweets**
> UserHighlightsTweetsResponse get_user_highlights_tweets(path_query_id, variables, features, field_toggles)

get user highlights tweets

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
from twitter_openapi_python_generated.models.user_highlights_tweets_response import UserHighlightsTweetsResponse
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
    api_instance = twitter_openapi_python_generated.TweetApi(api_client)
    path_query_id = 'acwIZetKoEZPfIAhjXYpuA' # str |  (default to 'acwIZetKoEZPfIAhjXYpuA')
    variables = '{"userId": "44196397", "count": 40, "includePromotedContent": true, "withVoice": true}' # str |  (default to '{"userId": "44196397", "count": 40, "includePromotedContent": true, "withVoice": true}')
    features = '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}' # str |  (default to '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}')
    field_toggles = '{"withArticlePlainText": false}' # str |  (default to '{"withArticlePlainText": false}')

    try:
        api_response = api_instance.get_user_highlights_tweets(path_query_id, variables, features, field_toggles)
        print("The response of TweetApi->get_user_highlights_tweets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TweetApi->get_user_highlights_tweets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;acwIZetKoEZPfIAhjXYpuA&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;userId&quot;: &quot;44196397&quot;, &quot;count&quot;: 40, &quot;includePromotedContent&quot;: true, &quot;withVoice&quot;: true}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;rweb_video_screen_enabled&quot;: false, &quot;rweb_cashtags_enabled&quot;: true, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;responsive_web_profile_redirect_enabled&quot;: false, &quot;rweb_tipjar_consumption_enabled&quot;: false, &quot;verified_phone_label_enabled&quot;: false, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;rweb_cashtags_composer_attachment_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;responsive_web_grok_annotations_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;rweb_conversational_replies_downvote_enabled&quot;: false, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;content_disclosure_indicator_enabled&quot;: true, &quot;content_disclosure_ai_generated_indicator_enabled&quot;: true, &quot;responsive_web_grok_show_grok_translated_post&quot;: true, &quot;responsive_web_grok_analysis_button_from_backend&quot;: true, &quot;post_ctas_fetch_enabled&quot;: true, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: false, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: true, &quot;responsive_web_enhance_cards_enabled&quot;: false}&#39;]
 **field_toggles** | **str**|  | [default to &#39;{&quot;withArticlePlainText&quot;: false}&#39;]

### Return type

[**UserHighlightsTweetsResponse**](UserHighlightsTweetsResponse.md)

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

# **get_user_media**
> UserTweetsResponse get_user_media(path_query_id, variables, features, field_toggles)

get user media tweets

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
from twitter_openapi_python_generated.models.user_tweets_response import UserTweetsResponse
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
    api_instance = twitter_openapi_python_generated.TweetApi(api_client)
    path_query_id = '9EovraBTXJYGSEQXZqlLmQ' # str |  (default to '9EovraBTXJYGSEQXZqlLmQ')
    variables = '{"userId": "44196397", "count": 40, "includePromotedContent": false, "withClientEventToken": false, "withBirdwatchNotes": false, "withVoice": true}' # str |  (default to '{"userId": "44196397", "count": 40, "includePromotedContent": false, "withClientEventToken": false, "withBirdwatchNotes": false, "withVoice": true}')
    features = '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}' # str |  (default to '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}')
    field_toggles = '{"withArticlePlainText": false}' # str |  (default to '{"withArticlePlainText": false}')

    try:
        api_response = api_instance.get_user_media(path_query_id, variables, features, field_toggles)
        print("The response of TweetApi->get_user_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TweetApi->get_user_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;9EovraBTXJYGSEQXZqlLmQ&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;userId&quot;: &quot;44196397&quot;, &quot;count&quot;: 40, &quot;includePromotedContent&quot;: false, &quot;withClientEventToken&quot;: false, &quot;withBirdwatchNotes&quot;: false, &quot;withVoice&quot;: true}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;rweb_video_screen_enabled&quot;: false, &quot;rweb_cashtags_enabled&quot;: true, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;responsive_web_profile_redirect_enabled&quot;: false, &quot;rweb_tipjar_consumption_enabled&quot;: false, &quot;verified_phone_label_enabled&quot;: false, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;rweb_cashtags_composer_attachment_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;responsive_web_grok_annotations_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;rweb_conversational_replies_downvote_enabled&quot;: false, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;content_disclosure_indicator_enabled&quot;: true, &quot;content_disclosure_ai_generated_indicator_enabled&quot;: true, &quot;responsive_web_grok_show_grok_translated_post&quot;: true, &quot;responsive_web_grok_analysis_button_from_backend&quot;: true, &quot;post_ctas_fetch_enabled&quot;: true, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: false, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: true, &quot;responsive_web_enhance_cards_enabled&quot;: false}&#39;]
 **field_toggles** | **str**|  | [default to &#39;{&quot;withArticlePlainText&quot;: false}&#39;]

### Return type

[**UserTweetsResponse**](UserTweetsResponse.md)

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

# **get_user_tweets**
> UserTweetsResponse get_user_tweets(path_query_id, variables, features, field_toggles)

get user tweets

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
from twitter_openapi_python_generated.models.user_tweets_response import UserTweetsResponse
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
    api_instance = twitter_openapi_python_generated.TweetApi(api_client)
    path_query_id = '36rb3Xj3iJ64Q-9wKDjCcQ' # str |  (default to '36rb3Xj3iJ64Q-9wKDjCcQ')
    variables = '{"userId": "44196397", "count": 40, "includePromotedContent": true, "withQuickPromoteEligibilityTweetFields": true, "withVoice": true}' # str |  (default to '{"userId": "44196397", "count": 40, "includePromotedContent": true, "withQuickPromoteEligibilityTweetFields": true, "withVoice": true}')
    features = '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}' # str |  (default to '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}')
    field_toggles = '{"withArticlePlainText": false}' # str |  (default to '{"withArticlePlainText": false}')

    try:
        api_response = api_instance.get_user_tweets(path_query_id, variables, features, field_toggles)
        print("The response of TweetApi->get_user_tweets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TweetApi->get_user_tweets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;36rb3Xj3iJ64Q-9wKDjCcQ&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;userId&quot;: &quot;44196397&quot;, &quot;count&quot;: 40, &quot;includePromotedContent&quot;: true, &quot;withQuickPromoteEligibilityTweetFields&quot;: true, &quot;withVoice&quot;: true}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;rweb_video_screen_enabled&quot;: false, &quot;rweb_cashtags_enabled&quot;: true, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;responsive_web_profile_redirect_enabled&quot;: false, &quot;rweb_tipjar_consumption_enabled&quot;: false, &quot;verified_phone_label_enabled&quot;: false, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;rweb_cashtags_composer_attachment_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;responsive_web_grok_annotations_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;rweb_conversational_replies_downvote_enabled&quot;: false, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;content_disclosure_indicator_enabled&quot;: true, &quot;content_disclosure_ai_generated_indicator_enabled&quot;: true, &quot;responsive_web_grok_show_grok_translated_post&quot;: true, &quot;responsive_web_grok_analysis_button_from_backend&quot;: true, &quot;post_ctas_fetch_enabled&quot;: true, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: false, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: true, &quot;responsive_web_enhance_cards_enabled&quot;: false}&#39;]
 **field_toggles** | **str**|  | [default to &#39;{&quot;withArticlePlainText&quot;: false}&#39;]

### Return type

[**UserTweetsResponse**](UserTweetsResponse.md)

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

# **get_user_tweets_and_replies**
> UserTweetsResponse get_user_tweets_and_replies(path_query_id, variables, features, field_toggles)

get user replies tweets

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
from twitter_openapi_python_generated.models.user_tweets_response import UserTweetsResponse
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
    api_instance = twitter_openapi_python_generated.TweetApi(api_client)
    path_query_id = 'D5eKzDa5ZoJuC1TCeAXbWA' # str |  (default to 'D5eKzDa5ZoJuC1TCeAXbWA')
    variables = '{"userId": "44196397", "count": 40, "includePromotedContent": true, "withCommunity": true, "withVoice": true}' # str |  (default to '{"userId": "44196397", "count": 40, "includePromotedContent": true, "withCommunity": true, "withVoice": true}')
    features = '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}' # str |  (default to '{"rweb_video_screen_enabled": false, "rweb_cashtags_enabled": true, "profile_label_improvements_pcf_label_in_post_enabled": true, "responsive_web_profile_redirect_enabled": false, "rweb_tipjar_consumption_enabled": false, "verified_phone_label_enabled": false, "creator_subscriptions_tweet_preview_api_enabled": true, "responsive_web_graphql_timeline_navigation_enabled": true, "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false, "premium_content_api_read_enabled": false, "communities_web_enable_tweet_community_results_fetch": true, "c9s_tweet_anatomy_moderator_badge_enabled": true, "responsive_web_grok_analyze_button_fetch_trends_enabled": false, "responsive_web_grok_analyze_post_followups_enabled": true, "rweb_cashtags_composer_attachment_enabled": true, "responsive_web_jetfuel_frame": true, "responsive_web_grok_share_attachment_enabled": true, "responsive_web_grok_annotations_enabled": true, "articles_preview_enabled": true, "responsive_web_edit_tweet_api_enabled": true, "rweb_conversational_replies_downvote_enabled": false, "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true, "view_counts_everywhere_api_enabled": true, "longform_notetweets_consumption_enabled": true, "responsive_web_twitter_article_tweet_consumption_enabled": true, "content_disclosure_indicator_enabled": true, "content_disclosure_ai_generated_indicator_enabled": true, "responsive_web_grok_show_grok_translated_post": true, "responsive_web_grok_analysis_button_from_backend": true, "post_ctas_fetch_enabled": true, "freedom_of_speech_not_reach_fetch_enabled": true, "standardized_nudges_misinfo": true, "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true, "longform_notetweets_rich_text_read_enabled": true, "longform_notetweets_inline_media_enabled": false, "responsive_web_grok_image_annotation_enabled": true, "responsive_web_grok_imagine_annotation_enabled": true, "responsive_web_grok_community_note_auto_translation_is_enabled": true, "responsive_web_enhance_cards_enabled": false}')
    field_toggles = '{"withArticlePlainText": false}' # str |  (default to '{"withArticlePlainText": false}')

    try:
        api_response = api_instance.get_user_tweets_and_replies(path_query_id, variables, features, field_toggles)
        print("The response of TweetApi->get_user_tweets_and_replies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TweetApi->get_user_tweets_and_replies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_query_id** | **str**|  | [default to &#39;D5eKzDa5ZoJuC1TCeAXbWA&#39;]
 **variables** | **str**|  | [default to &#39;{&quot;userId&quot;: &quot;44196397&quot;, &quot;count&quot;: 40, &quot;includePromotedContent&quot;: true, &quot;withCommunity&quot;: true, &quot;withVoice&quot;: true}&#39;]
 **features** | **str**|  | [default to &#39;{&quot;rweb_video_screen_enabled&quot;: false, &quot;rweb_cashtags_enabled&quot;: true, &quot;profile_label_improvements_pcf_label_in_post_enabled&quot;: true, &quot;responsive_web_profile_redirect_enabled&quot;: false, &quot;rweb_tipjar_consumption_enabled&quot;: false, &quot;verified_phone_label_enabled&quot;: false, &quot;creator_subscriptions_tweet_preview_api_enabled&quot;: true, &quot;responsive_web_graphql_timeline_navigation_enabled&quot;: true, &quot;responsive_web_graphql_skip_user_profile_image_extensions_enabled&quot;: false, &quot;premium_content_api_read_enabled&quot;: false, &quot;communities_web_enable_tweet_community_results_fetch&quot;: true, &quot;c9s_tweet_anatomy_moderator_badge_enabled&quot;: true, &quot;responsive_web_grok_analyze_button_fetch_trends_enabled&quot;: false, &quot;responsive_web_grok_analyze_post_followups_enabled&quot;: true, &quot;rweb_cashtags_composer_attachment_enabled&quot;: true, &quot;responsive_web_jetfuel_frame&quot;: true, &quot;responsive_web_grok_share_attachment_enabled&quot;: true, &quot;responsive_web_grok_annotations_enabled&quot;: true, &quot;articles_preview_enabled&quot;: true, &quot;responsive_web_edit_tweet_api_enabled&quot;: true, &quot;rweb_conversational_replies_downvote_enabled&quot;: false, &quot;graphql_is_translatable_rweb_tweet_is_translatable_enabled&quot;: true, &quot;view_counts_everywhere_api_enabled&quot;: true, &quot;longform_notetweets_consumption_enabled&quot;: true, &quot;responsive_web_twitter_article_tweet_consumption_enabled&quot;: true, &quot;content_disclosure_indicator_enabled&quot;: true, &quot;content_disclosure_ai_generated_indicator_enabled&quot;: true, &quot;responsive_web_grok_show_grok_translated_post&quot;: true, &quot;responsive_web_grok_analysis_button_from_backend&quot;: true, &quot;post_ctas_fetch_enabled&quot;: true, &quot;freedom_of_speech_not_reach_fetch_enabled&quot;: true, &quot;standardized_nudges_misinfo&quot;: true, &quot;tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled&quot;: true, &quot;longform_notetweets_rich_text_read_enabled&quot;: true, &quot;longform_notetweets_inline_media_enabled&quot;: false, &quot;responsive_web_grok_image_annotation_enabled&quot;: true, &quot;responsive_web_grok_imagine_annotation_enabled&quot;: true, &quot;responsive_web_grok_community_note_auto_translation_is_enabled&quot;: true, &quot;responsive_web_enhance_cards_enabled&quot;: false}&#39;]
 **field_toggles** | **str**|  | [default to &#39;{&quot;withArticlePlainText&quot;: false}&#39;]

### Return type

[**UserTweetsResponse**](UserTweetsResponse.md)

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

