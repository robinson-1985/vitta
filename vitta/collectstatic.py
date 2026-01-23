import os
from django.core.management import call_command

if os.environ.get("RAILWAY_ENVIRONMENT") == "production":
    try:
        call_command("collectstatic", interactive=False, verbosity=0)
    except Exception as e:
        print("collectstatic failed:", e)
