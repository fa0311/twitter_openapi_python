import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from typing import Any

from twitter_openapi_python.models import PostApiUtilsHeader, TwitterApiUtilsResponse
from twitter_openapi_python.utils import build_response


class PostApiUtils:
    api: twitter.PostApi
    flag: dict[str, Any]

    def __init__(self, api: twitter.PostApi, flag: dict[str, Any]):
        self.api = api
        self.flag = flag

    def builder(
        self,
        response: twitter.ApiResponse,
    ) -> TwitterApiUtilsResponse[models.CreateTweetResponse, PostApiUtilsHeader]:
        if isinstance(response.data.actual_instance, twitter.Error):
            error: twitter.Error = response.data.actual_instance
            raise Exception(error)

        return build_response(
            response=response,
            data=response.data.actual_instance,
            type=PostApiUtilsHeader,
        )

    def post_create_tweet(
        self,
        tweet_text: str,
    ) -> TwitterApiUtilsResponse[models.CreateTweetResponse, PostApiUtilsHeader]:
        variables = twitter.PostCreateTweetRequestVariables.from_dict(
            self.flag["CreateTweet"]["variables"]
        )
        features = twitter.PostCreateTweetRequestFeatures.from_dict(
            self.flag["CreateTweet"]["features"]
        )
        variables.tweet_text = tweet_text

        response = self.api.post_create_tweet_with_http_info(
            path_query_id=self.flag["CreateTweet"]["queryId"],
            post_create_tweet_request=twitter.PostCreateTweetRequest(
                queryId=self.flag["CreateTweet"]["queryId"],
                variables=variables,
                features=features,
            ),
        )

        return self.builder(response)

    def post_delete_tweet(
        self,
        tweet_id: str,
    ) -> TwitterApiUtilsResponse[models.DeleteTweetResponse, PostApiUtilsHeader]:
        variables = twitter.PostCreateRetweetRequestVariables.from_dict(
            self.flag["DeleteTweet"]["variables"]
        )
        variables.tweet_id = tweet_id

        response = self.api.post_delete_tweet_with_http_info(
            path_query_id=self.flag["DeleteTweet"]["queryId"],
            post_delete_tweet_request=twitter.PostDeleteTweetRequest(
                queryId=self.flag["DeleteTweet"]["queryId"],
                variables=variables,
            ),
        )

        return self.builder(response)

    def post_create_retweet(
        self,
        tweet_id: str,
    ) -> TwitterApiUtilsResponse[models.CreateRetweetResponse, PostApiUtilsHeader]:
        variables = twitter.PostCreateRetweetRequestVariables.from_dict(
            self.flag["CreateRetweet"]["variables"]
        )
        variables.tweet_id = tweet_id

        response = self.api.post_create_retweet_with_http_info(
            path_query_id=self.flag["CreateRetweet"]["queryId"],
            post_create_retweet_request=twitter.PostCreateRetweetRequest(
                queryId=self.flag["CreateRetweet"]["queryId"],
                variables=variables,
            ),
        )

        return self.builder(response)

    def post_delete_retweet(
        self,
        source_tweet_id: str,
    ) -> TwitterApiUtilsResponse[models.DeleteRetweetResponse, PostApiUtilsHeader]:
        variables = twitter.PostDeleteRetweetRequestVariables.from_dict(
            self.flag["DeleteRetweet"]["variables"]
        )
        variables.source_tweet_id = source_tweet_id

        response = self.api.post_delete_retweet_with_http_info(
            path_query_id=self.flag["DeleteRetweet"]["queryId"],
            post_delete_retweet_request=twitter.PostDeleteRetweetRequest(
                queryId=self.flag["DeleteRetweet"]["queryId"],
                variables=variables,
            ),
        )

        return self.builder(response)

    # postFavoriteTweet
    def post_favorite_tweet(
        self,
        tweet_id: str,
    ) -> TwitterApiUtilsResponse[models.FavoriteTweetResponseData, PostApiUtilsHeader]:
        variables = twitter.PostCreateRetweetRequestVariables.from_dict(
            self.flag["FavoriteTweet"]["variables"]
        )
        variables.tweet_id = tweet_id

        response = self.api.post_favorite_tweet_with_http_info(
            path_query_id=self.flag["FavoriteTweet"]["queryId"],
            post_favorite_tweet_request=twitter.PostFavoriteTweetRequest(
                queryId=self.flag["FavoriteTweet"]["queryId"],
                variables=variables,
            ),
        )
        return self.builder(response)

    # postUnfavoriteTweet
    def post_unfavorite_tweet(
        self,
        tweet_id: str,
    ) -> TwitterApiUtilsResponse[
        models.UnfavoriteTweetResponseData,
        PostApiUtilsHeader,
    ]:
        variables = twitter.PostCreateRetweetRequestVariables.from_dict(
            self.flag["UnfavoriteTweet"]["variables"]
        )
        variables.tweet_id = tweet_id

        response = self.api.post_unfavorite_tweet_with_http_info(
            path_query_id=self.flag["UnfavoriteTweet"]["queryId"],
            post_unfavorite_tweet_request=twitter.PostUnfavoriteTweetRequest(
                queryId=self.flag["UnfavoriteTweet"]["queryId"],
                variables=variables,
            ),
        )
        return self.builder(response)
