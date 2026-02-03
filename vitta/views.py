from django.http import HttpResponse
from django.contrib.auth import get_user_model

def bootstrap(request):
    User = get_user_model()

    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            "admin",
            "admin@vitta.com",
            "SenhaForte123"
        )
        return HttpResponse("Admin criado com sucesso")

    return HttpResponse("Admin já existe")
