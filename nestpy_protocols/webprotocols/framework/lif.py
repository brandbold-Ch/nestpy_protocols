from abc import ABC, abstractmethod
from typing import Any, Union


class FrameworkLifProtocol(ABC):
    """
    Abstract base class that defines the interface for framework lifecycle events.

    Implementations must provide concrete methods to handle startup and shutdown
    events of the application framework.
    """

    @abstractmethod
    def on_event(self, event_type: str) -> None:
        """
        Handle an event identified by its type.

        Args:
            event_type: A string identifier for the event to handle (for example,
                        'user.created', 'order.placed', etc.).

        Returns:
            None. Implementations should process the event and perform any side
            effects (logging, state changes, notifications) as required.
        """

    @abstractmethod
    def set_on_startup(self, handlers: Any) -> None:
        """
        Set startup event handlers for the documentation routes.

        Args:
            handlers: A list of callables to be executed on application startup.

        Returns:
            None
        """

    @abstractmethod
    def set_on_shutdown(self, handlers: Any) -> None:
        """
        Set shutdown event handlers for the documentation routes.

        Args:
            handlers: A list of callables to be executed on application shutdown.

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
