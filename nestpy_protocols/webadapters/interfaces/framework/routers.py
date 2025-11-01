"""
Module defining the BaseServerRouter abstract contract.

This module declares the BaseServerRouter abstract base class which
specifies an interface for registering and querying router groups and
their routes. Implementations should manage grouped route registration,
route lookup, and router metadata for the underlying web framework.
"""

from abc import ABC, abstractmethod
from typing import List, Any, Callable, Optional, Dict, Sequence


class FrameworkRoutersProtocol(ABC):
    """
    Abstract base class that defines the interface for router group management.

    Implementations must provide concrete behavior to create router groups,
    add routes into those groups, and retrieve router group references or
    collections for inspection or further configuration.
    """

    @abstractmethod
    def add_router_group(
        self,
        prefix: str,
        name: str,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        dependencies: Optional[List[Any]] = None,
        include_in_schema: Optional[bool] = True
    ) -> None:
        """
        Create or register a router group with the application.

        Args:
            prefix: URL prefix applied to all routes in the group (e.g., '/users').
            name: Logical name or identifier for the router group.
            description: Optional human-readable description of the group.
            tags: Optional list of tags for documentation or grouping.
            dependencies: Optional list of dependency providers applied to the group.
            include_in_schema: Whether routes in this group should be included in generated API schemas.

        Returns:
            None. Implementations should register the router group with the framework.
        """
        ...

    @abstractmethod
    def add_route_in_router_group(self, name: str, path: str, endpoint: Callable[..., Any], **kwargs: Any) -> None:
        """
        Add a route to an existing router group.

        Args:
            name: The name or identifier of the target router group.
            path: The route path relative to the group's prefix (e.g., '/items').
            endpoint: A callable that will handle requests to the route.
            **kwargs: Additional framework-specific options for route registration (methods, response model, dependencies, etc.).

        Returns:
            None. Implementations should attach the route to the specified router group.
        """
        ...

    @abstractmethod
    def get_router_group(self, router_name: str) -> Any:
        """
        Retrieve a router group by its name.

        Args:
            router_name: The name or identifier of the router group to retrieve.

        Returns:
            A framework-specific router object or None if not found.
        """
        ...

    @abstractmethod
    def get_router_groups(self) -> List[Any] | Dict[Any, Any] | Sequence[Any]:
        """
        Return all registered router groups.

        Returns:
            A collection (list, dict, or sequence) of router group objects or metadata
            representing the registered router groups in the application.
        """
        ...