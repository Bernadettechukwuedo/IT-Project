from django.shortcuts import render
import subprocess
import requests
from .forms import PingForm
from .models import Ping


# Create your views here.
def ping(host):
    try:
        result = subprocess.run(
            ["ping", "-n", "4", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception:
        return None


def ping_info(url_or_ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{url_or_ip}")
        data = response.json()
        if data["status"] == "fail":
            return {
                "status": data["status"],
                "message": data["message"],
                "query": data["query"],
            }
        return {
            "status": data["status"],
            "country": data["country"],
            "countryCode": data["countryCode"],
            "regionName": data["regionName"],
            "isp": data["isp"],
            "org": data["org"],
            "query": data["query"],
        }

    except requests.exceptions.RequestException:
        return None


def ping_form_view(request):
    form = PingForm()
    result = None
    ip_info = None
    if request.method == "POST":
        form = PingForm(request.POST)
        if form.is_valid():
            host = form.cleaned_data["url_or_ip"]
            result = ping(host)
            ip_info = ping_info(host)

            Ping.objects.create(url=host, status=ip_info["status"])
        else:
            ip_info = None

    return render(
        request,
        "checker/index.html/",
        {"form": form, "result": result, "ip_info": ip_info},
    )
