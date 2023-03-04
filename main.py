from utils import get_data, get_filtered_data, get_last_data, get_formatted_data


def main():
    """
    Функция возвращает информацию о статусе получения данных из json-файла по ссылке (operations_url),
    выводит 5 последних (count_last_values) успешных (EXECUTED) транзакций
    """
    operations_url = "https://api.npoint.io/b4be3cfb294b7cd84ff9"
    count_last_values = 5
    filtered_empty_from = True

    data, info = get_data(operations_url)
    # Проверка получения данных data, в случае False выход из программы с выводом инфо о статусе ошибки
    if not data:
        exit(info)
    print(info)

    data = get_filtered_data(data, filtered_empty_from)
    data = get_last_data(data, count_last_values)
    data = get_formatted_data(data)
    # Печать элементов подготовленного списка дата через цикл по элеиентам этого списка
    for row in data:
        print(row)


if __name__ == "__main__":
    main()
