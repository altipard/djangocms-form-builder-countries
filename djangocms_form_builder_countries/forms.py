"""
Admin forms for country field plugin configuration.

Provides the form used in the Django CMS structure board
for configuring country field options.
"""

from django import forms
from django.utils.translation import gettext_lazy as _
from django_countries import countries
from djangocms_form_builder.forms import FormFieldMixin
from djangocms_form_builder.models import FormField
from entangled.forms import EntangledModelForm


class CountryMultipleChoiceField(forms.MultipleChoiceField):
    """
    Multiple choice field for selecting countries to show first.

    Pre-configured with all countries as choices and appropriate
    widget styling for the Django CMS admin.
    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('choices', list(countries))
        kwargs.setdefault('required', False)
        kwargs.setdefault('widget', forms.SelectMultiple(attrs={
            'class': 'form-select',
            'size': '8',
        }))
        super().__init__(*args, **kwargs)


class CountryFieldForm(FormFieldMixin, EntangledModelForm):
    """
    Admin form for configuring a country selection field.

    Extends the base FormFieldMixin to include country-specific options
    like configuring which countries to show first in the dropdown.
    """

    class Meta:
        model = FormField
        entangled_fields = {
            'config': [
                'countries_first',
            ]
        }

    countries_first = CountryMultipleChoiceField(
        label=_("Countries shown first"),
        help_text=_(
            "Select countries to display at the top of the dropdown. "
            "Common choices: Germany (DE), Austria (AT), Switzerland (CH)."
        ),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs and kwargs['instance']:
            instance = kwargs['instance']
            if hasattr(instance, 'config') and 'countries_first' not in instance.config:
                # Default to DACH countries for new instances
                self.fields['countries_first'].initial = ['DE', 'AT', 'CH']
