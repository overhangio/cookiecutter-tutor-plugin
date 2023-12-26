{{ cookiecutter.plugin_name}} plugin for `Tutor <https://docs.tutor.edly.io>`__
###############################################################################

{{ cookiecutter.description }}


Installation
************

.. code-block:: bash

    pip install git+{{ cookiecutter.git_repo }}

Usage
*****

.. code-block:: bash

    tutor plugins enable {{ cookiecutter.plugin_name }}

{%- if cookiecutter.license != 'Not open source' %}
License
*******

This software is licensed under the terms of the {{ cookiecutter.license }}.
{% endif %}