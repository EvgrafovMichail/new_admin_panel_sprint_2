from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="filmwork",
            name="file_path",
            field=models.FileField(blank=True, null=True, upload_to="movies/", verbose_name="file"),
        ),
    ]
