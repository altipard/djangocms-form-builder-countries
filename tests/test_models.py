"""
Tests for CountryField model.

Tests the proxy model functionality including:
- Form field generation
- Country ordering (priority countries first)
- Required/optional field behavior
- Placeholder handling
"""

from unittest.mock import Mock

from django import forms


class TestCountryFieldModel:
    """Tests for CountryField model and get_form_field method."""

    def create_country_field(self, config=None):
        """Create a mock CountryField instance with given config."""
        mock_field = Mock()
        mock_field.field_name = "country"
        mock_field.config = config or {}

        # Import here to ensure Django is configured
        from djangocms_form_builder_countries.models import CountryField

        mock_field.get_form_field = lambda: CountryField.get_form_field(mock_field)
        return mock_field

    def test_basic_field_generation(self):
        """Test that get_form_field returns a tuple with field name and ChoiceField."""
        field = self.create_country_field(
            {
                "field_label": "Country",
                "field_required": False,
            }
        )

        name, form_field = field.get_form_field()

        assert name == "country"
        assert isinstance(form_field, forms.ChoiceField)
        assert form_field.label == "Country"
        assert form_field.required is False

    def test_required_field(self):
        """Test that required=True produces a required form field."""
        field = self.create_country_field(
            {
                "field_label": "Country",
                "field_required": True,
            }
        )

        name, form_field = field.get_form_field()

        assert form_field.required is True
        # Required fields should not have a blank option at the start
        first_choice_value = form_field.choices[0][0]
        assert first_choice_value != "" or form_field.choices[0][1] == "---"

    def test_optional_field_has_blank_choice(self):
        """Test that optional fields have a blank/placeholder option."""
        field = self.create_country_field(
            {
                "field_label": "Country",
                "field_required": False,
            }
        )

        name, form_field = field.get_form_field()

        first_choice = form_field.choices[0]
        assert first_choice[0] == ""
        assert first_choice[1] == "Select a country"

    def test_custom_placeholder(self):
        """Test that custom placeholder text is used for blank choice."""
        field = self.create_country_field(
            {
                "field_label": "Country",
                "field_required": False,
                "field_placeholder": "Choose your country",
            }
        )

        name, form_field = field.get_form_field()

        first_choice = form_field.choices[0]
        assert first_choice[0] == ""
        assert first_choice[1] == "Choose your country"

    def test_countries_first_ordering(self):
        """Test that priority countries appear first in choices."""
        field = self.create_country_field(
            {
                "field_label": "Country",
                "field_required": True,
                "countries_first": ["DE", "AT", "CH"],
            }
        )

        name, form_field = field.get_form_field()
        choices = form_field.choices

        # First three should be DE, AT, CH in that order
        assert choices[0][0] == "DE"
        assert choices[1][0] == "AT"
        assert choices[2][0] == "CH"
        # Separator after priority countries
        assert choices[3] == ("", "---")

    def test_countries_first_case_insensitive(self):
        """Test that country codes are matched case-insensitively."""
        field = self.create_country_field(
            {
                "field_label": "Country",
                "field_required": True,
                "countries_first": ["de", "at"],  # lowercase
            }
        )

        name, form_field = field.get_form_field()
        choices = form_field.choices

        # Should still work with lowercase codes
        assert choices[0][0] == "DE"
        assert choices[1][0] == "AT"

    def test_empty_countries_first(self):
        """Test behavior with empty countries_first list."""
        field = self.create_country_field(
            {
                "field_label": "Country",
                "field_required": True,
                "countries_first": [],
            }
        )

        name, form_field = field.get_form_field()

        # Should not have separator
        separator_count = sum(1 for c in form_field.choices if c == ("", "---"))
        assert separator_count == 0

    def test_widget_class(self):
        """Test that the widget has the correct CSS class."""
        field = self.create_country_field(
            {
                "field_label": "Country",
                "field_required": False,
            }
        )

        name, form_field = field.get_form_field()

        assert "class" in form_field.widget.attrs
        assert form_field.widget.attrs["class"] == "form-select"

    def test_all_countries_present(self):
        """Test that all standard countries are present in choices."""

        field = self.create_country_field(
            {
                "field_label": "Country",
                "field_required": True,
            }
        )

        name, form_field = field.get_form_field()
        choice_codes = {c[0] for c in form_field.choices if c[0]}

        # Check some common countries are present
        assert "DE" in choice_codes  # Germany
        assert "US" in choice_codes  # United States
        assert "GB" in choice_codes  # United Kingdom
        assert "FR" in choice_codes  # France
        assert "JP" in choice_codes  # Japan

    def test_invalid_country_code_ignored(self):
        """Test that invalid country codes in countries_first are handled gracefully."""
        field = self.create_country_field(
            {
                "field_label": "Country",
                "field_required": True,
                "countries_first": ["XX", "DE", "ZZ"],  # XX and ZZ are invalid
            }
        )

        name, form_field = field.get_form_field()
        choices = form_field.choices

        # DE should be first, invalid codes should be ignored
        assert choices[0][0] == "DE"
        # Check that XX and ZZ are not in the choices
        choice_codes = [c[0] for c in choices]
        assert "XX" not in choice_codes
        assert "ZZ" not in choice_codes
