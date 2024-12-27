from django.contrib.auth.models import Group

def is_user_group_context(request):
    if request.user.is_authenticated:
        is_user_or_staffuser_or_superuser = request.user.groups.filter(
            name__in=["User", "Staffuser", "Superuser"]
        ).exists()
        is_staffuser_or_superuser = request.user.groups.filter(
            name__in=["Staffuser", "Superuser"]
        ).exists()
    else:
        is_user_or_staffuser_or_superuser = False
        is_staffuser_or_superuser = False

    return {
        "is_user_or_staffuser": is_user_or_staffuser_or_superuser,
        "is_staffuser_or_superuser": is_staffuser_or_superuser,
    }
