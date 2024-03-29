from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    


# from django.http.response import JsonResponse
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from students.models import Student
# from students.serializers import StudentSerializer

# class StudentView(APIView):
#     def get(self, request, pk=None):
#         if pk:
#             student = Student.objects.get(studentId=pk)
#             serializer = StudentSerializer(student)
#             return Response(serializer.data)
#         else:
#             students = Student.objects.all()
#             serializer = StudentSerializer(students, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Student added successfully", status=201)
#         return JsonResponse(serializer.errors)

#     def put(self, request, pk):
#         student = Student.objects.get(studentId=pk)
#         serializer = StudentSerializer(instance=student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Student updated successfully", status=200)
#         return JsonResponse(serializer.errors)

#     def delete(self, request, pk):
#         student = Student.objects.get(studentId=pk)
#         student.delete()
#         return JsonResponse("Student deleted successfully", status=200)
