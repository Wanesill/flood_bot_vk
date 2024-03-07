from concurrent.futures import ThreadPoolExecutor

from connect_vk import get_data_accounts_vk
from vk_group import process_vk_chat

from exceptions import ApiVkServiceError


def main() -> None:
    """
    Запуск основной логики программы.

    :return: None
    """

    try:
        data_accounts = list(get_data_accounts_vk("tokens.txt").items())

    except ApiVkServiceError:
        print("Ошибка получения данных Vk аккаунтов")

    len_data_account = len(data_accounts)

    try:
        executor = ThreadPoolExecutor()

        with open("text.txt", encoding="utf-8") as file_text:
            for index, row in enumerate(file_text):
                line = row.strip()
                account, user = data_accounts[index % len_data_account]
                executor.submit(process_vk_chat, account, user, line)

    except ApiVkServiceError:
        print("Ошибка при работе с Vk беседой")

    finally:
        executor.shutdown()


if __name__ == "__main__":
    main()
