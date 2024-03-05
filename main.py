from concurrent.futures import ThreadPoolExecutor

import vk_api
from dotenv import load_dotenv
import os

load_dotenv()


def vk_connect(token):
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    user = vk.account.getProfileInfo()
    group = vk.messages.joinChatByInviteLink(link=os.getenv("LINK_CHAT"))
    vk.messages.send(chat_id=group["chat_id"], message="Hi baby", random_id=0)
    vk.messages.removeChatUser(chat_id=group["chat_id"], user_id=user["id"])


def main():
    with open("tokens.txt") as file:
        with ThreadPoolExecutor() as executor:
            executor.map(vk_connect, map(str.strip, file))


if __name__ == "__main__":
    main()
