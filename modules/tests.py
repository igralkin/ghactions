from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from modules.models import Module
from modules.serializers import ModuleSerializer


class ModuleTestCase(APITestCase):

    def setUp(self):
        self.module_attributes = {
            'name': 'test',
            'description': 'a long description',
            'education_time': 5
        }

        # Создаем модуль для тестов
        self.module = Module.objects.create(**self.module_attributes)
        self.serializer = ModuleSerializer(instance=self.module)

    def test_get_list(self):
        """ Тестируем получение списка учебных модулей """
        response = self.client.get(
            reverse('modules:module_list')
        )

        # Проверяем, что полученный ответ соответствует ожидаемому формату
        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.module.pk,
                        "name": 'test',
                        "description": 'a long description',
                        "education_time": 5
                    }
                ]
            }
        )

    def test_module_create(self):
        """ Тестируем создание учебного модуля """
        data = {
            'name': 'module_name',
            'description': 'module_description',
            'education_time': 10
        }

        response = self.client.post(
            reverse('modules:module_create'),
            data=data
        )

        # Проверяем, что модуль успешно создан
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # Проверяем, что теперь в базе данных два модуля
        self.assertEqual(
            Module.objects.all().count(),
            2
        )

    def test_module_retrieve(self):
        """ Тестируем получение учебного модуля """
        response = self.client.get(
            reverse('modules:module_view', args=[self.module.pk]),
        )

        # Проверяем, что полученный ответ соответствует ожидаемому формату
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "id": self.module.pk,
                "name": 'test',
                "description": 'a long description',
                "education_time": 5
            }
        )

    def test_module_update(self):
        """ Тестируем обновление учебного модуля """
        data = {
            'name': 'updated_name',
            'description': 'updated_description',
            'education_time': 8
        }
        response = self.client.put(
            reverse('modules:module_update', args=[self.module.pk]),
            data
        )

        # Проверяем, что модуль успешно обновлен
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Проверяем, что поле education_time обновлено
        self.module.refresh_from_db()
        self.assertEqual(self.module.education_time, 8)

    def test_module_delete(self):
        """ Тестируем удаление учебного модуля """
        response = self.client.delete(
            reverse('modules:module_delete', args=[self.module.pk])
        )

        # Проверяем, что модуль успешно удален
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_str(self):
        """ Тестируем метод __str__ """
        expected = 'test'
        actual = str(self.module.name)

        self.assertEqual(expected, actual)

    def test_contains_fields(self):
        """ Тестируем наличие полей """
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()),
            {'id', 'name', 'description', 'education_time'}
        )

    def test_education_time_field_content(self):
        """ Тестируем поле 'education_time' """
        data = self.serializer.data
        self.assertEqual(
            data['education_time'],
            self.module_attributes['education_time']
        )

    def test_description_field_content(self):
        """ Тестируем поле 'description' """
        expected = 'a long description'
        actual = self.module.description
        self.assertEqual(expected, actual)
