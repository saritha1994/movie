from django.shortcuts import render,redirect
from app1.models import Movie
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
# def home(request):
#     m=Movie.objects.all()
#     context={'movie': m}
#
#     return render(request,'home.html',context)
class HomeView(ListView):
    model = Movie
    context_object_name = "movie"
    template_name = "home.html"

    def get_queryset(self):
        queryset=super().get_queryset().filter(title__startswith='k')
        return queryset

from app1.forms import Movie_form
# def add(request):
    # if (request.method == "POST"):
    #     t = request.POST['t']
    #     d = request.POST['d']
    #     la = request.POST['l']
    #     y = request.POST['y']
    #     i = request.FILES['i']
    #     b = Movie.objects.create(title=t, description=d, language=la, year=y, image=i)  # used instead of insert into
    #     b.save()
    #     return home(request)
    # if(request.method=="POST"):
    #     form=Movie_form(request.POST)
    #     if(form.is_valid()):
    #         form.save()
    #         return redirect('home')
    # form = Movie_form()
    # context={'form':form}
    # return render(request,'addmovie1.html',context)

class AddMovie(CreateView):
    model = Movie
    form_class = Movie_form
    template_name = "addmovie1.html"
    success_url = reverse_lazy('home')

# def detail(request,p):
#     m = Movie.objects.get(id=p)
#     context={'movie':m}
#     return render(request, 'detail.html',context)

class MovieDetail(DetailView):
    model = Movie
    context_object_name = "movie"
    template_name = "detail.html"

# def delete(request,p):
#     k = Movie.objects.get(id=p)
#     k.delete()
#     return redirect('home')
class MovieDelete(DeleteView):
    template_name = 'delete.html'
    model = Movie
    success_url = reverse_lazy('home')

# def edit(request,p):
#     k = Movie.objects.get(id=p)
#     if (request.method == "POST"):
#         k.title = request.POST['t']
#         k.description = request.POST['d']
#         k.language = request.POST['l']
#         k.year = request.POST['y']
#
#         if (request.FILES.get('i') == None):
#             k.save()
#         else:
#             k.image = request.FILES.get('i')
#
#         k.save()
#         return redirect('detail',p)
#     context = {'movie': k}
#
#     return render(request,'edit.html',context)
class MovieUpdate(UpdateView):
    model = Movie
    form_class = Movie_form
    template_name = "edit1.html"
    success_url = reverse_lazy('home')
