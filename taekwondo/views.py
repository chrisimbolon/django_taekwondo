from django.shortcuts import render, get_object_or_404,redirect
from .models import Coach, City, Province
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic import TemplateView  
from datetime import datetime
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import authenticate, login
from urllib.parse import urlparse
from .forms import CoachForm


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_message'] = "Welcome to the Taekwondo App!"
        return context


class CoachListView(ListView):
    template_name = 'coaches.html'
    model = Coach
    context_object_name = 'Coaches'

    def get_queryset(self):
        return super().get_queryset()

class CoachDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Coach
    context_object_name = 'Coach'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        coach = self.get_object()  
        # Check if the logged-in user is not the manager
        context['access_denied'] = self.request.user != coach.manager

        # Add the show_close_button and redirect_url to the context
        if not context['access_denied']:
            context['show_close_button'] = True
            context['redirect_url'] = reverse('coaches-list')
        return context

    def render_to_response(self, context, **response_kwargs):
        # Render access denied message if user is not the manager
        if context.get('access_denied'):
            return render(self.request, 'detail.html', context)
        return super().render_to_response(context, **response_kwargs)

@login_required
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_result = Coach.objects.filter(
                Q(full_name__icontains=search_term)|
                Q(dojang_name__icontains=search_term)|
                Q(status__icontains=search_term)|
                Q(phone_number__iexact=search_term)
        )
        context={
            'search_term':search_term,
            'Coaches':search_result.filter(manager=request.user)
        }
        return render(request, 'search.html',context)
    else:
        return redirect('home')

class CoachCreateView(LoginRequiredMixin, CreateView):
    model = Coach
    form_class = CoachForm
    template_name = 'create.html'
  
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
        messages.success(self.request, 'Coach added successfully')
        return redirect('coaches-list')

class CoachUpdateView(LoginRequiredMixin, UpdateView):
    model = Coach
    form_class = CoachForm
    template_name = 'update.html'

    def get_form_kwargs(self):
        """
        Override this method to bind the form to the existing instance.
        """
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()  # Explicitly bind the form to the instance
        return kwargs

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
        """
        Save the instance and add a success message.
        """
        instance = form.save()
        messages.success(self.request, 'Coach updated successfully')
        return redirect('detail', instance.pk)

    def form_invalid(self, form):
        """
        Handle invalid form submission with error feedback.
        """
        messages.error(self.request, "Failed to update coach. Please check the form and try again.")
        return super().form_invalid(form)

class CoachDeleteView(LoginRequiredMixin, DeleteView):
    model = Coach
    template_name = 'delete.html'
    success_url = '/coaches'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,'Coach deleted successfully')
        return super().delete(self, request, *args, **kwargs)

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')


def filter_provinces(request):
    country_code = request.GET.get("country_code")
    provinces = Province.objects.filter(country=country_code).values("id", "province_name")
    return JsonResponse(list(provinces), safe=False)

def filter_cities(request):
    province_id = request.GET.get('province_id')
    if province_id:
        cities = City.objects.filter(province_id=province_id).values('id', 'city_name')
        return JsonResponse(list(cities), safe=False)
    return JsonResponse([], safe=False)

def create_coach(request):
    provinces = Province.objects.all()
    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = CoachForm()
    return render(request, 'create.html', {'form': form, 'provinces': provinces})


class LoggedOutView(TemplateView):
    template_name = 'logged_out.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthenticationForm()
        return context


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )
            if user is not None:
                login(request, user)
                if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                    return JsonResponse({"success": True})
                return redirect("coaches-list")  # Fallback for non-AJAX requests

        # Handle login failure
        errors = form.errors.get_json_data()

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"success": False, "errors": errors}, status=400)

        # Fallback: Redirect to the page with a query parameter
        return redirect(f"{request.path}?login_failed=1")

    # Invalid request handling (GET or invalid POST)
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse({"success": False, "error": "Invalid request method."}, status=400)
    return redirect("coaches-list")
