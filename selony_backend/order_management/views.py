import json

from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.http import JsonResponse

from order_management.models import Order, OrderStatus


class WebHookView(CreateView):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(WebHookView, self).dispatch(*args, **kwargs)

    def post(self, request):

        resp = json.loads(request.body.decode("utf-8"))
        print("resp", resp)

        if resp['type'] == "payment_intent.succeeded":
            metadata = resp['data']['object']['metadata']
            order = metadata.get('order')
            ords = Order.objects.filter(id=order)

            if len(ords):
                ord_obj = ords[0]
                ord_obj.status = OrderStatus.PaymentCompleted.value
                ord_obj.last_status_change = timezone.now()
                ord_obj.payment_info = resp['data']['object']
                ord_obj.save()

        if resp['type'] == "payment_intent.payment_failed":

            metadata = resp['data']['object']['metadata']
            order = metadata.get('order')
            ords = Order.objects.filter(id=order)

            if len(ords):
                ord_obj = ords[0]
                ord_obj.status = OrderStatus.PaymentFailed.value
                ord_obj.last_status_change = timezone.now()
                ord_obj.payment_info = resp['data']['object']
                ord_obj.save()

        if resp['type'] == "payment_intent.canceled":

            metadata = resp['data']['object']['metadata']
            order = metadata.get('order')
            ords = Order.objects.filter(id=order)

            if len(ords):
                ord_obj = ords[0]
                ord_obj.status = OrderStatus.PaymentCancelled.value
                ord_obj.last_status_change = timezone.now()
                ord_obj.payment_info = resp['data']['object']
                ord_obj.save()

        return JsonResponse({"msg": "webhook executed successfully."},
                            status=200)
