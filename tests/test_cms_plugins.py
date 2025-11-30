"""
Tests for CMS plugin registration and configuration.

Tests the CountryFieldPlugin registration with Django CMS
and its fieldset configuration.
"""


class TestCountryFieldPlugin:
    """Tests for CountryFieldPlugin configuration."""

    def test_plugin_registered(self):
        """Test that CountryFieldPlugin is registered in the plugin pool."""
        from cms.plugin_pool import plugin_pool

        # Get all registered plugins
        plugins = plugin_pool.get_all_plugins()
        plugin_names = [p.__name__ for p in plugins]

        assert "CountryFieldPlugin" in plugin_names

    def test_plugin_attributes(self):
        """Test that plugin has correct attributes."""
        from djangocms_form_builder_countries.cms_plugins import CountryFieldPlugin

        assert hasattr(CountryFieldPlugin, "name")
        assert hasattr(CountryFieldPlugin, "module")
        assert hasattr(CountryFieldPlugin, "model")
        assert hasattr(CountryFieldPlugin, "form")

    def test_plugin_uses_country_field_model(self):
        """Test that plugin uses CountryField model."""
        from djangocms_form_builder_countries.cms_plugins import CountryFieldPlugin
        from djangocms_form_builder_countries.models import CountryField

        assert CountryFieldPlugin.model == CountryField

    def test_plugin_uses_country_field_form(self):
        """Test that plugin uses CountryFieldForm."""
        from djangocms_form_builder_countries.cms_plugins import CountryFieldPlugin
        from djangocms_form_builder_countries.forms import CountryFieldForm

        assert CountryFieldPlugin.form == CountryFieldForm

    def test_plugin_has_fieldsets(self):
        """Test that plugin has fieldsets configured."""
        from djangocms_form_builder_countries.cms_plugins import CountryFieldPlugin

        assert hasattr(CountryFieldPlugin, "fieldsets")
        assert len(CountryFieldPlugin.fieldsets) >= 1

    def test_fieldsets_include_countries_first(self):
        """Test that fieldsets include countries_first configuration."""
        from djangocms_form_builder_countries.cms_plugins import CountryFieldPlugin

        # Flatten all fields from fieldsets
        all_fields = []
        for fieldset in CountryFieldPlugin.fieldsets:
            fieldset_fields = fieldset[1].get("fields", [])
            for field in fieldset_fields:
                if isinstance(field, (list, tuple)):
                    all_fields.extend(field)
                else:
                    all_fields.append(field)

        assert "countries_first" in all_fields

    def test_plugin_module_is_forms(self):
        """Test that plugin is categorized under Forms module."""
        from djangocms_form_builder_countries.cms_plugins import CountryFieldPlugin

        module = str(CountryFieldPlugin.module)
        assert "form" in module.lower()

    def test_plugin_name_is_country(self):
        """Test that plugin name indicates it's a country field."""
        from djangocms_form_builder_countries.cms_plugins import CountryFieldPlugin

        name = str(CountryFieldPlugin.name)
        assert "country" in name.lower()


class TestAppConfiguration:
    """Tests for Django app configuration."""

    def test_app_config_name(self):
        """Test that app config has correct name."""
        from djangocms_form_builder_countries.apps import CountriesFieldConfig

        assert CountriesFieldConfig.name == "djangocms_form_builder_countries"

    def test_app_config_verbose_name(self):
        """Test that app config has a verbose name."""
        from djangocms_form_builder_countries.apps import CountriesFieldConfig

        assert CountriesFieldConfig.verbose_name is not None
        assert len(CountriesFieldConfig.verbose_name) > 0


class TestPackageMetadata:
    """Tests for package metadata."""

    def test_version_defined(self):
        """Test that package version is defined."""
        import djangocms_form_builder_countries

        assert hasattr(djangocms_form_builder_countries, "__version__")
        assert djangocms_form_builder_countries.__version__ is not None

    def test_version_format(self):
        """Test that version follows semver format."""
        import djangocms_form_builder_countries

        version = djangocms_form_builder_countries.__version__
        parts = version.split(".")

        # Should have at least major.minor.patch
        assert len(parts) >= 3
        # Major, minor, patch should be numeric
        assert parts[0].isdigit()
        assert parts[1].isdigit()
        # Patch might have additional suffixes like 'a1', 'b2', 'rc1'
        assert parts[2][0].isdigit()
