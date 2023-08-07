from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from .forms import UserSignUpForm, UserUpdateForm, PostForm, CommentForm, ContactForm
from blog.forms import LoginUserForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views import generic
from .models import Post, User
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.views.generic.edit import FormView
from django.core.mail import send_mail


def index(request):
    return render(request, "index.html")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "registration/login.html"


class UserCreateView(SuccessMessageMixin, generic.CreateView):
    template_name = "registration/register.html"
    success_url = reverse_lazy("index")
    form_class = UserSignUpForm
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        super().form_valid(form)
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password1"])
        user.save()
        login(self.request, user)
        return redirect(self.get_success_url())


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return get_object_or_404(User, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        time_on_site = timezone.now() - user.date_joined

        years_on_site = time_on_site.days // 365
        days_on_site = time_on_site.days % 365

        context["years_on_site"] = years_on_site
        context["days_on_site"] = days_on_site
        return context


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "blog/user_form.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy("blog:user_detail", args=[self.request.user.pk])

    def form_valid(self, form):
        user = self.get_object()
        if "photo" in self.request.FILES:
            user.photo = self.request.FILES["photo"]
            user.save()
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:my_posts")
    success_message = "Post created successfully!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.photo = self.request.FILES.get("photo")

        send_mail(
            "Contact Form Submission",
            f"{form.instance.author.username} has published new post"
            f"Check admin panel to approve or decline publication",
            "admin@orange.com",
            [form.instance.author.email],
            fail_silently=False,
        )
        return super().form_valid(form)

    def get_success_url(self):
        user_pk = self.object.author.pk if self.object.author else None
        if user_pk is not None:
            return reverse_lazy("blog:my_posts", kwargs={"pk": user_pk})
        else:
            return super().get_success_url()


class PostUpdateView(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_message = "Post updated successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_type"] = "update"
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        user_pk = self.object.author.pk if self.object.author else None
        if user_pk is not None:
            return reverse_lazy("blog:my_posts", kwargs={"pk": user_pk})
        else:
            return super().get_success_url()


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(is_published=True, is_approved=True).select_related("author").order_by("-pub_date")


class UserPostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = "blog/userpost_list.html"
    paginate_by = 5

    def get_queryset(self):
        user_pk = self.kwargs.get("pk")
        return Post.objects.select_related("author").filter(author__pk=user_pk).order_by("is_published")


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object

        comments = post.comment_set.filter(is_published=True).order_by("-pub_date")

        paginator = Paginator(comments, 3)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        form = self.form_class(request=self.request)

        context["comments"] = page_obj
        context["form"] = form

        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = self.form_class(request.POST, request=request)

        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.author = request.user.get_full_name()
            comment.post = post
            comment.save()

            send_mail(
                "Created new Comment",
                f"{request.user} has published new post" f"Check admin panel to approve or decline publication",
                "admin@orange.com",
                ["service@orange.com"],
                fail_silently=False,
            )

            return redirect("blog:post", pk=post.pk)

        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[str(self.object.pk)])


class ContactView(SuccessMessageMixin, FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("blog:posts")
    success_message = "Your contact request was sent successfully"

    def form_valid(self, form):
        first_name = form.cleaned_data["first_name"]
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]

        send_mail(
            "Contact Form Submission",
            f"Name: {first_name}\nEmail: {email}\nMessage: {message}",
            "admin@orange.com",
            [email],
            fail_silently=False,
        )
        form.save()
        return super().form_valid(form)
