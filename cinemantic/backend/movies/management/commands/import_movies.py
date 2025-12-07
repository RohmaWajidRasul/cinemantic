import sqlite3
from django.db import IntegrityError
from django.core.management.base import BaseCommand
from movies.models import Movie, Genre


class Command(BaseCommand):
    help = "Import movies from standalone SQLite DB → Postgres with field renaming, deduplication, and normalized genres."

    def add_arguments(self, parser):
        parser.add_argument('sqlite_db_path', type=str, help="Path to movies.db SQLite file")

    def handle(self, *args, **options):
        db_path = options['sqlite_db_path']

        # Connect to SQLite
        sqlite_conn = sqlite3.connect(db_path)
        sqlite_conn.row_factory = sqlite3.Row
        cursor = sqlite_conn.cursor()

        cursor.execute("SELECT * FROM movies")
        rows = cursor.fetchall()
        self.stdout.write(f"Found {len(rows)} movies in SQLite. Importing to Postgres...\n")

        imported = 0
        duplicates = 0

        for row in rows:
            raw = dict(row)

            # 1) Rename fields
            title = (raw.get("names") or "").strip()
            release_date = raw.get("date_x") or ""
            overview = (raw.get("overview") or "").strip()

            # ======== DEDUPLICATION RULE ========
            # Skip if Movie with same (title, release_date, overview) exists
            if Movie.objects.filter(
                title__iexact=title,
                release_date=release_date,
                overview__iexact=overview
            ).exists():
                duplicates += 1
                continue

            # 2) Extract genre names from SQLite (genre column)
            genre_text = raw.get("genre") or ""
            genre_names = [
                g.strip()
                for g in genre_text.replace("|", ",").split(",")
                if g.strip()
            ]

            # 3) Prepare movie_data mapped to your Django Movie model
            movie_data = {
                "title": title,
                "release_date": release_date,
                "score": raw.get("score"),
                "overview": overview,
                "crew": raw.get("crew") or "",
                "original_title": raw.get("orig_title") or "",
                "status": raw.get("status") or "",
                "original_language": raw.get("orig_lang") or "",
                "budget": raw.get("budget_x"),
                "revenue": raw.get("revenue"),
                "country": raw.get("country") or "",
            }

            # 4) Insert into Postgres
            try:
                movie = Movie.objects.create(**movie_data)
                imported += 1
            except IntegrityError:
                duplicates += 1
                continue

            # 5) Link genres
            for gname in genre_names:
                genre_obj, _ = Genre.objects.get_or_create(name=gname)
                movie.genres.add(genre_obj)

        sqlite_conn.close()

        self.stdout.write("\n🎬 Import Summary")
        self.stdout.write(f"   ✔ Imported movies:         {imported}")
        self.stdout.write(f"   ⚠ Duplicates skipped:      {duplicates}")
        self.stdout.write("   ✔ Movies + genres imported successfully into Postgres.\n")
