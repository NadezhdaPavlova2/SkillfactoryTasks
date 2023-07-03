import requests

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"



    def get_api_key(self, email:str , password:str):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с уникальным ключем пользователя, найденного по указанным email и паролем"""
        headers = {
            'email': email,
            'password': password
        }

        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result



    def get_list_of_pets(self, auth_key:str, filter: str = ''):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат
        в формате JSON со списком найденных питомцев, совпадающих с фильтром. На данный
        момент фильтр может иметь либо пустое значение - получить список всех питомцев, либо
        'my_pets' - получить список собственных питомцев"""
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result



    def add_new_pet(self, auth_key:str, name:str, animal_type:str, age:str, pet_photo:str):
        """Метод делает запрос к API сервера, отправляет данные о питомце и возвращает статус запроса
        и результат в формате JSON c информацией о добавленном питомце"""
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        headers = {'auth_key': auth_key['key']}
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}
        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data, files=file)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text
        return status, result


    def delete_pet(self, auth_key:str, pet_id:str):
        """Метод делает запрос к API сервера и возвращает статус запроса
        200 если питомец удален"""
        headers = {'auth_key': auth_key['key']}
        res = requests.delete(self.base_url + f'/api/pets/{pet_id}', headers=headers)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


    def update_information_about_pet(self, auth_key:str, pet_id:str, name:str, animal_type:str, age:str):
        """Метод делает запрос к API сервера, отправляет измененные данные о питомце и возвращает статус
        запроса и результат в формате JSON c информацией об измененном питомце"""
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        headers = {'auth_key': auth_key['key']}
        res = requests.put(self.base_url + f'/api/pets/{pet_id}', headers=headers, data=data)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


    def create_pet_without_photo(self, auth_key:str, name:str, animal_type:str, age:str):
        """Метод делает запрос к API сервера, отправляет данные о питомце и его фото и возвращает статус
         запроса и результат в формате JSON c информацией о добавленном питомце"""
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        headers = {'auth_key': auth_key['key']}
        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text
        return status, result


    def add_photo_of_pet(self, auth_key:str, pet_id:str, pet_photo:str):
        """Метод делает запрос к API сервера, отправляет фото питомца и возвращает статус запроса
        и результат в формате JSON c информацией о добавленном питомце"""
        headers = {'auth_key': auth_key['key']}
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}
        res = requests.post(self.base_url + f'/api/pets/set_photo/{pet_id}', headers=headers, files=file)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result