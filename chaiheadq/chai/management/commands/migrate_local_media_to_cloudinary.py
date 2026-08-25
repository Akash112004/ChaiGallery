from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand, CommandError

from chai.models import Tea


class Command(BaseCommand):
    help = "Upload locally stored Tea images to the configured Cloudinary storage."

    def _candidate_paths(self, relative_name: str):
        name_path = Path(relative_name)
        basename = name_path.name
        return [
            Path(settings.MEDIA_ROOT) / relative_name,
            Path(settings.MEDIA_ROOT) / "tea_images" / basename,
            Path(settings.BASE_DIR) / "media" / relative_name,
            Path(settings.BASE_DIR) / "media" / "tea_images" / basename,
            Path(settings.BASE_DIR).parent / "chaiheadq" / "media" / relative_name,
            Path(settings.BASE_DIR).parent / "chaiheadq" / "media" / "tea_images" / basename,
            Path(settings.BASE_DIR).parent / "media" / relative_name,
            Path(settings.BASE_DIR).parent / "media" / "tea_images" / basename,
        ]

    def handle(self, *args, **options):
        credentials = settings.CLOUDINARY_STORAGE
        required_settings = ("CLOUD_NAME", "API_KEY", "API_SECRET")
        missing = [name for name in required_settings if not credentials.get(name)]
        if missing:
            raise CommandError(
                "Cloudinary credentials are missing: " + ", ".join(missing)
            )

        if "cloudinary_storage" not in default_storage.__class__.__module__:
            raise CommandError("The default storage is not configured for Cloudinary.")

        migrated = 0
        skipped = 0
        for tea in Tea.objects.exclude(image=""):
            relative_name = tea.image.name
            local_path = None
            for candidate in self._candidate_paths(relative_name):
                if candidate.is_file():
                    local_path = candidate
                    break

            if not local_path:
                self.stdout.write(self.style.WARNING(f"Skipped missing file: {relative_name}"))
                skipped += 1
                continue

            if not local_path.is_file():
                self.stdout.write(self.style.WARNING(f"Skipped missing file: {relative_name}"))
                skipped += 1
                continue

            with local_path.open("rb") as image_file:
                tea.image.save(relative_name, File(image_file), save=True)
            migrated += 1
            self.stdout.write(self.style.SUCCESS(f"Uploaded: {relative_name}"))

        self.stdout.write(
            self.style.SUCCESS(f"Completed: {migrated} uploaded, {skipped} skipped.")
        )
