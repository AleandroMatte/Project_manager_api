'''
Test for models
'''

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    '''test models.'''

    def test_create_user_with_email_sucessfull(self):
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_user_email(self):
        sample = [
            ['teste1@Exemplo.com', "teste1@exemplo.com"],
            ['Teste2@EXEMPLO.com', "Teste2@exemplo.com"],
            ['TESTE3@EXEMPLO.COM', "TESTE3@exemplo.com"],
            ['teste4@exemplo.COM', 'teste4@exemplo.com']
        ]
        for email, email_corrigido in sample:
            user = get_user_model().objects.create_user(email, 'sample1234')
            self.assertEqual(user.email, email_corrigido)

    def test_new_user_without_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", 'test123')

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            'test@exemplo.com', 'pass123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)