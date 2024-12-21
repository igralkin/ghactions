from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView)
from modules.models import Module
from modules.paginators import ModulePaginator
from modules.serializers import ModuleSerializer


class ModuleListAPIView(ListAPIView):
    """ Возвращает список всех модулей """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all().order_by('id')
    pagination_class = ModulePaginator


class ModuleCreateAPIView(CreateAPIView):
    """ Создание модели """
    serializer_class = ModuleSerializer


class ModuleRetrieveAPIView(RetrieveAPIView):
    """ Детальный обзор модуля по id """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


class ModuleUpdateAPIView(UpdateAPIView):
    """ Изменение  модуля по id """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


class ModuleDestroyAPIView(DestroyAPIView):
    """ Удаление модуля по id """
    queryset = Module.objects.all()
