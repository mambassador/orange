from django.core.management.base import BaseCommand

from blog.models import Post, User, Comment


class Command(BaseCommand):
    help = "Deletes all mock data from the tables"  # NOQA A003

    def handle(self, *args, **options):
        self.stdout.write("Deleting mock data...")

        User.objects.all().delete()
        Post.objects.all().delete()
        Comment.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Mock data deleted successfully."))
