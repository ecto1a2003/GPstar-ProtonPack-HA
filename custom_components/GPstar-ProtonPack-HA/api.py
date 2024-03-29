"""Sample API Client."""
from __future__ import annotations

import asyncio
import socket

import aiohttp
import async_timeout


class IntegrationBlueprintApiClientError(Exception):
    """Exception to indicate a general API error."""


class IntegrationBlueprintApiClientCommunicationError(
    IntegrationBlueprintApiClientError
):
    """Exception to indicate a communication error."""


class IntegrationBlueprintApiClientAuthenticationError(
    IntegrationBlueprintApiClientError
):
    """Exception to indicate an authentication error."""


class IntegrationBlueprintApiClient:
    """Sample API Client."""

    def __init__(
        self,
        url: str,
        username: str,
        password: str,
        session: aiohttp.ClientSession,
    ) -> None:
        """Sample API Client."""
        self._username = username
        self._password = password
        self._session = session
        self.url = url
        print("api url " +self.url)
    async def async_get_data(self) -> any:
        """Get data from the API."""
        return await self._api_wrapper(
            # method="get", url="https://jsonplaceholder.typicode.com/posts/1"
            method="get",
            #url="https://jsonplaceholder.typicode.com/posts/1",
            #url="http://192.168.50.10/status",
            url=self.url
            #headers={"Content-type": "application/json; charset=UTF-8"},
        )
    #async def async_set_title(self, value: str) -> any:
    async def async_set_title(self) -> any:
        """put data to the API."""
        return await self._api_wrapper(
            method="put",
            #url="https://jsonplaceholder.typicode.com/posts/1",
            url="http://192.168.50.10/pack/on",
            #data={"mode": value},
            #headers={"Content-type": "application/json; charset=UTF-8"},
        )

    async def _api_wrapper(
        self,
        method: str,
        url: str,
        data: dict | None = None,
        headers: dict | None = None,
    ) -> any:
        """Get information from the API."""
        try:
            async with async_timeout.timeout(10):
                response = await self._session.request(
                    method=method,
                    url=url,
                    headers=headers,
                    json=data,
                )
                if response.status in (401, 403):
                    raise IntegrationBlueprintApiClientAuthenticationError(
                        "Invalid credentials",
                    )
                response.raise_for_status()
                print( await response.json())
                return await response.json()

        except asyncio.TimeoutError as exception:
            raise IntegrationBlueprintApiClientCommunicationError(
                "Timeout error fetching information",
            ) from exception
        except (aiohttp.ClientError, socket.gaierror) as exception:
            raise IntegrationBlueprintApiClientCommunicationError(
                "Error fetching information",
            ) from exception
        except Exception as exception:  # pylint: disable=broad-except
            raise IntegrationBlueprintApiClientError(
                "Something really wrong happened!"
            ) from exception
