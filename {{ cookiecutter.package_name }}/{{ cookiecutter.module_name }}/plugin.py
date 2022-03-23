from glob import glob
import os
import pkg_resources

from .__about__ import __version__

templates = pkg_resources.resource_filename(
    "{{ cookiecutter.module_name }}", "templates"
)

config = {
    "defaults": {
        "VERSION": __version__,
    },
}

hooks = {}


def patches():
    all_patches = {}
    patches_dir = pkg_resources.resource_filename(
        "{{ cookiecutter.module_name }}", "patches"
    )
    for path in glob(os.path.join(patches_dir, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
