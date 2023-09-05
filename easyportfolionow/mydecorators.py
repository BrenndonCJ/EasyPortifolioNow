from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin

# Decorator para views baseadas em classes
class LogoutRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""
    def __init__(self, procfile_url) -> None:
        self.procfile_url = procfile_url

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.procfile_url)
        return super().dispatch(request, *args, **kwargs)