from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignUpPageView

# Create your tests here.

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='j',
            password='full',
            email='12@12.com'       
        )

        self.assertEqual(user.username,'j')
        self.assertEqual(user.email,'12@12.com')
        
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User= get_user_model()

        admin_user = User.objects.create_superuser(
            username ='admin',
            email ='email@admin.com',
            password='boss'
        )

        self.assertEqual(admin_user.username,'admin')
        self.assertEqual(admin_user.email,'email@admin.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class SignUpPageTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_sign_up_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response,'signup.html')
        self.assertContains(self.response,"Sign up")
        self.assertNotContains(self.response,"not here")

    def test_sign_up_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form,CustomUserCreationForm)

    def test_sign_up_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__,SignUpPageView.as_view().__name__)

