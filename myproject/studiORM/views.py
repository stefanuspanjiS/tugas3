from django.db.models import Count, Avg
from django.shortcuts import render
from .models import User, Course

def statistics_view(request):
    total_users = User.objects.count()
    users_with_courses = User.objects.annotate(course_count=Count('studiORM')).filter(course_count__gt=0).count()
    users_without_courses = total_users - users_with_courses
    average_courses_per_user = User.objects.annotate(course_count=Count('studiORM')).aggregate(Avg('course_count'))['course_count__avg']
    user_with_most_courses = User.objects.annotate(course_count=Count('studiORM')).order_by('-course_count').first()
    users_without_any_course = User.objects.annotate(course_count=Count('studiORM')).filter(course_count=0)

    context = {
        'total_users': total_users,
        'users_with_courses': users_with_courses,
        'users_without_courses': users_without_courses,
        'average_courses_per_user': average_courses_per_user,
        'user_with_most_courses': user_with_most_courses,
        'users_without_any_course': users_without_any_course,
    }
    return render(request, 'statistics.html', context)
