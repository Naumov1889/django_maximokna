from .utils import memoize
from gallery.models import PhotoCategory
from callback.forms import CallbackForm
from socials.models import Social


def photo_categories(request):
    return {
       "photoCategories": memoize(
           lambda: PhotoCategory.objects.all()
       )
    }

def callback(request):
    return {
        "callback_form": CallbackForm
    }


def social_icons(request):
    return {
        "socials": Social.objects.all
    }
