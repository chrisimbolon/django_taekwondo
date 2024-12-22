from django.shortcuts import render, get_object_or_404,redirect
from .models import Coach
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView  
from datetime import datetime


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_message'] = "Welcome to the Taekwondo App!"
        return context


class CoachListView(LoginRequiredMixin, ListView):
    template_name = 'coaches.html'
    model = Coach
    context_object_name = 'Coaches'

    def get_queryset(self):
        Coaches = super().get_queryset()
        return Coaches

    # def get_queryset(self):
    #     Coaches = super().get_queryset()
    #     filtered = Coaches.filter(manager=self.request.user)
    #     print("Filtered Coaches:", filtered)  
    #     return filtered


class CoachDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Coach
    context_object_name = 'Coach'

@login_required
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_result = Coach.objects.filter(
                Q(Nama_Lengkap__icontains=search_term)|
                Q(Nama_Dojang__icontains=search_term)|
                Q(Status__icontains=search_term)|
                Q(No_Telp__iexact=search_term)
        )
        context={
            'search_term':search_term,
            'Coaches':search_result.filter(Manager=request.user)
        }
        return render(request, 'search.html',context)
    else:
        return redirect('home')

class CoachCreateView(LoginRequiredMixin, CreateView):
    model = Coach
    template_name = 'create.html'
    fields = [
        'registration_number', 'full_name', 'place_of_birth', 'date_of_birth', 'dojang_name',
        'sex', 'province', 'city', 'status', 'belt', 'phone_number', 'email', 'photo',
    ]

    def post(self, request, *args, **kwargs):
        # Intercept POST data to handle the date format
        post_data = request.POST.copy()
        raw_dob = post_data.get('date_of_birth')

        if raw_dob:
            try:
                # Convert DD-MM-YYYY to YYYY-MM-DD
                dob_converted = datetime.strptime(raw_dob, '%d-%m-%Y').strftime('%Y-%m-%d')
                post_data['date_of_birth'] = dob_converted
            except ValueError:
                messages.error(request, "Invalid date format. Please use DD-MM-YYYY.")
                return self.form_invalid(self.get_form())  # Return form with an error message

        # Replace the request.POST with modified data
        request.POST = post_data
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user  # Assign the logged-in user as the manager
        instance.save()
        messages.success(self.request, 'Coach data added successfully')
        return redirect('coaches-list')

class CoachUpdateView(LoginRequiredMixin, UpdateView):
    model = Coach
    template_name = 'update.html'
    fields = ['No_Reg','Nama_Lengkap','Tempat_Lahir','Tanggal_Lahir','Nama_Dojang',
            'Jenis_Kelamin','Provinsi_Asal','Kota_Asal','Status','Sabuk_Akhir','No_Telp',
            'Email','Photo',]

    def form_valid(self,form):
        instance = form.save()
        messages.success(self.request,'Data Coach berhasil diupdate')
        return redirect('detail',instance.pk)

class CoachDeleteView(LoginRequiredMixin, DeleteView):
    model = Coach
    template_name = 'delete.html'
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,'Data Coach berhasil dihapus')
        return super().delete(self, request, *args, **kwargs)

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
