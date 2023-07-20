from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost
from django.contrib import admin
# Apply summernote to all TextField in model.
class BlogPostModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content',)

admin.site.register(BlogPost, BlogPostModelAdmin)
