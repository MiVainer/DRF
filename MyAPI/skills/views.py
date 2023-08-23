from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView

from .models import Skills, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializer import SkillSerializer

# ViewSet заменяет всю хрень которую мы писали ниже !! Замечательная штука ViewSet!
'''class SkillViewSet(viewsets.ModelViewSet):
    #queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self): #Изменение вывода записей
        pk = self.kwargs.get("pk")

        if not pk:
            return Skills.objects.all()[:8] # Вывести первые 8 записей таблицы
        return Skills.objects.filter(pk=pk)
    @action(methods=['get'], detail=True) # Определение нового маршрута, выводим список из таблицы Category
    def category(self, request, pk):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})
'''


#  3 класса ниже можно заменить одним ViewSet
class SkillAPIList(generics.ListCreateAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer # название сериализатора из serializer.py
    permission_classes = (IsAuthenticatedOrReadOnly, ) #Настраиваем возможность просмотра только для авторизованнх пользователей


class SkillAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (IsAuthenticated, )

class SkillAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (IsAdminOrReadOnly, ) #Удаление записей разрешено только админу

# класс SkillAPIList заменяет написанный ниже класс SkillAPIView, SkillAPIView использовался
# в качестве подробного разбора работы
'''class SkillAPIView(APIView):
    #Передаём сериализованные данные пользователю
    def get(self, request):
        w = Skill.objects.all()
        return Response({'skill': SkillSerializer(w, many=True).data}) # many указывает что обрабатывается не одна запись, а список
    # Получаем данные от пользователя в виде байтовой json строки и переводим в словарь понятный базе данных методом Response.
    def post(self, request):
        # Проверяем данные на ошибки (например указанны не все поля)
        serializer = SkillSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Метод save вызывает create из serializer.py
        serializer.save()
        return Response({'post': serializer.data})

    # Обновление записей таблицы БД, обращение к методу update сериализатора
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Skill.objects.get(pk=pk)

        except:
            return Response({"error": "Objects does not exists"})

        serializer = SkillSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        try:
            instance = Skill.objects.get(pk=pk)
        except:
            return Response({"error": "Objects does not exists"})

        instance.delete()

        return Response({"post": "delete post " + str(pk)})
'''

