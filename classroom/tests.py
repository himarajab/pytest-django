from .models import Student
from django.test import TestCase

# Create your tests here.

class TestStudentmodel(TestCase):
  def setUp(self):
    self.student1 = Student.objects.create(
      first_name = "Tom",
      last_name = "hima",
      admission_number=12345,

    )
  
  def test_student_can_created(self):
    # student1 = Student.objects.create(
    #   first_name = "Tom",
    #   last_name = "hima",
    #   admission_number=1234,

    # )

    # student_result = Student.objects.last()

    self.assertEqual(self.student1.first_name ,'Tom')

  def test_str_resturn_self(self):
    # student1 = Student.objects.create(
    #   first_name = "Tom",
    #   last_name = "hima",
    #   admission_number=1234,

    # )

    # student_result = Student.objects.last()

    self.assertEqual(str(self.student1) ,'Tom')

  def test_grade_fail(self):
    # student1 = Student.objects.create(
    #   first_name = "Tom",
    #   last_name = "hima",
    #   admission_number=1234,
    #   average_score=10
    # )

    # student_result = Student.objects.last()

    self.assertEqual(self.student1.get_grade() ,"Fail")


  def test_grade_pass(self):
      # student1 = Student.objects.create(
      #   first_name = "Tom",
      #   last_name = "hima",
      #   admission_number=1234,
      #   average_score=60
      # )

      # student_result = Student.objects.last()

      self.assertEqual(self.student1.get_grade() ,"Pass")


  def test_grade_excellent(self):
      # student1 = Student.objects.create(
      #   first_name = "Tom",
      #   last_name = "hima",
      #   admission_number=1234,
      #   average_score=90
      # )

      # student_result = Student.objects.last()

      self.assertEqual(self.student1.get_grade() ,"Excellent")
