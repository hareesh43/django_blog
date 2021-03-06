from django.contrib import admin
from .models import Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title','timestamp','updated']
    list_display_links  = ['title','updated']
    list_filter = ['updated']
    search_fields = ['content','title']



    class Meta:
        model = Post
        


admin.site.register(Post,PostModelAdmin)
