from hypothesis.extra.django import TestCase
import pytest
from .models import Student,Classroom
from mixer.backend.django import mixer
from hypothesis import given,settings , strategies as st

# Create your tests here.

# don't write the data to the db instead create it in memory
pytestmark = pytest.mark.django_db

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

    # self.assertEqual(student_result.first_name ,'Tom')
    assert student_result.first_name =='Tom'
  
  
  def test_str_resturn_self(self):
   
    student1 = mixer.blend(Student,first_name='Tom')


    student_result = Student.objects.last()

    assert str(student_result) =='Tom'


  # @given(st.characters)
  # def test_slugify(self,name):
  #   student1 = mixer.blend(Student,first_name='Tom')


  #   student_result = Student.objects.last()

  #   assert len(str(student_result.username)) == len(name)



  @given(st.floats(min_value=0, max_value=40))
  def test_grade_fail(self,fail_score):
   
    student1 = mixer.blend(Student,average_score=fail_score)

    student_result = Student.objects.last()

    assert student_result.get_grade() =="Fail"

  @given(st.floats(min_value=40, max_value=70))
  def test_grade_pass(self,pass_grade):
    student1 = mixer.blend(Student,average_score=pass_grade)
    student_result = Student.objects.last()

    assert student_result.get_grade() =="Pass"

  @given(st.floats(min_value=70, max_value=100))
  def test_grade_excellent(self,excllent_grade):
    student1 = mixer.blend(Student,average_score=excllent_grade)

    student_result = Student.objects.last()

    assert student_result.get_grade() =="Excellent"

  @given(st.floats(min_value=101))
  def test_grade_error(self,error_grade):
    student1 = mixer.blend(Student,average_score=error_grade)

    student_result = Student.objects.last()

    assert student_result.get_grade() =="Error"


class TestClassroomModel:
  def test_classroom_crete(self):
    classroom = mixer.blend(Classroom,name='math')
    classroom_result = Classroom.objects.last()

    assert str(classroom_result) == 'math'