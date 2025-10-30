"""
Module defining the BaseServerEvents abstract contract.

This module declares the BaseServerEvents abstract base class which
specifies an interface for handling server-side events. Implementations
should handle event routing, processing, and any necessary side effects.
"""

from abc import ABC, abstractmethod


class BaseServerEvents(ABC):
    """
    Abstract base class that defines the interface for server event handling.

    Implementations must provide a concrete `on_event` method to react to
    named events emitted by the application or external systems.
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
        ...
