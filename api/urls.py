from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from api import views

# override docstring for API Root
class Router(DefaultRouter):
    def get_api_root_view(self, api_urls=None):
        root_view = super(Router, self).get_api_root_view(api_urls=api_urls)
        root_view.cls.__doc__ = "API Root View\n" + \
                                "Provides Entry Point information for " + \
                                "other API calls"
        return root_view

# Schema import

schema_view = get_schema_view(title='Pastebin API')

# create a router and register our viewsets with it
router = Router()
router.register(r'polities', views.PolityViewSet)
router.register(r'districts', views.DistrictViewSet)
router.register(r'elections', views.ElectionViewSet)
router.register(r'candidates', views.CandidateViewSet)
router.register(r'election_candidates', views.ElectionCandidateViewSet)
router.register(r'issue_categories', views.IssueCategoryViewSet)
router.register(r'polls', views.PollViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'candidate_positions', views.CandidatePositionViewSet)
router.register(r'public_answers', views.PublicAnswerViewSet)

# The API URLs are determined automatically by the router
# Additionally, include the login URLs for browsable API

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^schema/$', schema_view),
]
