from queue import Queue


def get_text_queue(filename: str) -> Queue:
    """
    Формирование очереди из текста файла.

    :param filename: Файл с текстом
    :return: Queue
    """

    queue: Queue = Queue()

    with open(filename, encoding="utf-8") as file_text:
        for row in file_text:
            queue.put(row.strip())

    return queue
