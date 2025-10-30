"""
Module defining the AbstractWebServer contract.

This module declares the AbstractWebServer abstract base class which
specifies composition methods to attach various server contract objects
(such as params, functions, events, routers, middlewares and docs) to
a web server adapter implementation.
"""

from abc import ABC, abstractmethod
from nestpy_protocols.webadapters.contracts import (
    BaseServerDocs,
    BaseServerParams,
    BaseServerRouter,
    BaseServerMiddlewares,
    BaseServerFunctions,
    BaseServerEvents,
)


class AbstractWebServer(ABC):
    """
    Abstract base class that groups methods for attaching server contracts.

    Implementations should accept instances of the specific contract interfaces
    and return them (optionally wrapped or configured) so callers can continue
    composing or inspecting the configured contract objects.
    """

    @abstractmethod
    def server_params(self, params: BaseServerParams) -> BaseServerParams:
        """
        Attach or configure server parameters.

        Args:
            params: An instance implementing BaseServerParams representing server-level configuration and metadata.

        Returns:
            The configured BaseServerParams instance (may be the same object or an adapter/wrapper).
        """
        ...

    @abstractmethod
    def server_functions(self, functions: BaseServerFunctions) -> BaseServerFunctions:
        """
        Attach or configure server functions (route/websocket registration helpers).

        Args:
            functions: An instance implementing BaseServerFunctions to register routes and handlers.

        Returns:
            The configured BaseServerFunctions instance.
        """
        ...

    @abstractmethod
    def server_events(self, events: BaseServerEvents) -> BaseServerEvents:
        """
        Attach or configure server lifecycle and event handlers.

        Args:
            events: An instance implementing BaseServerEvents for startup/shutdown and event hooks.

        Returns:
            The configured BaseServerEvents instance.
        """
        ...

    @abstractmethod
    def server_router(self, routers: BaseServerRouter) -> BaseServerRouter:
        """
        Attach or configure router groups and route management.

        Args:
            routers: An instance implementing BaseServerRouter to manage grouped routes.

        Returns:
            The configured BaseServerRouter instance.
        """
        ...

    @abstractmethod
    def server_middlewares(self, middlewares: BaseServerMiddlewares) -> BaseServerMiddlewares:
        """
        Attach or configure middleware and exception handlers.

        Args:
            middlewares: An instance implementing BaseServerMiddlewares to register middleware and handlers.

        Returns:
            The configured BaseServerMiddlewares instance.
        """
        ...

    @abstractmethod
    def server_docs(self, docs: BaseServerDocs) -> BaseServerDocs:
        """
        Attach or configure documentation (OpenAPI/Swagger) related settings.

        Args:
            docs: An instance implementing BaseServerDocs to configure API documentation.

        Returns:
            The configured BaseServerDocs instance.
        """
        ...