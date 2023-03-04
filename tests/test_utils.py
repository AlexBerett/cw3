from utils import get_data, get_last_data, get_formatted_data, get_filtered_data


def test_get_data():
    """
    Функция тестирует функцию get_data
    """
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677856139653&signature=kAxhXa_UIHexLM3Rzan2zmshO9mpP0cSDxU0ziRMJq4&downloadName=operations.json"
    assert get_data(url) is not None

    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677856139653&signature=kAxhXa_UIHexLM3Rzan2zmshO9mpP0cSDxU0ziRMJq4&downloadNam=operations.json"
    data, info = get_data(url)
    assert data is None
    assert info == "warning: Статус ответа 400"

    url = "https://fil.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677856139653&signature=kAxhXa_UIHexLM3Rzan2zmshO9mpP0cSDxU0ziRMJq4&downloadNam=operations.json"
    data, info = get_data(url)
    assert data is None
    assert info == "error: requests.exceptions.ConnectionError"


def test_get_filtered_data(test_data):
    """
    Функция тестирует функцию get_filtered_data
    :param test_data: фикстура для теста
    """
    data = get_filtered_data(test_data)
    assert len(data) == 4
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 3


def test_get_last_data(test_data):
    """
    Функция тестирует функцию get_last_data
    :param test_data: фикстура для теста
    """
    data = get_last_data(test_data, count_last_values=2)
    assert data[0]['date'] == '2021-04-04T23:20:05.206878'
    assert len(data) == 2


def test_get_formatted_data(test_data):
    """
    Функция тестирует функцию get_formatted_data
    :param test_data: фикстура для теста
    """
    data = get_formatted_data(test_data[:1])
    assert data == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n']
    data = get_formatted_data(test_data[3:4])
    assert data == ['23.03.2018 Открытие вклада\n[СКРЫТО]  -> Счет **2431\n48223.05 руб.\n']
