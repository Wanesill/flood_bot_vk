from typing import Any

import vk_api
from vk_api.vk_api import VkApiMethod

from exceptions import ApiVkServiceError


def get_data_accounts_vk(filename: str) -> dict[VkApiMethod, dict[str, Any]]:
    """
    Считывание с файла токены и подлючение к Vk аккаунтам. Сбор данные аккаунтов в словарь.

    :param filename: Файл с токенами
    :return: dict
    """

    data_accounts = {}

    with open(filename) as file_tokens:
        for row in file_tokens:
            token = row.strip()
            account = __get_account_vk(token)

            try:
                data = account.account.getProfileInfo()
            except ApiVkServiceError as error:
                print("Ошибка получения данных аккаунта")
                raise error

            data_accounts[account] = data

    return data_accounts


def __get_account_vk(token: str) -> VkApiMethod:
    """
    Подключение и получение Vk аккаунта через токен.

    :param token: Получение токена из сайта: https://vkhost.github.io/
    :return: VkApiMethod
    """

    try:
        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()
    except ApiVkServiceError as error:
        print("Ошибка подключения к Vk аккаунту")
        raise error

    return vk
