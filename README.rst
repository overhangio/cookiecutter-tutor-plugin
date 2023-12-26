Tutor plugin cookiecutter 🍪
############################

This is a `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/README.html>`__ for getting started with `Tutor plugins <https://docs.tutor.edly.io/plugins/index.html>`__. It will generate a base scaffold for an empty tutor plugin that does, well, nothing.

Requirements
************

.. code-block:: bash

    pip install -U cookiecutter

Usage
*****

.. code-block:: bash

    cookiecutter https://github.com/overhangio/cookiecutter-tutor-plugin.git

Please keep the "contrib" part in your generated package name to differentiate from official plugins.

Once you have generated your plugin, you can start using it right away (even if it won't do anything)

.. code-block:: bash

    pip install -e ./tutor-contrib-myplugin
    tutor plugins list  # Your plugin should appear here
    tutor plugins enable myplugin  # Have fun!

Migrating from v0 plugins
*************************

.. _Migrating from v0 plugins: docs/migrating-from-v0-plugins.rst

The plugin API was upgraded from ``v0`` to ``v1`` in `Tutor v13.2.0 <https://github.com/overhangio/tutor/releases/tag/v13.2.0>`__. This cookiecutter generates plugin scaffolds for ``v1``. The ``v0`` API will be supported for some time, but you are encouraged to upgrade your plugins. To upgrade a ``v0`` plugin that was generated previously with this cookiecutter, please follow the instructions in the `Migrating from v0 plugins`_ section.

Troubleshooting
***************

This Tutor plugin template is maintained by `Emad Rad <https://github.com/CodeWithEmad>`_ from `edSPIRIT <https://edspirit.com>`_. Community support is available from the official `Open edX forum <https://discuss.openedx.org>`_.

Do you need help using this template? See the `troubleshooting <https://docs.tutor.edly.io/troubleshooting.html>`__ section from the Tutor documentation.

Contributing
************

Pull requests are welcome! Please read the `"contributing" section from the Tutor documentation <https://docs.tutor.edly.io/tutor.html#contributing>`__.

Unlike other Tutor repositories, you do not need to run ``make changelog-entry``. Instead, simply edit ``CHANGELOG.md`` to note any changes that might affect plugin developers using the cookiecutter.

License
*******

This software is licensed under the terms of the `AGPLv3 <https://www.gnu.org/licenses/agpl-3.0.en.html>`__.
