from django.http import JsonResponse, HttpResponse

class FileSizeLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "POST" and request.FILES:
            for file in request.FILES.values():
                if file.size > 1 * 1024 * 1024:  # 1 MB limit
                    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                        # Respond with JSON for AJAX requests
                        return JsonResponse(
                            {"error": "Uploaded file exceeds the size limit (1 MB)."},
                            status=400,
                        )
                    else:
                        # Return plain HTML for non-AJAX requests
                        return HttpResponse(
                            "Uploaded file exceeds the size limit (1 MB).",
                            status=400,
                        )

        return self.get_response(request)
