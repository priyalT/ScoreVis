import pytest
from hypothesis import given, strategies as st
import json

def serialize_to_json(data: dict) -> str:
    return json.dumps(data)
def deserialize_to_json(json_str: str) -> dict:
    return json.loads(json_str)

@given(st.dictionaries(keys=st.text(), values=st.integers() | st.booleans() | st.text()))
def test_round_trip_serialization(metadata):
    """Test to see whether JSON metadata round-trip preserves structure"""
    serialized_strings = serialize_to_json(metadata)
    dict_unserialized = deserialize_to_json(serialized_strings)
    assert dict_unserialized == metadata