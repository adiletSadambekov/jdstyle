from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from core.models import ApplicationCall, Product, ToNotification
from core.serializers import ProductSerializer, ApplicationCallSerializer

from core.management.commands.bot import bot

class ProductView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = LimitOffsetPagination


class ApplicationCallView(CreateAPIView):
    serializer_class = ApplicationCallSerializer
    queryset = ApplicationCall.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = dict(serializer.data)
        admins = ToNotification.objects.all()
        for admin in admins:
            try:
                bot.send_message(
                    admin.tg_id,
                    f'Новый запрос на перевон Имя: {data["name"]}\nконтакт: {data["phone_number"]}\nДата и время создания: {timezone.now().strftime("%y-%m-%d %H:%M")}'
                )
            except Exception as e:
                print(e)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)