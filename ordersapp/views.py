from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from ordersapp.models import Order


class OrderList(ListView):
    pass

class OrderCreate(CreateView):
    pass

class OrderUpdate(UpdateView):
    pass

class OrderDelete(DeleteView):
    pass

class OrderDetail(DetailView):
    pass

# функция для замены статуса
def order_forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SEND_TO_PROCEED
    order.save()
    return HttpResponseRedirect(reverse('orders:list'))