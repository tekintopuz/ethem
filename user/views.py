import json
import pprint

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.template import loader
from django.views import View
from django_datatables_view.base_datatable_view import BaseDatatableView

from citizen.models import Citizen
from city.models import City
from criminal.models import CriminalRecord
from police.models import PoliceOfficer, PoliceStation
from user.context_processors import ROOT
from user.models import User
from utils.util import get_next_id


def handler401(request, template_name='police/401.html'):
    context = {}
    if "status" in request.session:
        context["status"] = request.session["status"]
        del request.session["status"]
    if "message" in request.session:
        context["message"] = request.session["message"]
        del request.session["message"]
    template = loader.get_template(template_name)
    return HttpResponse(template.render(context, request))


def handler403(request, template_name='police/403.html'):
    context = {}
    if "status" in request.session:
        context["status"] = request.session["status"]
        del request.session["status"]
    if "message" in request.session:
        context["message"] = request.session["message"]
        del request.session["message"]
    template = loader.get_template(template_name)
    return HttpResponse(template.render(context, request))


def handler404(request, template_name='police/404.html'):
    context = {}
    if "status" in request.session:
        context["status"] = request.session["status"]
        del request.session["status"]
    if "message" in request.session:
        context["message"] = request.session["message"]
        del request.session["message"]
    template = loader.get_template(template_name)
    return HttpResponse(template.render(context, request))


def handler500(request, template_name='police/500.html'):
    context = {}
    if "status" in request.session:
        context["status"] = request.session["status"]
        del request.session["status"]
    if "message" in request.session:
        context["message"] = request.session["message"]
        del request.session["message"]
    template = loader.get_template(template_name)
    return HttpResponse(template.render(context, request))


def handler501(request, template_name='police/501.html'):
    context = {}
    if "status" in request.session:
        context["status"] = request.session["status"]
        del request.session["status"]
    if "message" in request.session:
        context["message"] = request.session["message"]
        del request.session["message"]

    template = loader.get_template(template_name)
    return HttpResponse(template.render(context, request))


def server_error(request, error_code):
    context = {}
    if "status" in request.session:
        context["status"] = request.session["status"]
        del request.session["status"]
    if "message" in request.session:
        context["message"] = request.session["message"]
        del request.session["message"]

    template = loader.get_template("police/" + str(error_code) + ".html")
    return HttpResponse(template.render(context, request))


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'active': ['#home_li'],
            'menu_open': [],
            'my_orders': True

        }
        template = loader.get_template('police/index.html')
        return HttpResponse(template.render(context, request))


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/")
        else:
            context = {
                'active': [],
                'menu_open': []}
            template = loader.get_template('police/login.html')
            return HttpResponse(template.render(context, request))

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            request.session["status"] = "success"
            request.session["message"] = "Sisteme başarı ile giriş yapıldı."

            if "next" in request.GET:
                return redirect(self.request.GET.get('next'))
            return redirect("/")
        else:
            context = {
                'active': [],
                'menu_open': [],
                'status': 'error',
                'message': "wrong username or password"}
            template = loader.get_template('police/login.html')
            return HttpResponse(template.render(context, request))


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/")
        else:
            context = {
                'active': [],
                'menu_open': []}
            template = loader.get_template('police/register.html')
            return HttpResponse(template.render(context, request))

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        company = request.POST['company']
        email = request.POST['email']
        department = request.POST['department']
        door = request.POST['door']
        address = request.POST['address']
        password = request.POST['password']
        re_password = request.POST['password']

        if password != re_password:
            context = {
                'status': "error",
                'message': "Şifre ve şifre tekrarı uyuşmuyor"
            }
            template = loader.get_template('police/register.html')
            return HttpResponse(template.render(context, request))

        user, created = User.objects.get_or_create(email=email, username=email)
        if created:
            user.first_name = first_name
            user.last_name = last_name
            user.company = company
            user.department = department
            user.door = door
            user.address = address
            user.set_password(password)
            user.is_active = True
            user.save()

            return redirect("/login")

        else:
            context = {
                'status': "error",
                'message': "Bu eposta zaten kayıtlı."
            }
            template = loader.get_template('police/register.html')
            return HttpResponse(template.render(context, request))


