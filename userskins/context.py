from userskins.models import SkinPreference
from django.conf import settings


def userskins(request):
    skin = settings.USERSKINS_DEFAULT
    if request.COOKIES.has_key("userskins") and request.COOKIES["userskins"] in settings.USERSKINS_DETAILS:
        skin = request.COOKIES["userskins"]
    if getattr(settings,"USERSKINS_USE_COMPRESS_GROUPS",False):
        return {"userskins_skin": skin, "userskins_use_compress":True }
    else:
        skin_uri = u"%s%s" % (settings.STATIC_URL, settings.USERSKINS_DETAILS[skin])
        return {"userskins_current_skin_name": skin, "userskins_skin": skin_uri, "userskins_use_compress":False }
