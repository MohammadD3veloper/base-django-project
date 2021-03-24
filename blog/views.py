from django.shortcuts import render
from django.views import generic
from .models import Post,Page
from django.db.models.query import Q
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    last_3_posts = Post.objects.order_by("-id")[:3]
    return render(request, "index.html", {"last_posts":last_3_posts})

class ListPostsView(generic.ListView):
    model = Post
    queryset = Post.objects.order_by("-id")
    paginate_by = 9
    template_name = "posts.html"
    context_object_name = "posts"

class DetailPostView(generic.DetailView):
    model = Post
    queryset = Post.objects.order_by("-id")
    template_name = "detail.html"
    slug_field = "slug"
    context_object_name = "post"

class SearchListView(generic.ListView):
	template_name = 'search.html'
	model = Post

	def get_queryset(self, *args, **kwargs):
		query = super(SearchListView, self).get_queryset(*args, **kwargs)
		search_query = self.request.GET.get('q')
		if search_query:
			query = Post.objects.filter(
				Q(name__icontains=search_query)|
				Q(text__icontains=search_query)|
				Q(author__first_name__icontains=search_query)|
				Q(author__last_name__icontains=search_query) |
                Q(category__name__icontains=search_query) |
                Q(subcategory__name__icontains=search_query)
				).order_by('-id').distinct()

		return query

class SearchListView(generic.ListView):
    template_name = "search.html"
    context_object_name = "result"
    model = Post
    paginate_by = 9

    def get_queryset(self, *args , **kwargs):
        query = super(SearchListView, self).get_queryset(*args, **kwargs)
        search_query = self.request.GET.get("q")
        if search_query:
            query = Post.objects.filter(
				Q(name__icontains=search_query)|
				Q(text__icontains=search_query)|
				Q(author__first_name__icontains=search_query)|
				Q(author__last_name__icontains=search_query) |
                Q(category__name__icontains=search_query) |
                Q(subcategory__name__icontains=search_query)
				).order_by('-id').distinct()
            return query

@login_required
def dashboardview(request):
    return render(request,"dashboard.html",{"user":request.user.username})

def aboutus(request):
    page = Page.objects.get(title="aboutus")
    return render(request, "aboutus.html", {"aboutus":page.text})

def contactus(request):
    page = Page.objects.get(title="contactus")
    return render(request, "contactus.html", {"contactus":page.text})