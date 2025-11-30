================================
djangocms-form-builder-countries
================================

|pypi| |python| |django| |djangocms| |license|

**djangocms-form-builder-countries** is a plugin extension for
`djangocms-form-builder <https://github.com/django-cms/djangocms-form-builder>`_
that adds a country selector field to the form builder.

It integrates `django-countries <https://github.com/SmileyChris/django-countries>`_
with the Django CMS Form Builder, providing a dropdown field with all ISO 3166-1
countries and localized country names.

Key Features
============

- Country dropdown field for djangocms-form-builder forms
- All ISO 3166-1 countries with localized names
- Configurable "countries first" option to prioritize specific countries
  (e.g., DACH region: Germany, Austria, Switzerland)
- Full integration with form builder validation and submission system
- Bootstrap 5 compatible styling
- Works with djangocms-form-builder's XHR-based form submission


Installation
============

Install the package via pip::

    pip install djangocms-form-builder-countries

Or with your preferred package manager.


Configuration
=============

Add the package to your ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        ...
        'django_countries',
        'djangocms_form_builder_countries',
        ...
    ]

No migrations are required as the plugin uses a proxy model.


Usage
=====

After installation, a new "Country" field type will be available in the
Django CMS Form Builder structure board under the "Forms" module.

Adding a Country Field
----------------------

1. Create or edit a form in the Django CMS structure board
2. Add a new plugin to the form
3. Select "Country" from the "Forms" module
4. Configure the field:

   - **Field Label**: The label shown to users
   - **Field Name**: The internal field name for form processing
   - **Required**: Whether the field is mandatory
   - **Placeholder**: Text shown when no country is selected

5. Optionally configure "Countries First" to show specific countries
   at the top of the dropdown

Countries First Feature
-----------------------

The "Countries First" option allows you to prioritize specific countries
at the top of the dropdown list. This is useful for forms targeting
specific regions.

For example, for a form targeting the DACH region, you can select:

- Germany (DE)
- Austria (AT)
- Switzerland (CH)

These countries will appear at the top of the list, followed by a separator
and all other countries in alphabetical order.


Requirements
============

- Python 3.9+
- Django 4.2+
- django-cms 4.1+
- djangocms-form-builder 2.0+
- django-countries 7.0+


Contributing
============

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (``git checkout -b feature/amazing-feature``)
3. Commit your changes (``git commit -m 'Add some amazing feature'``)
4. Push to the branch (``git push origin feature/amazing-feature``)
5. Open a Pull Request


License
=======

This project is licensed under the MIT License - see the LICENSE file for details.


.. |pypi| image:: https://img.shields.io/pypi/v/djangocms-form-builder-countries.svg
    :target: https://pypi.org/project/djangocms-form-builder-countries/

.. |python| image:: https://img.shields.io/pypi/pyversions/djangocms-form-builder-countries.svg
    :target: https://pypi.org/project/djangocms-form-builder-countries/

.. |django| image:: https://img.shields.io/badge/django-4.2%20%7C%205.0%20%7C%205.1%20%7C%205.2-blue.svg
    :target: https://www.djangoproject.com/

.. |djangocms| image:: https://img.shields.io/badge/django--cms-4.1%20%7C%205.0-blue.svg
    :target: https://www.django-cms.org/

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT
