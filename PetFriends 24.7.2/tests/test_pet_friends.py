from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """Проверяет возможность получения ключа auth_key с корректными данными"""
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    """Проверяет возможность получения списка созданных питомцев"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet(name='Бузуз', animal_type='Вомбат', age='3', pet_photo=r'C:\Users\nadya\PycharmProjects\PetFriends\venv\Images\17.jpg'):
    """Проверяет возможность добавления нового питомца без фото с корректными данными"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert len(result) > 0

def test_delete_pet(pet_id=''):
    """Проверяет возможность удаления существующего питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, result = pf.add_new_pet(auth_key, name='Кот', animal_type='Кот', age='6', pet_photo=r'C:\Users\nadya\PycharmProjects\PetFriends\venv\Images\17.jpg')
    pet_id = result['id']
    status, result = pf.delete_pet(auth_key, pet_id)
    assert status == 200

def test_update_information_about_pet(pet_id=''):
    """Проверяет возможность обновления информации о питомце с корректными данными"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, result = pf.add_new_pet(auth_key, name='Кот', animal_type='Кот', age='6',
                               pet_photo=r'C:\Users\nadya\PycharmProjects\PetFriends\venv\Images\17.jpg')
    pet_id = result['id']
    status, result = pf.update_information_about_pet(auth_key, pet_id, name='Пес', animal_type='Пес', age='7')
    assert status == 200

def test_add_new_pet_without_photo(name='Собаня', animal_type='Пес', age='10'):
    """Проверяет возможность добавления питомца без фото с корректными данными"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert len(result) > 0

def test_add_photo_of_pet(pet_id='', pet_photo=r'C:\Users\nadya\PycharmProjects\PetFriends\venv\Images\Вася.jpg'):
    """Проверяет возможность добавления фото к существующему питомцу с корректными данными"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, result = pf.create_pet_without_photo(auth_key, name='Вася', animal_type='Кот', age='2')
    pet_id = result['id']
    status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)
    assert status == 200

def test_add_new_pet_with_too_much_value(name='Бузуз', animal_type='Вомбат', age='1508', pet_photo=r'C:\Users\nadya\PycharmProjects\PetFriends\venv\Images\17.jpg'):
    """Проверяет возможность создать питомца со слишком большим значением возраста"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert len(result) > 0

def test_add_new_pet_with_negative_age(name='Бузуз', animal_type='Вомбат', age='-5', pet_photo=r'C:\Users\nadya\PycharmProjects\PetFriends\venv\Images\17.jpg'):
    """Проверяет возможность создать нового питомца с отрицательным значением возраста"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert len(result) > 0

def test_get_api_key_without_email(email='', password=valid_password):
    """Проверяет что нельзя получить api_key при пустом значении поля email"""
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_add_new_pet_with_number_name(name=123456, animal_type='Вомбат', age='3', pet_photo=r'C:\Users\nadya\PycharmProjects\PetFriends\venv\Images\17.jpg'):
    """Проверяет что нельзя добавить питомца с численным значением вместо букв"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert len(result) > 0

def test_add_new_pet_with_invalid_type_of_photo(name='Бузуз', animal_type='Вомбат', age='3', pet_photo=r'C:\Users\nadya\PycharmProjects\PetFriends\venv\Images\кот-чавкает.gif'):
    """Проверяет что нельзя добавить питомца с некорректным типом фото"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert len(result) > 0

def test_get_all_pets_with_invalid_key(auth_key='123456', filter=''):
    """Проверяет что нельзя получить список питомцев с некорректным auth_key"""
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200

def test_add_new_pet_with_num_age(name='Собаня', animal_type='Пес', age=10):
    """Проверяет что нельзя добавить питомца с типом данных int вместо str в поле возраст"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200

def test_add_new_pet_with_num_animal_type(name='Собаня', animal_type='43434', age=10):
    """Проверяет что нельзя добавить питомца с численным значением в поле animal_type """
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200

def test_add_new_pet_with_empty_pet_photo(name='Бузуз', animal_type='Вомбат', age='3', pet_photo=r''):
    """Проверяет что нельзя добавить питомца с пустым полем pet_photo"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200

def test_get_api_key_for_invalid_email(email="abc@@yandex.ru", password=valid_password):
    """Проверяет что нельзя получить api_key c некорректным значением поля email"""
    status, result = pf.get_api_key(email, password)
    assert status == 200




