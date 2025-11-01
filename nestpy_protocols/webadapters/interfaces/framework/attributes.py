"""
Module defining the BaseServerParams abstract contract.

This module declares the BaseServerParams abstract base class which
specifies the interface for configuring server-level parameters and
metadata (OpenAPI/Swagger info, middleware, lifecycle, responses, etc.).
Implementations should apply these settings to the underlying web framework.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Type, Callable, Union


class FrameworkAttributesProtocol(ABC):
    """
    Abstract base class that defines the interface for server metadata and
    configuration parameters.

    Implementations must provide concrete behavior to apply contact/license
    information, server options, middleware registration, response defaults,
    and other global settings used by the application and API documentation.
    """

    @abstractmethod
    def set_contact(self, contact: Union[Dict[str, Any], str, None]) -> None:
        """
        Set the contact information for the API.

        Args:
            contact: A mapping with contact details (for example keys like 'name',
                     'email', 'url'), a string, or None to clear contact info.

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_license(self, license_info: Union[Dict[str, Any], str, None]) -> None:
        """
        Set the license information for the API.

        Args:
            license_info: A mapping describing the license (for example 'name' and
                          'identifier'/'url'), a string, or None to clear license info.

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_license_url(self, license_url: str) -> None:
        """
        Set the URL pointing to the API license text.

        Args:
            license_url: A string URL referencing the license document.

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_media_type(self, media_type: str) -> None:
        """
        Set the default media type used by the API (e.g., 'application/json').

        Args:
            media_type: The default response/request content type.

        Returns:
            None
        """
        ...

    @abstractmethod
    def add_middleware(self, middleware_class: Type[Callable], *args, **kwargs) -> None:
        """
        Register a middleware component with the application.

        Args:
            middleware_class: A middleware class or factory accepted by the framework.
            *args, **kwargs: Initialization arguments passed to the middleware.

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_title(self, title: str) -> None:
        """
        Set the API or application title.

        Args:
            title: A short, human-readable title for the API.

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_summary(self, summary: str) -> None:
        """
        Set a short summary for the API.

        Args:
            summary: A brief one-line summary describing the API.

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_description(self, description: str) -> None:
        """
        Set a detailed description for the API.

        Args:
            description: A longer description of the API and its purpose.

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_version(self, version: str) -> None:
        """
        Set the API version string.

        Args:
            version: The semantic version or identifier for the API (e.g., '1.0.0').

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_terms_of_service(self, terms: str) -> None:
        """
        Set the terms of service text or URL for the API.

        Args:
            terms: A string containing terms of service or a URL pointing to them.

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_servers(self, servers: List[Dict[str, Any]]) -> None:
        """
        Configure a list of servers/environments for the API documentation.

        Args:
            servers: A list of server description mappings (each typically includes 'url' and 'description').

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_root_path_in_servers(self, enabled: bool) -> None:
        """
        Enable or disable inclusion of the application's root path in server entries.

        Args:
            enabled: Boolean flag indicating whether to include root_path in servers.

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_separate_input_output_schemas(self, enabled: bool) -> None:
        """
        Toggle whether input and output schemas are generated as separate definitions.

        Args:
            enabled: Boolean flag to separate input and output schemas in generated docs.

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_default_response_class(self, response_class: Any) -> None:
        """
        Set the default response class/type used by the framework.

        Args:
            response_class: A response class or factory used to build HTTP responses.

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_callbacks(self, callbacks: List[Any]) -> None:
        """
        Register callback handlers (e.g., async callbacks or background tasks).

        Args:
            callbacks: A list of callback definitions accepted by the framework or docs generator.

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_webhooks(self, webhooks: Any) -> None:
        """
        Configure webhook endpoints or definitions.

        Args:
            webhooks: Webhook definitions or a structure used by the framework/docs.

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_responses(self, responses: Dict[Any, Dict[str, Any]]) -> None:
        """
        Define default or global response schemas for operations.

        Args:
            responses: A mapping where keys are status codes or names and values are response schema dictionaries.

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_extra(self, **extra: Any) -> None:
        """
        Set arbitrary extra metadata to be included in the API specification.

        Args:
            **extra: Keyword metadata items that will be attached to the API info or spec.

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_lifespan(self, lifespan: Any) -> None:
        """
        Configure application lifespan handling (startup/shutdown hooks).

        Args:
            lifespan: A lifespan manager, context manager, or callable used to control app lifecycle.

        Returns:
            None
        """
        ...