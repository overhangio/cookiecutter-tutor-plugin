Tutor plugin cookiecutter 🍪
============================

This is a `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/tutorial2.html>`__ for getting started with `Tutor plugins <https://docs.tutor.overhang.io/plugins.html>`__. It will generate a base scaffold for an empty tutor plugin that does, well, nothing.

Requirements
------------

::

    pip install cookiecutter

Usage
-----

::

    cookiecutter https://github.com/overhangio/cookiecutter-tutor-plugin.git

Once you have generated your plugin, you can start using it right away (even if it won't do anything)::
 
    pip install -e ./tutor-myplugin
    tutor plugins list # your plugin should appear here
    tutor plugins enable myplugin # hack at it!

License
-------

This software is licensed under the terms of the `AGPLv3 <https://www.gnu.org/licenses/agpl-3.0.en.html>`__.
