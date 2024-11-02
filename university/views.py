from django.shortcuts import get_object_or_404
from django.views import generic
from university.forms import StudentForm
from university.models import Student


class StudentListView(generic.ListView):
    template_name = "students/students.html"
    context_object_name = "students"
    model = Student

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


class StudentDetailView(generic.DetailView):
    template_name = "students/student_info.html"
    context_object_name = "student"

    def get_object(self, **kwargs):
        student_id = self.kwargs.get("id")
        return get_object_or_404(Student, id=student_id)


class CreateStudentView(generic.CreateView):
    template_name = "students/add_student.html"
    form_class = StudentForm
    success_url = '/students/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateStudentView, self).form_valid(form=form)


class DeleteStudentView(generic.DeleteView):
    template_name = "students/remove_student.html"
    success_url = '/students/'

    def get_object(self, **kwargs):
        student_id = self.kwargs.get("id")
        return get_object_or_404(Student, id=student_id)


class EditStudentView(generic.UpdateView):
    template_name = "students/edit_student.html"
    form_class = StudentForm
    success_url = '/students/'

    def get_object(self, **kwargs):
        student_id = self.kwargs.get("id")
        return get_object_or_404(Student, id=student_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditStudentView, self).form_valid(form=form)


class SearchStudentView(generic.ListView):
    template_name = "students/students.html"
    context_object_name = "students"
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Student.objects.filter(student_id__icontains=query).order_by('student_id')
        return Student.objects.all().order_by('student_id')





