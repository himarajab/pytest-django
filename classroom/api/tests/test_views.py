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
    self.client = APIClient()
    print(self.client,'my client')

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
    
    input_data = {
    "first_name": "ahmed",
    "last_name": "mohamed",
    "username": "",
    "admission_number": 987,
    "is_qualified": True,
    "average_score": 100
}

    url = reverse('student_cretae_api')

    response = self.client.post(url,data=input_data)
    # response = self.client.get('/api/student/list/')
    

    # print(dir(response))

    assert response.status_code == 201
    assert len(response.json()) != None
    assert Student.objects.count() == 1

  
  def test_student_detail_works(self):
    student = mixer.blend(Student,first_name='Hima')
    student2 = mixer.blend(Student,first_name='hima2')
    
    
    url = reverse('student_detail_api',kwargs={'pk':1})

    response = self.client.get(url)
    # response = self.client.get('/api/student/list/')
    
    # print(dir(response))

    assert response.status_code == 200
    assert len(response.json()) != None
    assert response.json()['first_name'] == 'Hima'
    assert response.json()['username'] == 'hima'


  def test_student_delete_works(self):
    student = mixer.blend(Student,first_name='Hima')
    url = reverse('student_delete_api',kwargs={'pk':1})

    response = self.client.delete(url)

    # assert response.status_code == 200
    print(f'\n {response.data} \n ')
    assert response.data is  None
    assert Student.objects.count() == 0


  
class TestClassroomAPIView(TestCase):
  def SetUp(self):
    self.client = APIClient()
    # User = get_user_model()
    # self.our_user = User.objects.create(username='test user',password='abcde')
    # self.token = Token.objects.create(user = our_user)
    # self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)
    # print(f'\n {self.token.key} \n')
    # import ipdb ; ipdb.set_trace()
    # print(self.client,'my client')

    User = get_user_model()
    self.our_user = User.objects.create_user(username='test user',password='abcde')
    self.token_url = 'http://localhost:8000/api-token-auth/'
    user_data = {
      'username':'testuser','password':'abcde'
    }
    response = self.client.post(self.token_url,data=user_data)
    import ipdb ; ipdb.set_trace()
    print(response.data,' response ')
    self.client.credentials(HTTP_AUTHORIZATION="Token "+ response.data['token'])

  def test_classroom_qs(self):
    classroom = mixer.blend(Classroom,student_capacity=20)
    classroom2 = mixer.blend(Classroom,student_capacity=27)
    url = reverse('class_qs_api',kwargs={'student_cabacity':15})

    response = self.client.get(url)
    # print(f'\n {vars(response.data)} \n')
    assert response.status_code == 202
    # import ipdb ; ipdb.set_trace()
    assert response.data['number_of_classes'] == 2
    assert response.data['classroom_data'] != []
