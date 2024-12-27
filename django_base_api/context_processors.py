from django.contrib.auth.models import Group

def is_user_group_context(request):
    if request.user.is_authenticated:
        is_user_group = request.user.groups.filter(name="User").exists()
    else:
        is_user_group = False
    return {"is_user_group": is_user_group}
