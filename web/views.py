from django.shortcuts import render

def main_veiw(request):
    return render(request, "web/main.html")