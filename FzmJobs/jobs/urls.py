from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import JobApplicationViewSet, DashboardView

router = DefaultRouter()
# Use .register() for ViewSets
router.register(r'applications', JobApplicationViewSet)

# Add to urlpatterns for other views
urlpatterns = router.urls + [
    path('dashboard/', DashboardView.as_view())
]