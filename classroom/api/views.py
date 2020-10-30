from rest_framework import status,permissions,authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.response import Response

from .serializers import StudentSerializer,ClassroomSerializer
# from .serializers import StudentSerializer, ClassroomSerializer
from classroom.models import Student, Classroom

class StudentListAPIView(ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentCreateAPIView(CreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentDetailAPIView(RetrieveAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class StudentDeleteAPIView(DestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class ClassroomNumberAPIView(APIView):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        authentication.TokenAuthentication
    ]

    def get(self,*args, **kwargs):

        url_number = self.kwargs.get('student_cabacity')
        print(url_number,'student_cabacity')

        
        classroom_qs = Classroom.objects.filter(student_capacity__gte=url_number)

        serialized_data = ClassroomSerializer(classroom_qs,many=True)
        number_of_classes = classroom_qs.count()
        if serialized_data.is_valid:
            return Response(
                {
                    'classroom_data':serialized_data.data,
                    'number_of_classes':number_of_classes
                },
                status=status.HTTP_202_ACCEPTED,
                )
        else:
            return Response({'error':'error happen'})


