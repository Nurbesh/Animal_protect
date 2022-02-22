from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from .permission import IsActive, IsAuthorPermission
from .serializers import AnimalSerializer
from .models import Animal
from rest_framework.permissions import AllowAny


class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsActive]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorPermission]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]


class AnimalView(PermissionMixin, ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]

    filterset_fields = ['types']
    search_fields = ['name']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    def partial_update(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=kwargs.get('pk'))
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context













# class RetrieveUpdateDestroyAnimalAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = AnimalSerializer
#     queryset = Animal.objects.all()
#     permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]



