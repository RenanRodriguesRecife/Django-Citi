from django.views import generic
from .models import Category, Course

# Create your views here.

class IndexView(generic.ListView):
	template_name = "catalog/index.html"
	context_object_name = "all_course"

	def get_queryset(self):
		return Course.objects.highlined()

class DetailView(generic.DetailView):
	model = Course
	template_name = "catalog/detail.html"

def category(request, slug):
	category = get_object_or_404(Category,slug=slug)
	context = {
		'category': category,
		'course':Couse.objects.filter(category=category)

	}
	return render(request,'catalog/category.html',context)