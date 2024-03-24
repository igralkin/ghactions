from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTestCase(TestCase):

    def test_create_user(self):
        User = get_user_model()
        email = 'test@test.ru'
        password = 'test'

        # Создание пользователя
        user = User.objects.create(
            email=email,
            first_name='test',
            last_name='test',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        user.set_password(password)
        user.save()

        # Проверка, что пользователь успешно создан
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)

        # Удаление пользователя
        user.delete()
