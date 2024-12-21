from django.shortcuts import render, get_object_or_404,redirect
from .models import Pelatih
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView  



class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_message'] = "Welcome to the Taekwondo App!"
        return context


class PelatihListView(LoginRequiredMixin, ListView):
    template_name = 'coaches.html'
    model = Pelatih
    context_object_name = 'Pelatihs'

    def get_queryset(self):
        Pelatihs = super().get_queryset()
        filtered = Pelatihs.filter(Manager=self.request.user)
        print("Filtered Pelatihs:", filtered)  # Debug output
        return filtered

    # def get_queryset(self):
    #     Pelatihs = super().get_queryset()
    #     return Pelatihs.filter(Manager = self.request.user)




class PelatihDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Pelatih
    context_object_name = 'Pelatih'

@login_required
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_result = Pelatih.objects.filter(
                Q(Nama_Lengkap__icontains=search_term)|
                Q(Nama_Dojang__icontains=search_term)|
                Q(Status__icontains=search_term)|
                Q(No_Telp__iexact=search_term)
        )
        context={
            'search_term':search_term,
            'Pelatihs':search_result.filter(Manager=request.user)
        }
        return render(request, 'search.html',context)
    else:
        return redirect('home')

class PelatihCreateView(LoginRequiredMixin, CreateView):
    model = Pelatih
    template_name = 'create.html'
    fields = ['No_Reg','Nama_Lengkap','Tempat_Lahir','Tanggal_Lahir','Nama_Dojang',
            'Jenis_Kelamin','Provinsi_Asal','Kota_Asal','Status','Sabuk_Akhir','No_Telp',
                'Email','Photo',]

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.Manager = self.request.user
        instance.save()
        messages.success(self.request,'Data Pelatih berhasil ditambah')
        return redirect('home')


class PelatihUpdateView(LoginRequiredMixin, UpdateView):
    model = Pelatih
    template_name = 'update.html'
    fields = ['No_Reg','Nama_Lengkap','Tempat_Lahir','Tanggal_Lahir','Nama_Dojang',
            'Jenis_Kelamin','Provinsi_Asal','Kota_Asal','Status','Sabuk_Akhir','No_Telp',
            'Email','Photo',]

    def form_valid(self,form):
        instance = form.save()
        messages.success(self.request,'Data Pelatih berhasil diupdate')
        return redirect('detail',instance.pk)

class PelatihDeleteView(LoginRequiredMixin, DeleteView):
    model = Pelatih
    template_name = 'delete.html'
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,'Data Pelatih berhasil dihapus')
        return super().delete(self, request, *args, **kwargs)

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
