from django.db.models import Count, Avg, Max, Q
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Dna
from .serializers import DnaSerializer


class DnaListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.AllowAny]

    # 1. List all
    def get(self, request, *args, **kwargs):
        # Получаем параметр species из query params
        species = request.query_params.get('species', None)

        # Если параметр не указан, возвращаем все записи, иначе фильтруем
        if species:
            dnas = Dna.objects.filter(species=species)
        else:
            dnas = Dna.objects.all()
        serializer = DnaSerializer(dnas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Dna with given dna data
        '''
        data = {
            "animal_name": request.data.get('animal_name'),
            "species": request.data.get('species'),
            "test_date": request.data.get('test_date'),
            "milk_yield": request.data.get('milk_yield'),
            "health_status": request.data.get('health_status'),
        }
        serializer = DnaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatisticsView(APIView):
    permission_classes = []  # Если не нужна аутентификация
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        # Выполняем агрегирующий запрос
        data = Dna.objects.values('species').annotate(
            total_tests=Count('id'),
            avg_milk_yield=Avg('milk_yield'),
            max_milk_yield=Max('milk_yield'),
            good_health_count=Count('id', filter=Q(health_status="good"))
        )

        # Преобразуем результат в нужный формат
        result = []
        for item in data:
            total_tests = item['total_tests']
            good_health_count = item['good_health_count']
            # Рассчитываем процент хорошего здоровья
            good_health_percentage = (good_health_count / total_tests * 100) if total_tests else 0

            result.append({
                "species": item['species'],
                "total_tests": total_tests,
                "avg_milk_yield": float(item['avg_milk_yield']) if item['avg_milk_yield'] is not None else 0,
                "max_milk_yield": float(item['max_milk_yield']) if item['max_milk_yield'] is not None else 0,
                "good_health_percentage": good_health_percentage
            })

        return Response({"statistics": result}, status=status.HTTP_200_OK)
