"""
CMS Plugin registration for country field.

Registers the CountryFieldPlugin with the Django CMS plugin pool,
making it available in the Form Builder structure board.
"""

from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from djangocms_form_builder import forms as form_builder_forms
from djangocms_form_builder import settings as form_builder_settings
from djangocms_form_builder.cms_plugins.form_plugins import FormElementPlugin

from .forms import CountryFieldForm
from .models import CountryField

# Get mixin factory from form builder settings
mixin_factory = form_builder_settings.get_renderer(form_builder_forms)


@plugin_pool.register_plugin
class CountryFieldPlugin(mixin_factory("SelectField"), FormElementPlugin):
    """
    Django CMS plugin for country selection in forms.

    Integrates django-countries with djangocms-form-builder,
    providing a dropdown field with all ISO 3166-1 countries.

    Features:
        - All countries with localized names
        - Option to show specific countries first (e.g., DACH region)
        - Integrates with Form Builder's validation and submission system
    """

    name = _("Country")
    module = _("Forms")
    model = CountryField
    form = CountryFieldForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("field_label", "field_name"),
                    ("field_required", "field_placeholder"),
                )
            },
        ),
        (
            _("Country Options"),
            {
                "classes": ("collapse",),
                "description": _(
                    "Configure which countries to show first in the dropdown. "
                    "This is useful for forms targeting specific regions."
                ),
                "fields": ("countries_first",),
            },
        ),
    )

    def get_render_template(self, context, instance, placeholder):
        """
        Return the template for rendering the country field.

        Uses the standard form builder select template.
        """
        return f"djangocms_form_builder/{form_builder_settings.framework}/widgets/base.html"
