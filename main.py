from utils import get_data, get_filtered_data, get_last_data, get_formatted_data


def main():
    """
    Функция возвращает информацию о статусе получения данных из json-файла по ссылке (operations_url),
    выводит 5 последних (count_last_values) успешных (EXECUTED) транзакций
    """
    operations_url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677856139653&signature=kAxhXa_UIHexLM3Rzan2zmshO9mpP0cSDxU0ziRMJq4&downloadName=operations.json"
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
    for row in data:
        print(row)


if __name__ == "__main__":
    main()
