from datetime import datetime, timedelta
from typing import Iterable

from django.db.models import Count

from .models import JobApplication, HealthStatus

WEEKLY_APPLICATIONS_MINIMUM_THRESHOLD = 2
DUE_DATE_THRESHOLD_RED = 2
DUE_DATE_THRESHOLD_YELLOW = 7

def compute_status(applications: Iterable[JobApplication], today: datetime) -> HealthStatus:
    past_weeks_applications = [a for a in applications if a.date_applied >= today - timedelta(days=7)]
    if len(past_weeks_applications) < WEEKLY_APPLICATIONS_MINIMUM_THRESHOLD:
        return HealthStatus.RED

    due_dates = [a.date_applied for a in applications]

    if due_dates:
        soonest_due_date = min(due_dates)
        if soonest_due_date <= today + timedelta(days=DUE_DATE_THRESHOLD_RED):
            return HealthStatus.RED
        elif soonest_due_date <= today + timedelta(days=DUE_DATE_THRESHOLD_YELLOW):
            return HealthStatus.YELLOW

    return HealthStatus.GREEN


def compute_application_funnel_dict(applications: Iterable[JobApplication]) -> dict:
    # funnel from strictest to least restrictive
    get_count = lambda s: len([a for a in applications if a.status == s])
    statuses = [
        JobApplication.Status.SAVED,
        JobApplication.Status.APPLIED,
        JobApplication.Status.REJECTED_PRESCREEN,
        JobApplication.Status.UNDER_REVIEW,
        JobApplication.Status.INTERVIEWING,
        JobApplication.Status.REJECTED_POSTINTERVIEW,
        JobApplication.Status.RECEIVED_OFFER,
    ]

    funnel_dict = {s[1]: get_count(s) for s in statuses}





    #for a in applications:

    #status_counts_qs = JobApplication.objects.values('status').annotate(count=Count('status'))
    #status_counts_dict = {status['status']: status['count'] for status in status_counts_qs}
    status_counts_dict = {
        JobApplication.Status.APPLIED: status_counts_qs[JobApplication.Status.APPLIED[0]]
    }

    total = 0
    # for k in JobApplication.STATUS_ORDERING
    # for t in reversed(status_counts_dict):
    #     total += status_counts_dict[t]
    #     status_counts_dict[t] = total





