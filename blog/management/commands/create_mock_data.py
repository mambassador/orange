from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
import random
from blog.models import Post, Comment

User = get_user_model()


class Command(BaseCommand):
    help = "Generate mock data for the User, Post, and Comment models."

    def handle(self, *args, **kwargs):
        total_users = 100
        total_posts_per_user = 50
        total_comments_per_post = 200
        fake = Faker()

        for _ in range(total_users):
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = f"{first_name.lower()}.{last_name.lower()}"
            email = f"{username}@example.com"

            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                description=fake.text(max_nb_chars=200),
                photo=fake.image_url(width=200, height=200),
            )

            self.stdout.write("Creating user ")

            posts = []
            for _ in range(total_posts_per_user):
                title = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
                description = fake.text(max_nb_chars=200)
                pub_date = fake.past_datetime(start_date="-30d", tzinfo=None)
                text = fake.paragraph(nb_sentences=10, variable_nb_sentences=True, ext_word_list=None)
                is_published = fake.boolean(chance_of_getting_true=90)
                is_approved = fake.boolean(chance_of_getting_true=90)

                post = Post.objects.create(
                    title=title,
                    description=description,
                    pub_date=pub_date,
                    author=user,
                    text=text,
                    is_published=is_published,
                    is_approved=is_approved,
                    photo=fake.image_url(width=800, height=600),
                )
                posts.append(post)

                self.stdout.write("Creating post ")

            for _ in range(total_comments_per_post):
                author = fake.name()
                text = fake.paragraph(nb_sentences=5, variable_nb_sentences=True, ext_word_list=None)
                pub_date = fake.past_datetime(tzinfo=None)
                is_published = fake.boolean(chance_of_getting_true=90)

                post = random.choice(posts)
                Comment.objects.create(
                    author=author,
                    post=post,
                    text=text,
                    pub_date=pub_date,
                    is_published=is_published,
                )
                self.stdout.write("Creating comment ")

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully generated {total_users} users, "
                f"{total_posts_per_user} posts per user, and "
                f"{total_comments_per_post} comments per post."
            )
        )
