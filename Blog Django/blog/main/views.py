from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, TemplateView
from .forms import BlogForm
from .models import Blog


class IndexView(TemplateView):
    template_name = "main/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogs = Blog.objects.all()
        context["blogs"] = blogs

        return context
    
class BlogView(FormView):
    template_name = 'main/blogform.html'
    form_class  = BlogForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. We will be in touch soon.')
        return super().form_valid(form)
    
    def create_blog(request):
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            # Guardar el blog y la imagen
            blog = form.save(commit=False)
            blog.usuario_crea = request.user  # Si quieres asignar al usuario actual
            blog.save()
            return redirect('success_url')  # Redirige a la página de éxito
        else:
            form = BlogForm()
        return render(request, 'create_blog.html', {'form': form})