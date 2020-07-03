from django.shortcuts import render
from .models import Banner, PortfolioCategory, Advantage, FirstScreenImg

def home(request):
    context = {
        "banners": Banner.objects.all(),
        "first_screen_img": FirstScreenImg.objects.all().first(),
        "black_burger": FirstScreenImg.objects.all().first().isDark,
        "photoCategories": PortfolioCategory.objects.all(),
        "advantages": Advantage.objects.all()
    }
    return render(request, "base/index.html", context)


def policy_page(request):
    return render(request, 'base/policy.html', {"black_burger": True})


def plastikovye_okna(request):
    return render(request, "base/plastikovye-okna.html", {"black_burger": True})
