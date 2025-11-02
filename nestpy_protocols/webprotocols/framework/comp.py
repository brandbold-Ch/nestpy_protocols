"""
Module defining the FrameworkCompProtocol abstract contract.

This module declares the FrameworkCompProtocol abstract base class which
specifies the interface for registering routes, websockets, routers and
global settings on a server adapter. Implementations should apply these
methods to the underlying web framework.
"""

from typing import Union
from abc import ABC, abstractmethod
from typing import List, Any, Dict, Sequence


class FrameworkCompProtocol(ABC):
    """
    Abstract base class that defines the interface for server routing and
    function registration.

    Implementations must provide concrete behavior for adding HTTP routes,
    websocket routes, registering websocket handlers, including router groups,
    tracing endpoints, and setting a global URL prefix.

    """

    @abstractmethod
    def add_router_group(self, name: str, **kwargs: Any) -> None:
        """
        Create or register a router group with the application.

        Args:
            name: Logical name or identifier for the router group.
            **kwargs: Additional options for the add_router_group function.

        Returns:
            None. Implementations should register the router group with the framework.
        """

    @abstractmethod
    def add_route_in_router_group(self, name: str, **kwargs: Any) -> None:
        """
        Add a route to an existing router group.

        Args:
            name: The name or identifier of the target router group.
            **kwargs: Additional framework-specific options for route registration (methods, response model, dependencies, etc.).

        Returns:
            None. Implementations should attach the route to the specified router group.
        """

    @abstractmethod
    def get_router_group(self, router_name: str) -> Any:
        """
        Retrieve a router group by its name.

        Args:
            router_name: The name or identifier of the router group to retrieve.

        Returns:
            A framework-specific router object or None if not found.
        """

    @abstractmethod
    def get_router_groups(self) -> List[Any] | Dict[Any, Any] | Sequence[Any]:
        """
        Return all registered router groups.

        Returns:
            A collection (list, dict, or sequence) of router group objects or metadata
            representing the registered router groups in the application.
        """

    @abstractmethod
    def add_api_route(self, **kwargs: Any) -> None:
        """
        Register an HTTP API route.

        Args:
            **kwargs: Additional framework-specific options (methods, dependencies, response models, etc.).

        Returns:
            None
        """

    @abstractmethod
    def add_api_websocket_route(self, **kwargs: Any) -> None:
        """
        Register a websocket route.

        Args:
            **kwargs: Additional framework-specific websocket options.

        Returns:
            None
        """

    @abstractmethod
    def websocket(self, **kwargs: Any) -> None:
        """
        Decorator-style or direct registration helper for websocket endpoints.

        Args:
            **kwargs: Additional options used when registering the websocket handler.

        Returns:
            None
        """

    @abstractmethod
    def include_router_group(self, **kwargs: Any) -> None:
        """
        Include a router or a group of routes into the application.

        Args:
            **kwargs: Options for mounting the router (prefix, tags, dependencies, etc.).

        Returns:
            None
        """
