"""
Pytest configuration for djangocms-form-builder-countries tests.

Provides fixtures for testing Django CMS plugins.
"""

import pytest


@pytest.fixture
def country_field_config():
    """Provide common country field configurations for tests."""
    return {
        "default": {
            "field_label": "Country",
            "field_name": "country",
            "field_required": False,
        },
        "required": {
            "field_label": "Country",
            "field_name": "country",
            "field_required": True,
        },
        "with_priority": {
            "field_label": "Country",
            "field_name": "country",
            "field_required": True,
            "countries_first": ["DE", "AT", "CH"],
        },
        "with_placeholder": {
            "field_label": "Country",
            "field_name": "country",
            "field_required": False,
            "field_placeholder": "Please select your country",
        },
    }
