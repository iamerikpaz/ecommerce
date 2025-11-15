from django.shortcuts import reverse, redirect
from django.conf import settings

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        if not settings.MAINTENANCE_MODE:
            return self.get_response(request)

        if path == reverse('maintenance'):
            return self.get_response(request)

        # Permitir acceso si es admin o staff
        if request.user.is_authenticated and (request.user.is_superadmin or request.user.is_staff):
            return self.get_response(request)

        # Permitir acceso directo a securelogin sin usar reverse
        if path.startswith('/securelogin'):
            return self.get_response(request)

        return redirect('maintenance')

"""     def __call__(self, request):
        
        path = request.META.get('PATH_INFO', "")

        if settings.MAINTENANCE_MODE and path!= reverse("maintenance"):
            response = redirect(reverse("maintenance"))
            return response

        response = self.get_response(request)

        return response  """