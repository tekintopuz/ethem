import os

from dotenv import load_dotenv

load_dotenv()

ROOT =  os.getenv("ROOT")
WS_ROOT =  os.getenv("WS_ROOT")

def global_settings(request):
    my_context = {
        'ROOT': ROOT,
        'WS_ROOT': WS_ROOT,
    }
    if "status" in request.session:
        my_context["status"] = request.session["status"]
        my_context["message"] = request.session["message"]
        del request.session["status"]
        del request.session["message"]

    return my_context
