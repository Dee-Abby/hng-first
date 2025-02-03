from django.http import JsonResponse
from datetime import datetime

def basic_info_view(request):
    response_data = {
        "email": "adisahabeebulah@gmail.com",  # Replace with your HNG12 Slack registered email
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/Dee-Abby/hng-first.git"  # Replace with your actual GitHub repo URL
    }
    return JsonResponse(response_data, status=200)
