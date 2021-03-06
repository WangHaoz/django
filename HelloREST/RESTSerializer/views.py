from django.http import JsonResponse
from django.views import View
from rest_framework.parsers import JSONParser

from RESTSerializer.models import Person, Student
from RESTSerializer.serializers import PersonSerializer, StudentSerializer


class PersonView(View):

    def get(self, request):
        persons = Person.objects.all()

        person_serializer = PersonSerializer(persons, many=True)

        return JsonResponse(person_serializer.data, safe=False)

    def post(self, request):
        p_name = request.POST.get('p_name')
        p_age = request.POST.get('p_age')

        person = Person()

        person.p_name = p_name
        person.p_age = p_age
        person.save()

        person_serializer = PersonSerializer(person)

        return JsonResponse(data=person_serializer.data)


class StudentView(View):

    def post(self, request):

        # s_name = request.POST.get('s_name')
        # s_age = request.POST.get('s_age')
        #
        # student = Student()
        # student.s_name = s_name
        # student.s_age = s_age
        # student.save()
        #
        # student_serializer = StudentSerializer(student)
        #
        # return JsonResponse(student_serializer.data)

        # 接收前端传过来的json数据  并转变成python的字典
        data = JSONParser().parse(request)
        print(data)
        print(type(data))
        # 将python字典恢复成正常的对象实例
        student_serializer = StudentSerializer(data=data)
        print(student_serializer)
        print(type(student_serializer))
        # 检测对象是否符合字段的要求
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=201)


        return JsonResponse(student_serializer.errors, status=400)



