from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from lists.forms import ExistingListItemForm, ItemForm, NewListForm
from lists.models import Item, List

User = get_user_model()


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def new_list(request):
    form = NewListForm(data=request.POST)
    if form.is_valid():
        list_ = form.save(owner=request.user)
        return redirect(list_)
    return render(request, 'home.html', {'form': form})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    owner = list_.owner
    shared_with = list_.shared_with
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, 'form': form, 'owner': owner, 'shared_with': shared_with})


def my_lists(request, email):
    owner = User.objects.get(email=email)
    lists_shared_with_owner = owner.shared_with_list_set
    return render(request, 'my_lists.html', {'owner': owner, 'lists_shared_with_owner': lists_shared_with_owner})


def share_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        list_.shared_with.add(request.POST['email']) 
    return redirect(list_)
