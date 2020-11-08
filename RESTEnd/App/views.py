import uuid

from django.core.cache import cache
from django.shortcuts import render
from rest_framework import exceptions, status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import viewsets

from App.auth import LoginAuthentication
from App.models import UserModel, Address
from App.permissions import RequireLoginAddressPermission
from App.serializers import UserSerializer, AddressSerializer


class UsersAPIView(CreateAPIView):

    serializer_class = UserSerializer

    queryset = UserModel.objects.all()

    def post(self, request, *args, **kwargs):
        # 获取url地址?后的参数名为action对应的值
        action = request.query_params.get('action')

        if action == 'login':
            # 获取提交的值
            u_name = request.data.get('u_name')
            u_password = request.data.get('u_password')
            try:
                user = UserModel.objects.get(u_name=u_name)

                if user.u_password != u_password:
                    raise exceptions.AuthenticationFailed

                token = uuid.uuid4().hex

                cache.set(token, user.id)

                data = {
                    'msg': 'login success',
                    'status': 200,
                    'token': token,
                }

                return Response(data)

            except UserModel.DoesNotExist:
                raise exceptions.NotFound
        elif action == 'register':
            return self.create(request, *args, **kwargs)
        else:
            raise exceptions.ParseError


class UserAPIView(RetrieveAPIView):

    serializer_class = UserSerializer

    queryset = UserModel.objects.all()

    authentication_classes = (LoginAuthentication,)

    permission_classes = (RequireLoginAddressPermission,)

    def retrieve(self, request, *args, **kwargs):
        # 验证url地址路径里请求的id是不是用户自己的
        # kwargs.get('pk')获取路径中的id
        if kwargs.get('pk') != str(request.user.id):
            raise exceptions.AuthenticationFailed
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class AddressAPIView(viewsets.ModelViewSet):

    serializer_class = AddressSerializer

    queryset = Address.objects.all()

    authentication_classes = (LoginAuthentication,)

    permission_classes = (RequireLoginAddressPermission,)




    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        user = request.user

        address_id = serializer.data.get('id')

        # print(address_id)

        address = Address.objects.get(pk=address_id)

        address.a_user = user

        address.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.queryset.filter(a_user=request.user))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        # 验证url地址路径里请求的id是不是用户自己的
        print(Address.objects.filter(a_user=request.user).filter(id=kwargs.get('pk')).exists())
        if not Address.objects.filter(a_user=request.user).filter(id=kwargs.get('pk')).exists():
            raise exceptions.AuthenticationFailed
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
