Migrating from v0 plugins
#########################

The plugin API was upgraded from ``v0`` to ``v1`` in `Tutor v13.2.0 <https://github.com/overhangio/tutor/releases/tag/v13.2.0>`__. This cookiecutter generates plugin scaffolds for ``v1``. The ``v0`` API will be supported for some time, but you are encouraged to upgrade your plugins. To upgrade a ``v0`` plugin that was generated previously with this cookiecutter, perform the following steps:

- Replace ``tutor.plugin.v0`` by ``tutor.plugin.v1`` inside ``setup.py``.

- Rename the ``hooks`` folder to ``tasks`` inside templates folder.

- In ``plugin.py``:

  - At the top of the file, add the following line:

    .. code-block:: python

        from tutor import hooks

  - Modify the ``config`` object:

    - If present, replace the ``add`` key by ``unique``.
    - If present, replace the ``set`` key by ``overrides``.

  - Delete the ``templates`` object.

  - Replace the ``hooks`` object:

    - Declare a ``MY_INIT_TASKS`` variable:

        .. code-block:: python

            MY_INIT_TASKS = []

    - If present, replace each ``myservice`` item in ``init`` by:

        .. code-block:: python

            MY_INIT_TASKS.append((
                "myservice",
                ("yourplugin", "tasks", "myservice", "init"),
                10,  # default task priority
            ))

    - If present, replace each ``myservice`` item in ``pre-init`` by:

        .. code-block:: python

            MY_INIT_TASKS.append((
                "myservice",
                ("yourplugin", "tasks", "myservice", "pre-init"),
                1,  # high task priority (for pre-initialization)
            ))

    - If present, replace each ``"myimage": "myimage:latest"`` key/value in ``build-image`` by:

        .. code-block:: python

            hooks.Filters.IMAGES_BUILD.add_item((
                "myimage",
                ("plugins", "yourplugin", "build", "myimage"),
                "myimage:latest",
                (),
            ))

    - If present, replace each ``"myimage": "myimage:latest"`` key/value in ``remote-image`` by:

        .. code-block:: python

            hooks.Filters.IMAGES_PULL.add_item((
                "myimage",
                "myimage:latest",
            ))
            hooks.Filters.IMAGES_PUSH.add_item((
                "myimage",
                "myimage:latest",
            ))

  - Delete the ``patches`` function.

  - Add the following piece of code at the bottom of your file:

    .. code-block:: python

        ####### Boilerplate code
        # Add the "templates" folder as a template root
        hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
            str(importlib_resources.files("tutoryourplugin") / "templates")
        )
        # Render the "build" and "apps" folders
        hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
            [
                ("yourplugin/build", "plugins"),
                ("yourplugin/apps", "plugins"),
            ],
        )
        # Load patches from files
        for path in glob(
            str(importlib_resources.files("tutoryourplugin") / "patches" / "*")
        ):
            with open(path, encoding="utf-8") as patch_file:
                hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))
        # Add configuration entries
        hooks.Filters.CONFIG_DEFAULTS.add_items(
            [
                (f"YOUR_PLUGIN_{key}", value)
                for key, value in config.get("defaults", {}).items()
            ]
        )
        hooks.Filters.CONFIG_UNIQUE.add_items(
            [
                (f"YOUR_PLUGIN_{key}", value)
                for key, value in config.get("unique", {}).items()
            ]
        )
        hooks.Filters.CONFIG_OVERRIDES.add_items(list(config.get("overrides", {}).items()))
        # For each task added to MY_INIT_TASKS, load the task template and add it to the
        # CLI_DO_INIT_TASKS filter, which tells Tutor to run it as part of the `init` job.
        for service, template_path, priority in MY_INIT_TASKS:
            full_path: str = str(importlib_resources.files(
                "tutoryourplugin") / os.path.join("templates", *template_path)
            )
            with open(full_path, encoding="utf-8") as init_task_file:
                init_task: str = init_task_file.read()
            hooks.Filters.CLI_DO_INIT_TASKS.add_item((service, init_task), priority=priority)


  - In case the plugin has custom commands to be available from CLI, you will need to implement the ``CLI_COMMANDS`` filter according
    to `Tutor's reference documentation <https://docs.tutor.edly.io/reference/api/hooks/consts.html#tutor.hooks.Filters.CLI_COMMANDS>`__.
    You can implement this filter by adding the following code line to ``plugin.py``:

    .. code-block:: python

        tutor_hooks.Filters.CLI_COMMANDS.add_item(command)

  - Also, you will either need to rename the command function or use click's ``name=<plugin>`` argument.
    For example, to ensure your plugin command(s) are available under ``tutor xqueue ...``, you could write:

    .. code-block:: python

        @click.group(help="Interact with the Xqueue server", name="xqueue")
        def command():
              ...

  - Verify that the file contains no instance of ``yourplugin`` or ``YOUR_PLUGIN``. If it does, replace with your plugin name.

- Re-install your plugin.

- Verify that the plugin is listed when you run ``tutor plugins list``.