class LogoutView(View):
    def get(self, request):
        if request.method == 'GET' and request.user.is_authenticated:
            logout(request)
        return HttpResponseRedirect('/login')


class MyProfileView(LoginRequiredMixin, View):
    def get(self, request):
        context = {"open_menu": [],
                   "active": ["#profile_li"]}

        try:
            template = loader.get_template('police/member_profile.html')
            return HttpResponse(template.render(context, request))

        except Exception as e:
            context["status"] = "error"
            context["message"] = str(e)
            template = loader.get_template('police/../templates/404.html')
            return HttpResponse(template.render(context, request))

    def post(self, request):
        try:
            user = request.user
            if "form-type" in request.POST and request.POST.get("form-type") == "profile-form":

                user.first_name = request.POST.get("first_name")
                user.last_name = request.POST.get("last_name")
                new_email = request.POST.get("email")
                if "@" in new_email and not User.objects.filter(email=new_email).exists():
                    user.email = request.POST.get("email")
                else:
                    request.session["message"] = "Email değiştirilemedi. Bu eposta zaten kayıtlı."

                user.tckn = request.POST.get("tckn") if "tckn" in request.POST else ""
                user.pasaport_no = request.POST.get("pasaport_no") if "pasaport_no" in request.POST else ""
                user.vergi_no = request.POST.get("vergi_no") if "vergi_no" in request.POST else ""
                user.city = City.objects.filter(
                    id=int(request.POST.get("city"))).first() if "city" in request.POST else None

                user.address = request.POST.get("address") if "address" in request.POST else ""
                user.postcode = request.POST.get("postcode") if "postcode" in request.POST else ""

                user.second_name = request.POST.get("second_name") if "second_name" in request.POST else ""
                user.phone = request.POST.get("phone") if "phone" in request.POST else ""
                user.phone2 = request.POST.get("phone2") if "phone2" in request.POST else ""
                user.mobile_phone = request.POST.get("mobile_phone") if "mobile_phone" in request.POST else ""
                user.dahili = request.POST.get("dahili") if "dahili" in request.POST else ""
                user.marital_status = request.POST.get("marital_status") if "marital_status" in request.POST else ""
                user.bio = request.POST.get("bio") if "bio" in request.POST else ""
                user.academic = request.POST.get("academic") if "academic" in request.POST else ""

                if "avatar" in request.FILES:
                    user.avatar = request.FILES["avatar"]

                request.session["status"] = "success"
                request.session["message"] += "Profil Başarı İle Güncellendi"

            elif "form-type" in request.POST and request.POST.get("form-type") == "password-form":

                password = request.POST.get("password")
                new_password = request.POST.get("new_password")
                new_password2 = request.POST.get("new_password2")

                if user.check_password(password) and new_password == new_password2:
                    user.set_password(new_password)
                    user.raw_pwd = new_password

                    request.session["status"] = "success"
                    request.session["message"] = "Şifre Başarı İle Değiştirildi."

            else:
                request.session["status"] = "error"
                request.session["message"] = "Form-type bulunamadı"

            user.save()
            user.save()
        except Exception as e:
            request.session["status"] = "error"
            request.session["message"] = "Bir hata oluştu. Code => " + str(e)

        return redirect("/profile/")


class AllUsersView(LoginRequiredMixin, View):
    def get(self, request):
        context = {"open_menu": [],
                   "active": ["#all_users_li"], }

        try:
            if request.user.is_superuser:
                template = loader.get_template('users/all_users.html')
                return HttpResponse(template.render(context, request))

            else:
                return HttpResponseRedirect('/401')
        except Exception as e:
            request.session['status'] = "error"
            request.session['message'] = "Bir Hata Oluştu ==>" + str(e)
            return HttpResponseRedirect('/500')


