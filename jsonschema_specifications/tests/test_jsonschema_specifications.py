import jsonschema_specifications


def test_it_contains_metaschemas():
    resource, _, _ = jsonschema_specifications.REGISTRY.resource_at(
        "http://json-schema.org/draft-07/schema#",
    )
    schema = resource.resource
    assert schema["$id"] == "http://json-schema.org/draft-07/schema#"
    assert schema["title"] == "Core schema meta-schema"
