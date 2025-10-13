"""Fetch user data from the reqres API."""

import os
import requests
import typing as t


def get_api_response(url: str, headers: t.Dict[str, str]) -> t.Dict[str, t.Any]:
    """Get a response from the specified API endpoint."""
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    return response.json()


def main() -> t.List[t.Dict[str, t.Any]]:
    """Main function."""
    # Get your own free API key at https://reqres.in/signup
    api_key = os.environ.get("REQRES_API_KEY")
    if api_key is None:
        raise KeyError("REQRES_API_KEY environment variable not set")

    url = "https://reqres.in/api/users/"

    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    users = get_api_response(url, headers)

    return users["data"]


if __name__ == "__main__":  # pragma: no cover
    main()
