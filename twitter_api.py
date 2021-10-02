from requests_oauthlib import OAuth1Session
from io import BytesIO
import base64


def publish(image, tokens):
    auth = OAuth1Session(tokens["api_key"], tokens["api_key_secret"], tokens["access_token"],
                         tokens["access_token_secret"])

    # Image upload
    buff = BytesIO()
    image.save(buff, format="PNG")
    img_str = base64.b64encode(buff.getvalue())
    data = {
        "media_data": img_str,
    }
    url = "https://upload.twitter.com/1.1/media/upload.json"
    res = auth.post(url, data=data)
    media_id = res.json().get("media_id")

    # Tweet post
    data = {
        "status": "Good evening people!",
        "media_ids": media_id
    }
    url = "https://api.twitter.com/1.1/statuses/update.json"
    auth.post(url, data=data)
