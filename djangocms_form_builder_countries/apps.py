"""
Django application configuration for djangocms-form-builder-countries.
"""

from django.apps import AppConfig


class CountriesFieldConfig(AppConfig):
    """Application configuration for the countries field plugin."""

    name = "djangocms_form_builder_countries"
    verbose_name = "Django CMS Form Builder Countries"

    def ready(self):
        """Register CMS plugins when the application is ready."""
        from . import cms_plugins  # noqa: F401
