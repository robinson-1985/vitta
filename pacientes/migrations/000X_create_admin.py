from django.db import migrations


def create_admin(apps, schema_editor):
    User = apps.get_model("auth", "User")
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@vitta.com",
            password="SenhaForte123"
        )


class Migration(migrations.Migration):

    dependencies = [
       ("pacientes", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]