class AllUsersDatatableView(LoginRequiredMixin, BaseDatatableView):
    model = User

    columns = ['id', 'avatar', 'first_name', 'second_name', 'last_name', 'email', 'phone', 'mobile_phone', 'id']
    order_columns = ['id', 'avatar', 'first_name', 'second_name', 'last_name', 'email', 'phone', 'mobile_phone', 'id']
    max_display_length = 100
    uid = None
    login_secret = None
    user = None

    def get_initial_queryset(self):

        if self.request.user and self.request.user and self.request.user.is_superuser:
            return User.objects.filter(is_active=True).order_by("-id")
        else:
            return User.objects.filter(id__lte=0)

    def filter_queryset(self, qs):
        try:
            search = self.request.GET.get('search[value]', None)
            q = Q(id__icontains=search) | \
                Q(first_name__icontains=search) | \
                Q(last_name__icontains=search) | \
                Q(email__icontains=search) | \
                Q(phone__icontain=search) | \
                Q(mobile_phone__icontains=search) | \
                Q(dahili__icontains=search)
            qs = qs.filter(q)
            return qs

        except Exception as e:
            print(str(e))
            return qs

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            gruplar = ""
            for g in item.groups.all():
                gruplar += g.name + " | "

            json_data.append([
                "<a href='/kullanici-duzenle/" + str(item.id) + "'>" + str(item.id) + "</a>",
                "<img style='width:60px' class='image popup-image' src='" +
                (item.avatar.url if item.avatar else "/media/no-image.png") + "'/>",
                item.first_name,
                item.second_name,
                item.last_name,
                "<a href='/kullanici-duzenle/" + str(item.id) + "'>" + str(item.email) + "</a>",
                item.phone,
                item.mobile_phone,
                item.dahili,
                gruplar,
                "<a href='/kullanici-duzenle/" + str(item.id) +
                "' class='btn btn-success btn-block' style='margin:1px'>Detay</a>"
                "<button class='btn btn-danger btn-block delete' style='margin:1px' data-pk='" +
                str(item.id) + "' data-model='User'>SİL</button>",
            ])
        return json_data


class DeleteObjectView(LoginRequiredMixin, View):
    def post(self, request):
        if request.user.is_superuser:
            data = json.loads(request.body)
            pprint.pprint(request.POST)
            model = data["model"]
            rows_selected = data["pk"]
            status = "success"
            if "all" in rows_selected:
                rows_selected = "all"

            if model == 'User':
                model = User
            elif model == 'City':
                model = City
            else:
                model = None

            if model:
                items = model.objects.filter(pk__in=rows_selected) if rows_selected != "all" else model.objects.all()
                if len(items) > 0:
                    message = str(rows_selected) + " nolu " + model.__name__ + " başarı ile silindi."
                    for item in items:
                        item.delete()
                else:
                    status = "error"
                    message = "İlgili nesne bulunamadı. Silme işlemi başarısız"
            else:
                status = "error"
                message = "İlgili nesne bulunamadı. Silme işlemi başarısız"

            return JsonResponse({
                "status": status,
                "message": message
            })


class GetNecessaryDataView(LoginRequiredMixin, View):
    def get(self, request):
        context = {}
        user = request.user

        context[".first_name"] = user.first_name
        context[".last_name"] = user.last_name
        if user.is_superuser or user.groups.filter(name="Production").exists():

            context[".status"] = "success"
            context[".number_of_users"] = User.objects.all().count()
            context[".number_of_citizens"] = Citizen.objects.all().count()
            context[".number_of_criminalrecords"] = CriminalRecord.objects.all().count()
            context[".number_of_policeofficers"] = PoliceOfficer.objects.all().count()
            context[".number_of_policestations"] = PoliceStation.objects.all().count()

        else:
            pass

        return JsonResponse(context)


