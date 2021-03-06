from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Account)
admin.site.register(UserAuthToken)

admin.site.register(CourseCategory)
admin.site.register(CourseSubCategory)
admin.site.register(DegreeCourse)
admin.site.register(Teacher)
admin.site.register(Scholarship)
admin.site.register(Course)
admin.site.register(CourseDetail)

admin.site.register(OftenAskedQuestion)
admin.site.register(CourseOutline)
admin.site.register(CourseChapter)
admin.site.register(CourseSection)
admin.site.register(Homework)
admin.site.register(PricePolicy)
admin.site.register(ArticleSource)
admin.site.register(Article)
admin.site.register(Agree)
admin.site.register(Collection)
admin.site.register(Comment)