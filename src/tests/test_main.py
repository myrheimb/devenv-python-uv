"""Test main.py."""

from pytest import MonkeyPatch
from requests import HTTPError

import app.main as app
import pytest
import typing as t


class DummyResponse:
    """A dummy response object for testing."""

    def __init__(self, payload: t.Dict[str, t.Any], error: HTTPError | None) -> None:
        """Initialize the dummy response."""
        self._payload = payload
        self._error = error

    def raise_for_status(self) -> None:
        """Raise an error if one was set."""
        if self._error:
            raise self._error

    def json(self) -> t.Dict[str, t.Any]:
        """Return the payload."""
        return self._payload


def test_main_requires_api_key(monkeypatch: MonkeyPatch) -> None:
    """Test main function raises KeyError if REQRES_API_KEY is not set."""
    monkeypatch.delenv("REQRES_API_KEY", raising=False)
    with pytest.raises(KeyError):
        app.main()


def test_main_successful_run(monkeypatch: MonkeyPatch) -> None:
    """Test main function with successful API call."""
    monkeypatch.setenv("REQRES_API_KEY", "secret")

    def fake_get(url: str, **kwargs: t.Any) -> DummyResponse:
        """A fake get function to replace requests.get."""
        headers = kwargs.get("headers", {})
        assert url == "https://reqres.in/api/users/"
        assert headers["x-api-key"] == "secret"
        return DummyResponse(payload={"data": [{"id": 1}]}, error=None)

    monkeypatch.setattr(app.requests, "get", fake_get)

    assert app.main() == [{"id": 1}]


def test_get_api_response_http_error(monkeypatch: MonkeyPatch) -> None:
    """Test get_api_response raises HTTPError on bad response."""

    def fake_get(url: str, **kwargs: t.Any) -> DummyResponse:
        """A fake get function to replace requests.get."""
        return DummyResponse(payload={}, error=HTTPError("boom"))

    monkeypatch.setattr(app.requests, "get", fake_get)

    with pytest.raises(HTTPError):
        app.get_api_response("https://fake.url", {"foo": "bar"})
