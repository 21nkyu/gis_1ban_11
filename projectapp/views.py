from django.contrib.auth.decorators import login_required
# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    # success_url = reverse_lazy('articleapp:list')#디테일뷰가 없으니 임시로
    template_name = 'projectapp/create.html' #에서 시각화 할거다

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk}) #완성되면 가는 화면


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 20

    def get_context_data(self, **kwargs):  #오버라이드
        user = self.request.user  #만약 로그인 되지 않았다면 유저가 식별 되지 않음, 비회원유저
        project = self.object

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user,
                                                       project=project)   #비로그인시 이정보를 찾을 수 없다
        else:
            subscription = None

        article_list = Article.objects.filter(project=self.object) #해당프로젝트 글만 추려낸다
        return super().get_context_data(object_list=article_list,
                                        subscription=subscription,
                                        **kwargs) #글을 내보낸다


class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'

    paginate_by = 20