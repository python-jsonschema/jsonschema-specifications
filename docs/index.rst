.. include:: ../README.rst

Resources are exposed via a `referencing.Registry`.

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
