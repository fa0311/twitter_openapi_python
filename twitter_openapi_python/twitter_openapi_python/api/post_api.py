from typing import Any, Optional, TypeVar

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models

from twitter_openapi_python.models import TwitterApiUtilsResponse
from twitter_openapi_python.utils import build_response, non_nullable

T = TypeVar("T")
ResponseType = TwitterApiUtilsResponse[T]
ParamType = dict[str, Any]


class PostApiUtils:
    api: twitter.PostApi
    flag: ParamType

    def __init__(self, api: twitter.PostApi, flag: ParamType):
        self.api = api
        self.flag = flag

    def post_create_tweet(
        self,
        tweet_text: str,
        media_ids: Optional[list[str]] = None,
        tagged_users: Optional[list[list[str]]] = None,
        in_reply_to_tweet_id: Optional[str] = None,
        attachment_url: Optional[str] = None,
        conversation_control: Optional[str] = None,
    ) -> ResponseType[models.CreateTweetResponse]:
        variables = non_nullable(
            twitter.PostCreateTweetRequestVariables.from_dict(self.flag["CreateTweet"]["variables"])
        )
        features = non_nullable(twitter.PostCreateTweetRequestFeatures.from_dict(self.flag["CreateTweet"]["features"]))
        variables.tweet_text = tweet_text
        if media_ids:
            tagged_or = tagged_users or []
            variables.media.media_entities = [
                twitter.PostCreateTweetRequestVariablesMediaMediaEntitiesInner(
                    media_id=media_id,
                    tagged_users=tagged_or[idx] if len(tagged_or) > idx else [],
                )
                for idx, media_id in enumerate(media_ids)
            ]
        variables.attachment_url = attachment_url
        if conversation_control:
            variables.conversation_control = twitter.PostCreateTweetRequestVariablesConversationControl(
                mode=conversation_control
            )

        if in_reply_to_tweet_id:
            variables.reply = twitter.PostCreateTweetRequestVariablesReply(
                exclude_reply_user_ids=[],
                in_reply_to_tweet_id=in_reply_to_tweet_id,
            )

        res = self.api.post_create_tweet_with_http_info(
            path_query_id=self.flag["CreateTweet"]["queryId"],
            post_create_tweet_request=twitter.PostCreateTweetRequest(
                queryId=self.flag["CreateTweet"]["queryId"],
                variables=variables,
                features=features,
            ),
        )
        return build_response(res, res.data)

    def post_delete_tweet(
        self,
        tweet_id: str,
    ) -> ResponseType[models.DeleteTweetResponse]:
        variables = non_nullable(
            twitter.PostCreateRetweetRequestVariables.from_dict(self.flag["DeleteTweet"]["variables"])
        )
        variables.tweet_id = tweet_id

        res = self.api.post_delete_tweet_with_http_info(
            path_query_id=self.flag["DeleteTweet"]["queryId"],
            post_delete_tweet_request=twitter.PostDeleteTweetRequest(
                queryId=self.flag["DeleteTweet"]["queryId"],
                variables=variables,
            ),
        )
        return build_response(res, res.data)

    def post_create_retweet(
        self,
        tweet_id: str,
    ) -> ResponseType[models.CreateRetweetResponse]:
        variables = non_nullable(
            twitter.PostCreateRetweetRequestVariables.from_dict(self.flag["CreateRetweet"]["variables"])
        )
        variables.tweet_id = tweet_id

        res = self.api.post_create_retweet_with_http_info(
            path_query_id=self.flag["CreateRetweet"]["queryId"],
            post_create_retweet_request=twitter.PostCreateRetweetRequest(
                queryId=self.flag["CreateRetweet"]["queryId"],
                variables=variables,
            ),
        )
        return build_response(res, res.data)

    def post_delete_retweet(
        self,
        source_tweet_id: str,
    ) -> ResponseType[models.DeleteRetweetResponse]:
        variables = non_nullable(
            twitter.PostDeleteRetweetRequestVariables.from_dict(self.flag["DeleteRetweet"]["variables"])
        )
        variables.source_tweet_id = source_tweet_id

        res = self.api.post_delete_retweet_with_http_info(
            path_query_id=self.flag["DeleteRetweet"]["queryId"],
            post_delete_retweet_request=twitter.PostDeleteRetweetRequest(
                queryId=self.flag["DeleteRetweet"]["queryId"],
                variables=variables,
            ),
        )
        return build_response(res, res.data)

    # postFavoriteTweet
    def post_favorite_tweet(
        self,
        tweet_id: str,
    ) -> ResponseType[models.FavoriteTweetResponse]:
        variables = non_nullable(
            twitter.PostCreateBookmarkRequestVariables.from_dict(self.flag["FavoriteTweet"]["variables"])
        )
        variables.tweet_id = tweet_id

        res = self.api.post_favorite_tweet_with_http_info(
            path_query_id=self.flag["FavoriteTweet"]["queryId"],
            post_favorite_tweet_request=twitter.PostFavoriteTweetRequest(
                queryId=self.flag["FavoriteTweet"]["queryId"],
                variables=variables,
            ),
        )
        return build_response(res, res.data)

    # postUnfavoriteTweet
    def post_unfavorite_tweet(
        self,
        tweet_id: str,
    ) -> ResponseType[models.UnfavoriteTweetResponse]:
        variables = non_nullable(
            twitter.PostCreateRetweetRequestVariables.from_dict(self.flag["UnfavoriteTweet"]["variables"])
        )
        variables.tweet_id = tweet_id

        res = self.api.post_unfavorite_tweet_with_http_info(
            path_query_id=self.flag["UnfavoriteTweet"]["queryId"],
            post_unfavorite_tweet_request=twitter.PostUnfavoriteTweetRequest(
                queryId=self.flag["UnfavoriteTweet"]["queryId"],
                variables=variables,
            ),
        )
        return build_response(res, res.data)
