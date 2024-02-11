from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from web.forms import RegistrationForm, AuthForm, EventSlotForm, EventSlotTagForm
from web.models import EventSlot, EventSlotTag

User = get_user_model()

def main_view(request):
    eventslots = EventSlot.objects.all()
    return render(request, "web/main.html", {
        'eventslots': eventslots
    })


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                emil=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            is_success = True
            print(form.cleaned_data)
    return render(request, "web/registration.html", {"form": form, "is_success": is_success})

def auth_view(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Введены неверные данные")
            else:
                login(request, user)
                return redirect("main")
    return render(request, "web/auth.html", {'form': form})

def logout_view(request):
    logout(request)
    return redirect("main")

#def event_slot_edit_view(request, id=None):
#        eventslot = EventSlot.objects.get(id=id) if id is not None else None
#    form = EventSlotForm(instance=eventslot)
#    if request.method == 'POST':
#        form = EventSlotForm(data=request.POST, files=request.FILES, initial={'user':request.user})
#        if form.is_valid():
#            form.save()
#            return redirect("main")
#    return render(request, "web/event_slot.html", {'form': form})

def tags_view(request):
    tags = EventSlotTag.objects.all()
    form = EventSlotTagForm()
    if request.method == 'POST':
        form = EventSlotTagForm(data=request.POST, initial={'user':request.user})
        if form.is_valid():
            form.save()
            return redirect('tags')
    return render(request, "web/tags.html", {'tags': tags, "form": form})