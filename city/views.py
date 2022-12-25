from django.http import HttpResponse
from django.template import loader
from django.views import View


class CountryView(View):
    def get(self, request):
        context = {
            'active': ["#country_li"],
            'menu_open': []}
        template = loader.get_template('police/iller.html')
        return HttpResponse(template.render(context, request))

class CityView(View):
    def get(self, request):
        context = {
            'active': ["#il_li"],
            'menu_open': ["#il_ilce_semt_mahallekoy_li"]}
        template = loader.get_template('vize/iller.html')
        return HttpResponse(template.render(context, request))


class CityDatatableView(BaseDatatableView):
    model = Il
    my_type = ""
    user = ""
    login_secret = ""
    my_search = ""

    columns = ['id', 'name', 'id']
    order_columns = ['id', 'name', 'id']
    max_display_length = 100

    def get_initial_queryset(self):

        self.my_search = self.request.GET.get('my_search') if self.request.GET.get('my_search') else \
            self.request.GET.get('search[value]')

        return Il.objects.all()

    def filter_queryset(self, qs):
        try:
            self.my_search = self.request.GET.get('my_search') if self.request.GET.get('my_search') \
                else self.request.GET.get('search[value]')

            if self.my_search and not self.my_search == "":
                q = Q(id__icontains=self.my_search) | \
                    Q(name__icontains=self.my_search)
                qs = qs.filter(q)

            return qs
        except Exception as e:
            print(str(e))
            return qs

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            json_data.append([item.id,
                              item.name,
                              "<button class ='btn btn-primary btn-block edit-il' data-pk='{0}' data-name='{1}'>"
                              "DÜZENLE</button>".format(item.id, item.name) +
                              "<button class ='btn btn-danger btn-block delete-object' data-model='İl' "
                              "data-pk='{0}'>SİL</button>".format(item.id)
                              ])
        return json_data


class CountryDatatableView(BaseDatatableView):
    model = Il
    my_type = ""
    user = ""
    login_secret = ""
    my_search = ""

    columns = ['id', 'name', 'id']
    order_columns = ['id', 'name', 'id']
    max_display_length = 100

    def get_initial_queryset(self):

        self.my_search = self.request.GET.get('my_search') if self.request.GET.get('my_search') else \
            self.request.GET.get('search[value]')

        return Il.objects.all()

    def filter_queryset(self, qs):
        try:
            self.my_search = self.request.GET.get('my_search') if self.request.GET.get('my_search') \
                else self.request.GET.get('search[value]')

            if self.my_search and not self.my_search == "":
                q = Q(id__icontains=self.my_search) | \
                    Q(name__icontains=self.my_search)
                qs = qs.filter(q)

            return qs
        except Exception as e:
            print(str(e))
            return qs

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            json_data.append([item.id,
                              item.name,
                              "<button class ='btn btn-primary btn-block edit-il' data-pk='{0}' data-name='{1}'>"
                              "DÜZENLE</button>".format(item.id, item.name) +
                              "<button class ='btn btn-danger btn-block delete-object' data-model='İl' "
                              "data-pk='{0}'>SİL</button>".format(item.id)
                              ])
        return json_data
