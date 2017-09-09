from django.db import models
from django.urls import reverse
import pandas as pd

# Create your models here.

##Researcher
class Degree(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('degree_detail', kwargs={'pk': self.pk})

class PosDegree(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Researcher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    degree = models.ManyToManyField(Degree)
    pos_degree = models.ManyToManyField(PosDegree)

    def has_posdegree(self):
        if self.pos_degree.count() >0:
            return True
        else:
            return False

    def has_degree(self):
        if self.degree.count() >0:
            return True
        else:
            return False

    def __str__(self):
        return '{0} {1} '.format(self.first_name,self.last_name)


##Institution

class CourseTeacher(models.Model):
    researcher = models.ForeignKey(Researcher, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    position_type = models.CharField(max_length=50)



class Course(models.Model):
    name = models.CharField(max_length=200)
    researchers = models.ManyToManyField(CourseTeacher)

    def get_posdegree_teachers(self):
        pd_researchers = []

        for r in self.researchers.all():
            if r.researcher.has_posdegree():
                pd_researchers.append(r.researcher)

        return pd_researchers

    def get_degree_teachers(self):
        d_researchers = []

        for r in self.researchers.all():
            if r.researcher.has_degree():
                d_researchers.append(r.researcher)

        return d_researchers

    def has_teacher(self, researcher_id):
        '''Determine if a researcher is a teacher in this course'''
        result = False

        for r in self.researchers.all():
            if r.researcher.id == researcher_id:
                result = True
                break

        return result

    def __str__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class University(Institution):
    courses = models.ManyToManyField(Course)

    def get_posdegree_researchers(self):
        result = []

        for c in self.courses.all():

            result.append(c.get_posdegree_teachers())

        result = pd.Series(sum(result, [])).unique()

        return result

    def get_degree_researchers(self):
        result = []

        for c in self.courses.all():

            result.append(c.get_degree_teachers())

        result = pd.Series(sum(result, [])).unique()

        return result

    def get_researchers(self):
        result = []

        for c in self.courses.all():

            for t in c.researchers.all():
                result.append(t.researcher)

        result = pd.Series(result).unique()

        return result

    def get_categories(self):
        result_uni = []
        r_list = []

        for r in self.get_researchers():
            r_list.append([r.id, r.category])

        r_list = pd.DataFrame(r_list, columns=['id', 'category'])
        result_uni = r_list.groupby('category').count().transpose()
        result_uni['universidad'] = self.name

        return result_uni

    def get_teachers(self):
        result = []

        for c in self.courses.all():

            for t in c.researchers.all():
                result.append(t)

        result = pd.Series(result).unique()

        return result

    def get_positions(self):
        result_uni = []
        r_list = []

        for r in self.get_teachers():
            r_list.append([r.researcher.id, r.position, r.position_type])

        r_list = pd.DataFrame(r_list, columns=['id', 'position', 'position_type'])
        result_uni = r_list.groupby(['position', 'position_type']).count().transpose()
        result_uni['universidad'] = self.name

        return result_uni

    def get_courses(self, researcher_id):
        '''Returns courses for a given researcher id'''

        result = []

        for c in self.courses.all():
            if c.has_teacher(researcher_id):
                result.append(c)

        return result

##Proyects
class ProjectMember(models.Model):
    member = models.ForeignKey(Researcher)
    function = models.CharField(max_length=50)
    institution = models.ForeignKey(Institution)

class Project(models.Model):
    title = models.CharField(max_length=200)
    members = models.ManyToManyField(ProjectMember)
    institution = models.ManyToManyField(Institution)
    year = models.DateField("Project initialization")

    def __str__(self):
        return self.title