class MusteriView(LoginRequiredMixin, View):
    def get(self, request, musteri_id=0):
        if musteri_id not in ["0", 0]:
            context = {"menu_open": ["#musteriler_ul"],
                       "active": ["#musteri_duzenle_li", "#profile_link", "#profile_tab"]
                       }
            musteri = User.objects.filter(id=musteri_id).first()
        else:
            context = {"menu_open": ["#musteriler_ul"],
                       "active": ["#yeni_musteri_li"]
                       }
            musteri = None

        context["musteri"] = musteri

        template = loader.get_template('police/profile.html')
        return HttpResponse(template.render(context, request))

    def post(self, request, musteri_id=0):
        email = request.POST.get("email")
        if musteri_id in [0, '0']:
            if User.objects.filter(email=email).exists():
                return JsonResponse({
                    "status": "error",
                    "message": "Bu eposta zaten farklı bir kullanıcı tarafından kullnılmaktadır."
                })

            user = User.objects.create(id=get_next_id(User),
                                       email=email,
                                       tckn=request.POST.get("tckn"),
                                       vergi_no=request.POST.get("vergi_no"),
                                       post_code=request.POST.get("post_code"),
                                       first_name=request.POST.get("first_name"),
                                       last_name=request.POST.get("last_name"),
                                       company=request.POST.get("company"),
                                       department=request.POST.get("department"),
                                       door=request.POST.get("door"),
                                       address=request.POST.get("address"),
                                       phone=request.POST.get("phone"),
                                       raw_pwd=request.POST.get("password"),
                                       )
            user.set_password(request.POST.get("password"))

        elif request.user.is_superuser or request.user.pk == musteri_id:
            user = User.objects.get(pk=musteri_id)
            if "@" in email and not (User.objects.filter(email=email).exists() and user.email != email):
                user.email = email
                user.username = email
            else:
                return JsonResponse({
                    "status": "error",
                    "message": "Bu eposta zaten farklı bir kullanıcı tarafından kullnılmaktadır."
                })

            user.tckn = request.POST.get("tckn")
            user.vergi_no = request.POST.get("vergi_no")
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.company = request.POST.get("company")
            user.department = request.POST.get("department")
            user.door = request.POST.get("door")
            user.address = request.POST.get("address")
            user.post_code = request.POST.get("post_code")
            user.phone = request.POST.get("phone")
            user.raw_pwd = request.POST.get("password")

            user.save()
            return JsonResponse({
                "status": "success",
                "message": "Profil başarı ile güncellendi"
            })
        else:
            return JsonResponse({
                "status": "error",
                "message": "Yetkisiz işlem"
            })


class SetPassword(LoginRequiredMixin, View):
    def post(self, request, musteri_id=0):
        new_password = request.POST.get("new_password")

        if musteri_id in [0, '0']:
            request.user.set_password(new_password)
            request.user.save()
            return JsonResponse({
                "status": "success",
                "message": "Şifreniz başarı ile değiştirildi."
            })

        elif request.user.is_superuser:
            musteri = User.objects.get(id=musteri_id)
            musteri.set_password(new_password)
            musteri.save()
            return JsonResponse({
                "status": "success",
                "message": musteri.email + " kullanıcısının şifresi başarı ile değiştirldi."
            })


class TumMusterilerView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'active': ['#tum-musteriler', "#musteriler"],
            'menu_open': ["#musteriler"]
        }
        template = loader.get_template('police/tum_musteriler.html')
        return HttpResponse(template.render(context, request))


class TumMusterilereDatatableView(LoginRequiredMixin, BaseDatatableView):
    model = User

    columns = ['id', 'email', 'name', 'company', 'lastOrderDate', 'totalOrders', 'totalProducts', 'id']
    order_columns = ['id', 'email', 'name', 'company', 'lastOrderDate', 'totalOrders', 'totalProducts', 'id']
    max_display_length = 100

    my_search = None
    order_id = None

    def get_initial_queryset(self):
        return self.model.objects.all()

    def filter_queryset(self, qs):
        try:
            self.my_search = self.request.GET.get('my_search') if self.request.GET.get('my_search') \
                else self.request.GET.get('search[value]')

            if self.my_search and not self.my_search == "":
                qs = qs.filter(Q(name=self.my_search) | Q(company=self.my_search))
            return qs

        except Exception as e:
            print(str(e))
            return qs

    def prepare_results(self, qs):
        json_data = []

        for musteri in qs:
            json_data.append([
                musteri.pk,
                musteri.email,
                musteri.get_full_name(),
                musteri.company,
                musteri.lastOrderDate,
                musteri.totalOrders,
                musteri.totalProducts,
                "<a class ='btn btn-primary btn-block' href='{0}/musteri/{1}'>DETAY</a>"
                "<button class ='btn btn-danger btn-block delete-object' data-model='Users' "
                "data-pk='{0}'>SİL</button>".format(ROOT, musteri.id)
            ])
        return json_data
