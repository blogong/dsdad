import time
import requests

from utils.constants import POST_CREATE_TARGET_URL, POST_CREATE_HEADERS, POST_CREATE_AUTH_CODE
from utils.helper import generate_random_content


# create posts macro responsibility for managing sudden attack radio application
class PostCreator:

    @staticmethod
    def create_post_body(auth_code):
        return {
            "auth_code": auth_code,
            "content": generate_random_content(),
            "hash_tag_1": "",
            "hash_tag_2": "",
            "hash_tag_3": "",
            "post_type": "0",
            "season_level_join_flag": "Y",
            "season_level_no": "28",
            "user_level": "47",
            "youtube_url": ""
        }

    @classmethod
    def send_request(cls, auth_code, content):
        data = cls.create_post_body(auth_code, content)
        response = requests.post(url=POST_CREATE_TARGET_URL, headers=POST_CREATE_HEADERS, data=data)
        print(response.text)

    @classmethod
    def main(cls):
        while True:
            cls.send_request(POST_CREATE_AUTH_CODE)
            time.sleep(60 * 3)  # 3 minutes delay


if __name__ == '__main__':
    PostCreator.main()
