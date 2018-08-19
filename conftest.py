import os
import sys

from django import setup
from django.conf import settings

TEST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'demo', 'templates')

def pytest_configure():
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'test.db',
            }
        },
        INSTALLED_APPS=[
            'django_bootstrap_breadcrumbs',
            'view_breadcrumbs',
            'demo'
        ],
        ROOT_URLCONF='demo.urls',
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [TEST_DIR],
                'APP_DIRS': True,
            }
        ]
    )
    setup()
    create_db()


def create_db():
    if (sys.version_info < (3, 6)):
        from django.db import connection

        with connection.cursor() as c:
            c.executescript(
            """
            BEGIN;
            --
            -- Create model TestModel
            --
            DROP TABLE  IF EXISTS "demo_testmodel";
            CREATE TABLE "demo_testmodel" ("created_at" datetime NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "update_at" datetime NOT NULL, "name" varchar(50) NOT NULL);
            COMMIT;
            """)