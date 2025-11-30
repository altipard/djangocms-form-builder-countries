"""
Country field model for djangocms-form-builder.

Provides a proxy model that integrates django-countries
with the Django CMS Form Builder plugin system.
"""

from django import forms
from django.utils.translation import gettext_lazy as _

from djangocms_form_builder.models import FormField
from django_countries import countries


class CountryField(FormField):
    """
    Proxy model for country selection field in Django CMS Form Builder.

    Stores configuration in the JSON 'config' field inherited from FormField.

    Configuration options:
        field_name: Internal field name
        field_label: Label shown to user
        field_required: Whether field is required
        field_placeholder: Placeholder text (used as blank label)
        countries_first: List of country codes to show first (e.g., ['DE', 'AT', 'CH'])
    """

    class Meta:
        proxy = True
        verbose_name = _("Country field")
        verbose_name_plural = _("Country fields")

    def get_form_field(self):
        """
        Return the Django form field for this country selector.

        Uses django-countries to provide all ISO 3166-1 countries
        with localized names.

        Returns:
            tuple: (field_name, ChoiceField) for form construction
        """
        first_countries = self.config.get('countries_first', [])
        choices = list(countries)

        if first_countries:
            first_choices = []
            remaining_choices = []
            first_set = set(code.upper() for code in first_countries)

            for code, name in choices:
                if code in first_set:
                    first_choices.append((code, name))
                else:
                    remaining_choices.append((code, name))

            # Sort first_choices by the order specified in first_countries
            first_order = {code.upper(): i for i, code in enumerate(first_countries)}
            first_choices.sort(key=lambda x: first_order.get(x[0], 999))

            # Add separator between priority and remaining countries
            if first_choices:
                choices = first_choices + [('', '---')] + remaining_choices
            else:
                choices = remaining_choices

        required = self.config.get('field_required', False)
        placeholder = self.config.get('field_placeholder', '')

        if not required:
            blank_label = placeholder if placeholder else _("Select a country")
            choices = [('', blank_label)] + choices

        return self.field_name, forms.ChoiceField(
            label=self.config.get('field_label', ''),
            required=required,
            choices=choices,
            widget=forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
        )
