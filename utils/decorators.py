from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object): 
    @classmethod
    def as_view(self, **initkwargs):
        view = super(LoginRequiredMixin, self).as_view(**initkwargs)
        return login_required(view)