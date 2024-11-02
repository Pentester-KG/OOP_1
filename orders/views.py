from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Order
from .forms import OrderForm


class CreateOrderAPIView(generic.CreateView):
    template_name = "orders/create_order.html"
    form_class = OrderForm
    success_url = '/orders/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateOrderAPIView, self).form_valid(form=form)


class ListOrdersView(generic.ListView):
    template_name = "orders/orders.html"
    context_object_name = 'orders'
    model = Order


class DetailOrderView(generic.DetailView):
    template_name = "orders/order_detail.html"
    context_object_name = "order"
    pk_url_kwarg = 'id'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get("id")
        return get_object_or_404(Order, id=order_id)


class RemoveOrderView(generic.DeleteView):
    template_name = "orders/remove_order.html"
    success_url = '/orders/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get("id")
        return get_object_or_404(Order, id=order_id)


class SearchOrderView(generic.ListView):
    template_name = "orders/orders.html"
    context_object_name = "orders"
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Order.objects.filter(order_id__icontains=query).order_by('order_id')
        return Order.objects.all().order_by('order_id')

