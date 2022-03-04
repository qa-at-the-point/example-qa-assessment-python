import pytest
import requests
import veriff as api

VALID_SESSION_TESTS = [
    ("Carlos Kidman", "en", "US", api.DocumentType.DRIVERS_LICENSE),
    ("张 Zhāng", "ch", "CH", api.DocumentType.PASSPORT),
    ("Nico", "bg", "BG", api.DocumentType.ID_CARD),
    # ... add more examples including what we've documented in veriff.feature
]


@pytest.mark.parametrize("session", VALID_SESSION_TESTS)
def test_create_session(session):
    token = api.create_session(*session)
    assert token is not None and len(token) > 0


@pytest.mark.parametrize("session", VALID_SESSION_TESTS)
def test_get_session_config(session):
    token = api.create_session(*session)
    config = api.get_session_config(token)
    assert config.get("status") == "created"


LOCALE_TESTS = [
    ("en", "Passport"),
    ("bg", "Паспорт"),
    # more examples, but we could check the entire JSON object instead of a single field
]


@pytest.mark.parametrize("language, expected", LOCALE_TESTS)
def test_get_locales(language, expected):
    response = requests.get(f"https://magic.saas-3.veriff.me/static/locales/{language}-1qv6wh069s.json")
    json = response.json()
    assert json.get("vrff.PASSPORT") == expected
