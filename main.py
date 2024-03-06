from threading import Lock
from concurrent.futures import ThreadPoolExecutor

from text_queue import get_text_queue
from connect_vk import get_data_accounts_vk
from vk_group import process_vk_chat

from exceptions import ApiVkServiceError


def main() -> None:
    """
    Запуск основной логики программы.

    :return: None
    """

    lock: Lock = Lock()
    queue = get_text_queue("text.txt")
    queue_size: int = queue.qsize()
    timer: int = 1

    try:
        data_accounts = get_data_accounts_vk("tokens.txt")

    except ApiVkServiceError:
        print("Ошибка получения данных Vk аккаунтов")

    try:
        executor = ThreadPoolExecutor()

        for account, user in data_accounts.items():
            executor.submit(
                process_vk_chat, account, user, lock, queue, queue_size, timer
            )
            timer += 1

    except ApiVkServiceError:
        print("Ошибка при работе с Vk беседой")

    finally:
        executor.shutdown()


if __name__ == "__main__":
    main()
