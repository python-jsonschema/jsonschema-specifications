.. include:: ../README.rst

Resources are exposed via a `referencing.Registry`.

The purpose of this package is to provide these schemas via an explicit public API.
In other words, if you're authoring schemas, or building JSON Schema tooling, or otherwise need access to the JSON Schema official metaschemas and vocabularies, they're exposed here for runtime use in a way that doesn't require you to copy them, or to reach into the data files of a Python package you didn't necessarily author.

Usage
-----

There is essentially one main object provided, `jsonschema_specifications.REGISTRY`, which is a `referencing.Registry` (or more specifically a `referencing.jsonschema.SchemaRegistry`) containing all of the "official" JSON Schemas.

For full details on using it, see the `referencing documentation <referencing:intro>`, but for example:

.. code::

    from jsonschema_specifications import REGISTRY as SPECIFICATIONS

    DRAFT202012_DIALECT_URI = "https://json-schema.org/draft/2020-12/schema"
    print(SPECIFICATIONS.contents(DRAFT202012_DIALECT_URI))

    # -> prints the Draft 2020-12 meta-schema


Contents
--------

.. toctree::
    :glob:
    :maxdepth: 2

    api
