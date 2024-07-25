{{ cookiecutter.plugin_name }} plugin for `Tutor <https://docs.tutor.edly.io>`__
{%- set heading_underline_length = (cookiecutter.plugin_name | length + 50) %}
{{ '#' * heading_underline_length }}

{{ cookiecutter.description }}


Installation
************

.. code-block:: bash

    pip install git+{{ cookiecutter.git_repo }}

Usage
*****

.. code-block:: bash

    tutor plugins enable {{ cookiecutter.plugin_name }}

{% if cookiecutter.license != 'Not open source' %}
License
*******

This software is licensed under the terms of the {{ cookiecutter.license }}.
{% endif %}