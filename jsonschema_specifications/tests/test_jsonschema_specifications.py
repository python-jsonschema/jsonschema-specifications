from jsonschema_specifications import REGISTRY


def test_it_contains_metaschemas():
    schema = REGISTRY.contents("http://json-schema.org/draft-07/schema#")
    assert schema["$id"] == "http://json-schema.org/draft-07/schema#"
    assert schema["title"] == "Core schema meta-schema"
