import os
import dotenv

from typing import Any

from vk_api.vk_api import VkApiMethod

from exceptions import ApiVkServiceError


def process_vk_chat(account: VkApiMethod, user: dict[str, Any], message: str) -> None:
    """
    Запуск функций по работе с Vk беседой.

    :param account: Vk аккаунт
    :param user: Данные Vk аккаунта
    :param message: Строка из файла text.txt
    :return: None
    """

    chat = __join_vk_chat(account)
    __send_message_chat_vk_chat(account, chat, message)
    __leave_vk_chat(account, chat, user)


def __join_vk_chat(account: VkApiMethod) -> dict[str, int]:
    """
    Вступление в беседу по ссылке.

    :param account: Vk аккаунт
    :return: dict[str, int]
    """

    dotenv.load_dotenv()

    try:
        chat = account.messages.joinChatByInviteLink(link=os.getenv("LINK_CHAT"))
    except ApiVkServiceError as error:
        print("Ошибка вступления в Vk беседу по ссылке")
        raise error

    return chat


def __send_message_chat_vk_chat(
    account: VkApiMethod, chat: dict[str, int], message: str
) -> None:
    """
    Отправление сообщения в Vk беседу аккаунтом.

    :param account: Vk аккаунт
    :param chat: Vk беседа
    :param message: Текстовое сообщение
    :return: None
    """

    try:
        account.messages.send(chat_id=chat["chat_id"], message=message, random_id=0)
    except ApiVkServiceError as error:
        print("Ошибка отправления сообщения в Vk беседу")
        raise error


def __leave_vk_chat(
    account: VkApiMethod, chat: dict[str, int], user: dict[str, Any]
) -> None:
    """
    Покидание беседы Vk аккаунтом.

    :param account: Vk аккаунт
    :param chat: Vk беседа
    :param user: Данные Vk аккаунта
    :return: None
    """

    try:
        account.messages.removeChatUser(chat_id=chat["chat_id"], user_id=user["id"])
    except ApiVkServiceError as error:
        print("Ошибка покидания Vk беседы")
        raise error
