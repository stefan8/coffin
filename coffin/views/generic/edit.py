from django.views.generic.edit import CreateView as _CreateView, UpdateView as _UpdateView, DeleteView as _DeleteView, FormView as _FormView
from coffin.views.decorators import template_response

__all__ = ['CreateView', 'UpdateView', 'DeleteView', 'FormView']

CreateView, UpdateView, DeleteView, FormView = map(template_response,
        (_CreateView, _UpdateView, _DeleteView, _FormView)) 

