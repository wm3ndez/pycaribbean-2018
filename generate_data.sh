#!/usr/bin/env bash
python manage.py generate_users --quantity 100
python manage.py generate_tags --quantity 10000
python manage.py generate_categories --quantity 300
python manage.py generate_posts --quantity 10000 --blog 1
python manage.py copy_posts --blog 2
python manage.py copy_posts --blog 3
python manage.py copy_posts --blog 4