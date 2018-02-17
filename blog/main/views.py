from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User


class HomeView(TemplateView):
    template_name = 'index.html'


class PostRelatedViewMixin(object):
    def get_context_data(self, **kwargs):
        ctx = super(PostRelatedViewMixin, self).get_context_data(**kwargs)
        ctx['concrete_model'] = self.model
        return ctx

class Authors(ListView):
    template_name = 'authors.html'
    model = User
    queryset = User.objects.all()