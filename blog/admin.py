from django.contrib import admin
from .models import User, Post, Comment
from django.core.mail import send_mail
from django.urls import reverse


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_superuser")
    ordering = ("-date_joined",)


admin.site.register(User, UserAdmin)


class IsPublishedFilter(admin.SimpleListFilter):
    title = "Published"
    parameter_name = "is_published"

    def lookups(self, request, model_admin):
        return (
            ("published", "Published"),
            ("not_published", "Not Published"),
        )

    def queryset(self, request, queryset):
        if self.value() == "published":
            return queryset.filter(is_published=True)
        elif self.value() == "not_published":
            return queryset.filter(is_published=False)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "pub_date", "is_published")
    search_fields = ("author", "post__title", "text")
    date_hierarchy = "pub_date"
    ordering = ("-pub_date",)
    list_filter = (IsPublishedFilter,)  # Add the custom filter here

    def mark_published(self, request, queryset):
        queryset.update(is_published=True)

        for comment in queryset.filter(is_published=True):
            post_author_email = comment.post.author.email
            post_link = request.build_absolute_uri(reverse("blog:post", args=[comment.post.pk]))
            message = f"Your post has a new comment!\n\nView the comment: {post_link}"

            send_mail(
                "New Comment on Your Post",
                message,
                "admin@orange.com",
                [post_author_email],
                fail_silently=False,
            )

    mark_published.short_description = "Mark selected comments as Published"
    actions = [mark_published]


admin.site.register(Comment, CommentAdmin)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "pub_date", "is_approved")
    search_fields = (
        "title",
        "description",
        "author__username",
        "author__first_name",
        "author__last_name",
    )
    list_filter = ("is_approved", "pub_date")
    date_hierarchy = "pub_date"
    ordering = ("-pub_date",)
    inlines = [CommentInline]

    def mark_approved(self, request, queryset):
        queryset.update(is_approved=True)

    def mark_not_approved(self, request, queryset):
        queryset.update(is_approved=False)

    mark_approved.short_description = "Mark selected posts as Approved"
    mark_not_approved.short_description = "Mark selected posts as Not Approved"

    actions = [mark_approved, mark_not_approved]


admin.site.register(Post, PostAdmin)
