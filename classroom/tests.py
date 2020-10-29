from .models import Student
from django.test import TestCase
from mixer.backend.django import mixer
# Create your tests here.

class TestStudentmodel(TestCase):
  # def setUp(self):
  #   self.student1 = Student.objects.create(
  #     first_name = "Tom",
  #     last_name = "hima",
  #     admission_number=1234,

  #   )
  
  def test_student_can_created(self):
    
    student1 = mixer.blend(Student,first_name='Tom')
    student_result = Student.objects.last()

    self.assertEqual(student_result.first_name ,'Tom')

  def test_str_resturn_self(self):
   
    student1 = mixer.blend(Student,first_name='Tom')


    student_result = Student.objects.last()

    self.assertEqual(str(student_result) ,'Tom')

  def test_grade_fail(self):
   
    student1 = mixer.blend(Student,average_score=10)

    student_result = Student.objects.last()

    self.assertEqual(student_result.get_grade() ,"Fail")


  def test_grade_pass(self):
    student1 = mixer.blend(Student,average_score=60)
    student_result = Student.objects.last()

    self.assertEqual(student_result.get_grade() ,"Pass")


  def test_grade_excellent(self):
    student1 = mixer.blend(Student,average_score=90)

    student_result = Student.objects.last()

    self.assertEqual(student_result.get_grade() ,"Excellent")
