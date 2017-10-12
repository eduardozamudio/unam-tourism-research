from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic   import CreateView, UpdateView, DeleteView
from .models import University, Researcher, Course, Degree, PosDegree
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth    import logout
from django.forms.models import modelform_factory
from django.forms.widgets import CheckboxSelectMultiple
from django.forms import ModelMultipleChoiceField
from .forms import ResearcherForm
from rest_framework.views import APIView
from rest_framework.response import Response
import seaborn as sns

# Create your views here.
# def index(request):
#     latest_university_list = University.objects.all()
#     template = loader.get_template('condet/index.html')
#     context = {
#         'latest_university_list': latest_university_list
#     }
#     return HttpResponse(template.render(context, request))

def logout_view(request):
    context = logout(request)
    return HttpResponseRedirect(reverse_lazy('condet:index'))


class IndexView(generic.View):
    #template_name = 'condet/index.html'
    uni = University.objects.all()
    data = []

    for u in uni:
        data.append({
            'university' :u, 
            'posdegree_count' : len(u.get_posdegree_researchers())
            })

    context = {
        'data' : data,
    }
    
    def get(self, request, *args, **kwargs):

        return render(request, 'condet/index.html', self.context)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {}
        labels = []
        items =  []
        palette = []
        coordinates = []

        uni = University.objects.all()
        for u in uni:
            labels.append(u.name)
            items.append(len(u.get_posdegree_researchers()))
            coordinates.append(u.geom)

        palette = sns.color_palette('hls', len(uni)).as_hex()

        data = {
                "labels": labels,
                "items": items,
                "palette": palette,
                "coordinates": coordinates,
        }
        return Response(data)

##Researcher
class ResearcherView(generic.DetailView):
    model = Researcher

    # def get_context_data(self, **kwargs):
    #     context = super(ResearcherView, self).get_context_data(**kwargs)
    #     context['degrees'] = Researcher.degree.objects.all()

class ResearcherList(generic.ListView):
    model = Researcher

class ResearcherCreate(generic.CreateView):
    model = Researcher
    form_class = ResearcherForm
    # fields = ['first_name', 'last_name', 'category', 'degree', 'pos_degree']
    success_url = reverse_lazy('condet:researcher_list')

class ResearcherUpdate(generic.UpdateView):
    model = Researcher
    form_class = ResearcherForm
    success_url = reverse_lazy('condet:researcher_list')

class ResearcherDelete(generic.DeleteView):
    model = Degree
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('condet:researcher_list')

# def university_detail(request, university_id):
#     return HttpResponse("Universidad: %s" % university_id)


##University
class UniversityList(generic.ListView):
    model = University
    # template_name = 'condet/university_detail.html'
    # context_object_name = 'university'

class UniversityDetail(generic.DetailView):
    model = University
    fields = ['name', 'courses']

class UniversityCreate(generic.CreateView):
    model = University
    fields = ['name', 'courses']
    success_url = reverse_lazy('condet:university_list')

class UniversityUpdate(generic.UpdateView):
    model = University
    fields = ['name', 'courses']
    success_url = reverse_lazy('condet:university_list')

class UniversityDelete(generic.DeleteView):
    model = University
    fields = ['name']
    success_url = reverse_lazy('condet:university_list')


##Course
class CourseView(generic.ListView):
    template_name = 'condet/course_list.html'

    def get_queryset(self):
        return Course.objects.all()

class CourseDetail(generic.DetailView):
    model = Course


##Degree
class DegreeDetail(generic.DetailView):
    model = Degree

class DegreeList(generic.ListView):
    model = Degree

class DegreeCreate(generic.CreateView):
    model = Degree
    fields = ['name']
    success_url = reverse_lazy('condet:degree_list')

class DegreeUpdate(generic.UpdateView):
    model = Degree
    fields = ['name']
    success_url = reverse_lazy('condet:degree_list')

class DegreeDelete(generic.DeleteView):
    model = Degree
    fields = ['name']
    success_url = reverse_lazy('condet:degree_list')

##PosDegree
class PosDegreeDetail(generic.DetailView):
    model = PosDegree

class PosDegreeList(generic.ListView):
    model = PosDegree

class PosDegreeCreate(generic.CreateView):
    model = PosDegree
    fields = ['name']
    success_url = reverse_lazy('condet:posdegree_list')

class PosDegreeUpdate(generic.UpdateView):
    model = PosDegree
    fields = ['name']
    success_url = reverse_lazy('condet:posdegree_list')

class PosDegreeDelete(generic.DeleteView):
    model = PosDegree
    fields = ['name']
    success_url = reverse_lazy('condet:posdegree_list')


##Methods
def researcher_courses(request, researcher_id):
    courses = []

    researcher = Researcher.objects.get(id=researcher_id)

    for u in University.objects.all():
        # result = []
        u_courses = u.get_courses(researcher_id)

        for c in u_courses:
            courses.append(c.name)

        # courses[u.name] = ''.join(result)

    context = {'courses': courses,
               'researcher': researcher}

    return render(request, 'condet/researcher_courses.html', context)