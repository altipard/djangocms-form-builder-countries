"""
Pytest configuration for djangocms-form-builder-countries tests.

Configures Django settings and provides fixtures for testing
Django CMS plugins without a full CMS installation.
"""

import os
import sys

import django
import pytest


def pytest_configure(config):
    """Configure Django settings for tests."""
    # Add the tests directory to the path so settings can be found
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    if tests_dir not in sys.path:
        sys.path.insert(0, tests_dir)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

    # Setup Django
    django.setup()


@pytest.fixture(scope='session')
def django_db_setup():
    """Set up test database."""
    from django.conf import settings
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }


@pytest.fixture
def country_field_config():
    """Provide common country field configurations for tests."""
    return {
        'default': {
            'field_label': 'Country',
            'field_name': 'country',
            'field_required': False,
        },
        'required': {
            'field_label': 'Country',
            'field_name': 'country',
            'field_required': True,
        },
        'with_priority': {
            'field_label': 'Country',
            'field_name': 'country',
            'field_required': True,
            'countries_first': ['DE', 'AT', 'CH'],
        },
        'with_placeholder': {
            'field_label': 'Country',
            'field_name': 'country',
            'field_required': False,
            'field_placeholder': 'Please select your country',
        },
    }
