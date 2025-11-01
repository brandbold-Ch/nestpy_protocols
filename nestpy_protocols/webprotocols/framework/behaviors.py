"""
Module defining the FrameworkBehaviorsProtocol abstract contract.

This module declares the FrameworkBehaviorsProtocol abstract base class which
specifies the interface for registering routes, websockets, routers and
global settings on a server adapter. Implementations should apply these
methods to the underlying web framework.
"""

from typing import Any, Callable, Union
from abc import ABC, abstractmethod


class FrameworkBehaviorsProtocol(ABC):
    """
    Abstract base class that defines the interface for server routing and
    function registration.

    Implementations must provide concrete behavior for adding HTTP routes,
    websocket routes, registering websocket handlers, including router groups,
    tracing endpoints, and setting a global URL prefix.
    """

    @abstractmethod
    def add_api_route(self, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        """
        Register an HTTP API route.

        Args:
            path: The URL path where the endpoint will be mounted (for example, '/items').
            endpoint: A callable that will handle requests to the route.
            **kwargs: Additional framework-specific options (methods, dependencies, response models, etc.).

        Returns:
            None
        """

    @abstractmethod
    def add_api_websocket_route(self, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        """
        Register a websocket route.

        Args:
            path: The URL path for the websocket endpoint.
            endpoint: A callable that will handle websocket connections.
            **kwargs: Additional framework-specific websocket options.

        Returns:
            None
        """

    @abstractmethod
    def websocket(self, path: str, **kwargs: Any) -> None:
        """
        Decorator-style or direct registration helper for websocket endpoints.

        Args:
            path: The URL path for the websocket.
            **kwargs: Additional options used when registering the websocket handler.

        Returns:
            None
        """

    @abstractmethod
    def include_router_group(self, router: Any, **kwargs: Any) -> None:
        """
        Include a router or a group of routes into the application.

        Args:
            router: A router object (framework-specific) containing multiple routes.
            **kwargs: Options for mounting the router (prefix, tags, dependencies, etc.).

        Returns:
            None
        """

    @abstractmethod
    def trace(self, path: str, **kwargs: Any) -> None:
        """
        Register a tracing or instrumentation endpoint.

        Args:
            path: The URL path to attach tracing or profiling handlers.
            **kwargs: Additional options for the trace endpoint (middleware, handlers, etc.).

        Returns:
            None
        """

    @abstractmethod
    def set_global_url_prefix(self, prefix: str) -> None:
        """
        Set a global URL prefix applied to all registered routes.

        Args:
            prefix: A string prefix (for example, '/api/v1') to be prepended to all routes.

        Returns:
            None
        """

    @abstractmethod
    def stop_server(self) -> None:
        """
        Stop the server

        Returns:
            None
        """

    @abstractmethod
    def start_server(self, host: str, port: Union[str, int]) -> None:
        """
        Start the server listening on the specified host and port.

        Args:
            host: The hostname or IP address to bind the server to (e.g., '0.0.0.0').
            port: The port number or port string to bind to (e.g., 8000 or '8000').

        Returns:
            None. Implementations should start the server event loop or bind sockets
            so the application begins accepting connections.
        """
