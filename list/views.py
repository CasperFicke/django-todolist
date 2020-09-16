from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# home view
def home(request):
  if request.method == 'POST':
    form = ItemForm(request.POST or None)
    if form.is_valid():
      form.save()
      all_items = Item.objects.all
      messages.success(request, ('Item added succesfully'))
      return render(request, 'home.html', {'all_items': all_items})
  else:
    all_items = Item.objects.all
    return render(request, 'home.html', {'all_items': all_items})

# edit item view
def edit(request, item_id):
  if request.method == 'POST':
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
      form.save()
      messages.success(request, ('Item updated'))
      return redirect('home')
  else:
    item = Item.objects.get(pk=item_id)
    return render(request, 'edit.html', {'item': item})

# delete item view
def delete(request, item_id):
  todo_item = Item.objects.get(pk=item_id)
  todo_item.delete()
  messages.success(request, ("Item has been deleted!"))
  return redirect('home')

# cross item view
def cross_off(request, item_id):
  item = Item.objects.get(pk=item_id)
  item.completed = True
  item.save()
  return redirect('home')

# uncross item view
def uncross(request, item_id):
  item = Item.objects.get(pk=item_id)
  item.completed = False
  item.save()
  return redirect('home')

# about view
def about(request):
  myfirst_name = 'Casper'
  mylast_name  = 'Ficke'
  context = {'first_name': myfirst_name, 'last_name': mylast_name}
  return render(request, 'about.html', context)