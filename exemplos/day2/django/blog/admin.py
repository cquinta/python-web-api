from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "published")
    list_filter = ("published", "date")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["-date"]
    actions = ["publish", "unpublish"]

    @admin.action(description="Publish selected posts")
    def publish(self, request, queryset):
        queryset.update(published=True)
        
    @admin.action(description="Unpublish selected posts")
    def unpublish(self, request, queryset):
        queryset.update(published=False)
        


# Register your models here.
admin.site.register(Post, PostAdmin)