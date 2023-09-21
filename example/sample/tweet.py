import datetime
from twitter_openapi_python import TwitterOpenapiPython
import login as login


cookies_dict = login.login().get_cookies().get_dict()
𝕏 = TwitterOpenapiPython().get_client_from_cookies(cookies=cookies_dict)

time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
𝕏.get_post_api().post_create_tweet(tweet_text=f"Hello World!!{time}")
