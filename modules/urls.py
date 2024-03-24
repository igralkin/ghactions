from django.urls import path
from modules.apps import ModulesConfig
from modules.views import (ModuleListAPIView,
                           ModuleCreateAPIView,
                           ModuleRetrieveAPIView,
                           ModuleUpdateAPIView,
                           ModuleDestroyAPIView)

app_name = ModulesConfig.name

urlpatterns = [
    path('module/', ModuleListAPIView.as_view(), name='module_list'),
    path('module/create/', ModuleCreateAPIView.as_view(), name='module_create'),
    path('module/view/<int:pk>/', ModuleRetrieveAPIView.as_view(), name='module_view'),
    path('module/update/<int:pk>/', ModuleUpdateAPIView.as_view(), name='module_update'),
    path('module/delete/<int:pk>/', ModuleDestroyAPIView.as_view(), name='module_delete')
]
