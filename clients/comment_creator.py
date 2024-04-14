import asyncio
import aiohttp
import random
import datetime

from utils.constants import COMMENT_CREATE_TARGET_URL, COMMENT_CREATE_HEADERS, CREATE_COMMENT_POST_NO
from utils.helper import generate_random_content


class CommentCreator:
    def __init__(self):
        self.auth_codes = ["3289SIZI"]

    @staticmethod
    async def comment_create_body(auth_code):
        return {
            "auth_code": auth_code,
            "content": generate_random_content(),
            "post_no": CREATE_COMMENT_POST_NO,
            "season_level_join_flag": "Y",
            "season_level_no": "28",
            "sns_user_sn": "232469",
            "user_level": "47",
        }

    async def send_request(self, auth_code):
        try:
            await self.request_to_comment_create_server(auth_code)

        except aiohttp.ClientError as e:
            print(f"An error occurred while sending request: {e}")

    async def request_to_comment_create_server(self, auth_code):
        async with aiohttp.ClientSession() as session:
            print(f"Sending request with auth_code: {auth_code} and post_no: {CREATE_COMMENT_POST_NO}")
            async with session.post(
                    url=COMMENT_CREATE_TARGET_URL,
                    headers=COMMENT_CREATE_HEADERS,
                    data=await self.comment_create_body(auth_code),
            ) as response:
                print(await response.text())

    async def send_request_to_all_auth_code(self):
        for auth_code in self.auth_codes:
            await self.send_request(auth_code)
            # 0.1초 대기합니다.
            await asyncio.sleep(0.1)

    async def execute_until(self, end_time):
        while datetime.datetime.now() < end_time:
            await self.send_request_to_all_auth_code()
            random_delay = random.randint(10, 13)
            await asyncio.sleep(random_delay)

    async def main(self):
        while True:
            end_time = datetime.datetime.now() + datetime.timedelta(minutes=5)  # executes for 5 minutes
            await self.execute_until(end_time)


asyncio.run(CommentCreator().main())
