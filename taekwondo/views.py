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
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .forms import CoachForm
from django_filters.views import FilterView
from .filters import CoachFilter

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_message'] = "Welcome to the Taekwondo App!"
        return context

class CoachListView(FilterView):
    model = Coach
    template_name = "coaches.html"
    filterset_class = CoachFilter
    context_object_name = "Coaches"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Use the filterset's queryset to calculate if it's empty
        filter_set = context['filter']
        context['is_empty'] = not filter_set.qs.exists()
        return context

class CoachDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Coach
    context_object_name = 'Coach'

    def get_context_data(self, **kwargs):
        # Get the base context
        context = super().get_context_data(**kwargs)
        coach = self.get_object()
        user = self.request.user

        # Add logic to check if the user is the manager
        context['is_manager'] = coach.manager == user

        # Add special manager-specific context
        if context['is_manager']:
            context['show_close_button'] = True
            context['redirect_url'] = reverse('coaches-list')

        return context

    def render_to_response(self, context, **response_kwargs):
        # No access restriction for registered users
        return super().render_to_response(context, **response_kwargs)

@login_required
def search(request):
    if request.GET:
        search_term = request.GET.get('search_term', '')
        search_result = Coach.objects.filter(
            Q(full_name__icontains=search_term) |
            Q(registration_number__icontains=search_term) |
            Q(country__icontains=search_term) |
            Q(phone_number__iexact=search_term)
        )
        context = {
            'search_term': search_term,
            'Coaches': search_result
        }
        return render(request, 'search.html', context)
    else:
        return redirect('home')

class CoachCreateView(LoginRequiredMixin, CreateView):
    model = Coach
    form_class = CoachForm
    template_name = 'create.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user  # Assign the logged-in user as the manager
        instance.save()

        # Check if it's an AJAX request
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'message': 'Coach added successfully!'}, status=200)

        messages.success(self.request, 'Coach added successfully')
        return redirect('coaches-list')
    
    def form_invalid(self, form):
        # Handle AJAX requests
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'error': 'Failed to add coach.', 'errors': form.errors}, status=400)

        messages.error(self.request, "Failed to add coach. Please check the form and try again.")
        return super().form_invalid(form)

class CoachUpdateView(LoginRequiredMixin, UpdateView):
    model = Coach
    form_class = CoachForm
    template_name = 'update.html'

    def form_valid(self, form):
        instance = form.save()

        messages.success(self.request, "Coach updated successfully.")

        # Handle AJAX requests
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':

            messages_list = [
            {"tags": "success", "message": "Coach updated successfully!"}
            ]
        
            redirect_url = self.get_success_url()
            return JsonResponse({'messages': messages_list, 'redirect_url': redirect_url}, status=200)
            
        
        return super().form_valid(form)

    def form_invalid(self, form):

        # Handle AJAX requests
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'error': 'Failed to update coach.', 'errors': form.errors}, status=400)

        # Error message
        messages.error(self.request, "Failed to update coach. Please check the form.")
        return super().form_invalid(form)

    def get_success_url(self):
        # Redirect after successful update
        return reverse("detail", kwargs={"pk": self.object.pk})

class CoachDeleteView(LoginRequiredMixin, DeleteView):
    model = Coach
    success_url = '/coaches'

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Coach deleted successfully')
        return self.delete(request, *args, **kwargs)


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
    template_name = 'registration/logged_out.html'

    def get(self, request, *args, **kwargs):
        # Perform the logout operation
        logout(request)
        return super().get(request, *args, **kwargs)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            # Authenticate the user
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )
            if user is not None:
                # Log in the user
                login(request, user)
                print(f"User logged in successfully: {user.username}")  # Debug log
                
                if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                    return JsonResponse({"success": True})
                
                return redirect("coaches-list")  # Fallback for non-AJAX requests
            else:
                print("Authentication failed despite valid form.")  # Debug log

        # Handle login failure
        print("Login failed. Form errors:", form.errors)  # Debug log
        messages.error(request, "Invalid username or password.")  # 🔹 Add Django message
        errors = form.errors.get_json_data()

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"success": False, "errors": errors}, status=400)

        # Fallback: Redirect to the page with a query parameter
        return redirect(f"{request.path}?login_failed=1")

    # Invalid request handling (GET or invalid POST)
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        print("Invalid request method (non-POST) received via AJAX.")  # Debug log
        return JsonResponse({"success": False, "error": "Invalid request method."}, status=400)
    
    print("Invalid request method (non-POST) received via standard request.")  # Debug log
    return redirect("coaches-list")


@csrf_exempt
def get_csrf_token(request):
    return JsonResponse({"csrf_token": get_token(request)})

