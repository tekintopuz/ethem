from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views import View
from django_datatables_view.base_datatable_view import BaseDatatableView

from police.models import PoliceOfficer
from user.context_processors import ROOT


class PoliceOfficerView(LoginRequiredMixin, View):
    def get(self, request, citizen_id=0):
        if citizen_id not in ["0", 0]:
            context = {"menu_open": ["#citizens_ul"],
                       "active": ["#citizens_li", ]
                       }
            musteri = PoliceOfficer.objects.filter(id=citizen_id).first()
        else:
            context = {"menu_open": ["#citizens_ul"],
                       "active": ["#yeni_musteri_li"]
                       }
            musteri = None

        context["musteri"] = musteri

        template = loader.get_template('police/policeofficer.html')
        return HttpResponse(template.render(context, request))

    def post(self, request, citizen_id=0):
        email = request.POST.get("email")
        if citizen_id in [0, '0']:
            if PoliceOfficer.objects.filter(email=email).exists():
                return JsonResponse({
                    "status": "error",
                    "message": "Bu eposta zaten farklı bir kullanıcı tarafından kullnılmaktadır."
                })

            user = PoliceOfficer.objects.create(email=email,
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
                                          raw_pwd=request.POST.get("password")
                                          )


        elif request.user.is_superuser or request.user.pk == citizen_id:
            user = PoliceOfficer.objects.get(pk=citizen_id)
            if "@" in email and not (PoliceOfficer.objects.filter(email=email).exists() and user.email != email):
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


class AllPoliceOfficersView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'active': ["#citizens_li"],
            'menu_open': []
        }
        template = loader.get_template('police/all_policeofficers.html')
        return HttpResponse(template.render(context, request))


class AlLPoliceOfficersDatatableView(LoginRequiredMixin, BaseDatatableView):
    model = PoliceOfficer

    columns = ['id', 'rank', 'tenure', 'id']
    order_columns = ['id' ,'rank', 'tenure', 'id']
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

        for item in qs:
            json_data.append([
                item.pk,
                item.rank,
                item.tenure,
                "<a class ='btn btn-primary btn-block' href='{0}/police-officers/{1}'>EDIT</a>"
                "<button class ='btn btn-danger btn-block delete-object' data-model='PoliceOfficer' "
                "data-pk='{0}'>SİL</button>".format(ROOT, item.id)
            ])
        return json_data



