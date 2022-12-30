from django.utils import timezone

now = timezone.now().year


def year(request):
    now = timezone.now().year
    return {'year': now}
