"""
Module providing the FrameworkMwProtocol abstract contract.

This module defines the FrameworkMwProtocol abstract base class which
specifies the interface for registering middleware and exception handlers
on a server adapter. Implementations should apply these settings to the
underlying web framework.
"""

from abc import ABC, abstractmethod
from typing import Any


class FrameworkMwProtocol(ABC):
    """
    Abstract base class defining middleware and exception handler registration.

    Implementations should register middleware callables and exception handlers
    with the web framework so that requests and errors can be processed centrally.
    """

    @abstractmethod
    def add_middlewares(self, middlewares: Any) -> None:
        """
        Register a middleware component with the application.

        Args:
            middlewares: A middleware object or factory accepted by the framework.
            *args, **kwargs: Initialization arguments passed to the middleware.

        Returns:
            None
        """

    @abstractmethod
    def global_middleware(self, middleware: Any) -> None:
        """
        Register or apply a middleware component.

        Args:
            middleware: A middleware callable, class, decorator or factory
                             accepted by the web framework. The exact shape and
                             accepted parameters are framework-specific.

        Returns:
            None
        """

    @abstractmethod
    def trace(self, **kwargs: Any) -> None:
        """
        Register a tracing or instrumentation endpoint.

        Args:
            **kwargs: Additional options for the trace endpoint (middleware, handlers, etc.).

        Returns:
            None
        """

