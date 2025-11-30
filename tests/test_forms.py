"""
Tests for admin forms.

Tests the CountryFieldForm and CountryMultipleChoiceField
used in the Django CMS admin interface.
"""

import pytest
from django import forms
from django_countries import countries


class TestCountryMultipleChoiceField:
    """Tests for CountryMultipleChoiceField."""

    def test_default_choices(self):
        """Test that field has all countries as choices by default."""
        from djangocms_form_builder_countries.forms import CountryMultipleChoiceField

        field = CountryMultipleChoiceField()

        # Should have all countries
        assert len(field.choices) == len(list(countries))

    def test_not_required_by_default(self):
        """Test that field is not required by default."""
        from djangocms_form_builder_countries.forms import CountryMultipleChoiceField

        field = CountryMultipleChoiceField()

        assert field.required is False

    def test_widget_attributes(self):
        """Test that widget has correct CSS class and size."""
        from djangocms_form_builder_countries.forms import CountryMultipleChoiceField

        field = CountryMultipleChoiceField()

        assert isinstance(field.widget, forms.SelectMultiple)
        assert field.widget.attrs.get("class") == "form-select"
        assert field.widget.attrs.get("size") == "8"

    def test_custom_choices(self):
        """Test that custom choices can be provided."""
        from djangocms_form_builder_countries.forms import CountryMultipleChoiceField

        custom_choices = [("DE", "Germany"), ("AT", "Austria")]
        field = CountryMultipleChoiceField(choices=custom_choices)

        assert field.choices == custom_choices

    def test_can_be_made_required(self):
        """Test that field can be made required."""
        from djangocms_form_builder_countries.forms import CountryMultipleChoiceField

        field = CountryMultipleChoiceField(required=True)

        assert field.required is True

    def test_validates_country_codes(self):
        """Test that field validates selected country codes."""
        from djangocms_form_builder_countries.forms import CountryMultipleChoiceField

        field = CountryMultipleChoiceField()

        # Valid selection
        cleaned = field.clean(["DE", "AT"])
        assert cleaned == ["DE", "AT"]

        # Invalid selection should raise ValidationError
        with pytest.raises(forms.ValidationError):
            field.clean(["XX"])  # Invalid country code

    def test_accepts_empty_selection(self):
        """Test that empty selection is valid when not required."""
        from djangocms_form_builder_countries.forms import CountryMultipleChoiceField

        field = CountryMultipleChoiceField(required=False)

        cleaned = field.clean([])
        assert cleaned == []


class TestCountryFieldForm:
    """Tests for CountryFieldForm admin form."""

    def test_countries_first_field_exists(self):
        """Test that form has countries_first field."""
        from djangocms_form_builder_countries.forms import CountryFieldForm

        form = CountryFieldForm()

        assert "countries_first" in form.fields

    def test_countries_first_is_multiple_choice(self):
        """Test that countries_first is a MultipleChoiceField."""
        from djangocms_form_builder_countries.forms import CountryFieldForm, CountryMultipleChoiceField

        form = CountryFieldForm()

        assert isinstance(form.fields["countries_first"], CountryMultipleChoiceField)

    def test_countries_first_not_required(self):
        """Test that countries_first is not required."""
        from djangocms_form_builder_countries.forms import CountryFieldForm

        form = CountryFieldForm()

        assert form.fields["countries_first"].required is False

    def test_countries_first_has_help_text(self):
        """Test that countries_first has appropriate help text."""
        from djangocms_form_builder_countries.forms import CountryFieldForm

        form = CountryFieldForm()

        help_text = form.fields["countries_first"].help_text
        assert "countries" in help_text.lower()
        assert "DE" in help_text or "Germany" in help_text

    def test_countries_first_has_label(self):
        """Test that countries_first has a user-friendly label."""
        from djangocms_form_builder_countries.forms import CountryFieldForm

        form = CountryFieldForm()

        label = str(form.fields["countries_first"].label)
        assert "first" in label.lower() or "countries" in label.lower()
