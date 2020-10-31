from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from mixer.backend.django import mixer
import pytest
from classroom.models import Student,Classroom

class TestStudentAPIView(TestCase):
    def SetUp(self):
        self.my_client = APIClient()
        print(self.client,'my client')
        User = get_user_model()

        self.our_user = User.objects.create_user(username="testuser", password="abcde")

        self.token_url = "http://localhost:8000/api-token-auth/"

        user_data = {"username": "testuser", "password": "abcde"}

        response = self.client.post(self.token_url, data=user_data)

        # print(dir(response.), "reponse")
        print((response.data), "reponse")
        """
                {
            "token": "b89d0bab1b4f818c5af6682cec66f84b0bdb664c"
        }
        """
        
        self.my_client.credentials(HTTP_AUTHORIZATION="Token " + response.data["token"])

    def test_student_list_works(self):
      
        student = mixer.blend(Student,first_name='hima')
        student2 = mixer.blend(Student,first_name='hima2')
        url = reverse('student_list_api')

        response = self.client.get(url)
        # response = self.client.get('/api/student/list/')
        

        # print(dir(response))

        assert response.status_code == 200
        assert len(response.json()) == 2


    def test_student_create_works(self):
        # data
        self.my_client = APIClient()
        print(self.client,'my client')
        User = get_user_model()

        self.our_user = User.objects.create_user(username="testuser", password="abcde")

        self.token_url = "http://localhost:8000/api-token-auth/"

        user_data = {"username": "testuser", "password": "abcde"}

        response = self.client.post(self.token_url, data=user_data)

        # print(dir(response.), "reponse")
        print((response.data), "reponse")
        """
                {
            "token": "b89d0bab1b4f818c5af6682cec66f84b0bdb664c"
        }
        """
        
        self.my_client.credentials(HTTP_AUTHORIZATION="Token " + response.data["token"])
        input_data = {
            "first_name": "Wangari",
            "last_name": "Maathai",
            "username": "",
            "admission_number": 9876,
            "is_qualified": True,
            "average_score": 100,
        }

        url = reverse("student_create_api")

        # call the url
        response = self.my_client.post(url, data=input_data)
        # import ipdb ; ipdb.set_trace()
        # assertions
        # - json
        # - status

        print(response.data)
        assert response.json() != None
        assert response.status_code == 201
        assert Student.objects.count() == 1


    def test_student_detail_works(self):
        student = mixer.blend(Student,pk=1,first_name='Hima')
        student2 = mixer.blend(Student,pk=2,first_name='hima2')
        
        
        url = reverse('student_detail_api',kwargs={'pk':1})

        response = self.client.get(url)
        # response = self.client.get('/api/student/list/')
        
        # print(dir(response))

        assert response.status_code == 200
        assert len(response.json()) != None
        assert response.json()['first_name'] == 'Hima'
        assert response.json()['username'] == 'hima'


    def test_student_delete_works(self):
        self.my_client = APIClient()
        print(self.client,'my client')
        User = get_user_model()

        self.our_user = User.objects.create_user(username="testuser", password="abcde")

        self.token_url = "http://localhost:8000/api-token-auth/"

        user_data = {"username": "testuser", "password": "abcde"}

        response = self.client.post(self.token_url, data=user_data)

        # print(dir(response.), "reponse")
        print((response.data), "reponse")
        """
                {
            "token": "b89d0bab1b4f818c5af6682cec66f84b0bdb664c"
        }
        """
        
        self.my_client.credentials(HTTP_AUTHORIZATION="Token " + response.data["token"])
        student = mixer.blend(Student,pk=1,first_name='Hima')
        assert Student.objects.count() == 1

        url = reverse('student_delete_api',kwargs={'pk':1})
        # import ipdb ; ipdb.set_trace()
        response = self.my_client.delete(url)

        # assert response.status_code == 200
        print(f'\n {response.data} \n ')
        assert response.data is  None
        assert Student.objects.count() == 0


  
class TestClassroomAPIViews(TestCase):
    def setUp(self):
        self.client = APIClient()

        print(self.client, "self.client")

        # method 1

        # from rest_framework.authtoken.models import Token

        # from django.contrib.auth import get_user_model

        # User = get_user_model()

        # self.our_user = User.objects.create(username="testuser", password="abcde")

        # self.token = Token.objects.create(user=self.our_user)

        # print(self.token.key, "token")

        # self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        # method 2 # normal

        User = get_user_model()

        self.our_user = User.objects.create_user(username="testuser", password="abcde")

        self.token_url = "http://localhost:8000/api-token-auth/"

        user_data = {"username": "testuser", "password": "abcde"}

        response = self.client.post(self.token_url, data=user_data)

        # print(dir(response.), "reponse")
        print((response.data), "reponse")
        """
                {
            "token": "b89d0bab1b4f818c5af6682cec66f84b0bdb664c"
        }
        """
        
        self.client.credentials(HTTP_AUTHORIZATION="Token " + response.data["token"])

    def test_classroom_qs_works(self):
        classroom = mixer.blend(Classroom, student_capacity=20)
        classroom2 = mixer.blend(Classroom, student_capacity=27)
        # import ipdb ; ipdb.set_trace()

        url = reverse("class_qs_api", kwargs={"student_capacity": 15})

        response = self.client.get(url,)

        assert response.status_code == 202
        assert response.data["classroom_data"] != []
        assert response.data["number_of_classes"] == 2
