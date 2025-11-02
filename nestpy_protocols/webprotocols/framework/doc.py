"""
Module providing the FrameworkDocProtocol abstract contract.

This module defines the FrameworkDocProtocol abstract base class which
specifies the interface for configuring server documentation endpoints
and options (OpenAPI, Swagger UI, Redoc) for web adapters.
"""

from typing import Any
from abc import ABC, abstractmethod


class FrameworkDocProtocol(ABC):
    """
    Abstract base class that defines the interface for server documentation
    configuration. Implementations should apply these settings to the web
    framework's documentation tooling (OpenAPI, Swagger UI, Redoc, etc.).
    """

    @abstractmethod
    def set_openapi_url(self, url: str) -> None:
        """
        Set the URL where the generated OpenAPI JSON/YAML specification will be served.

        Args:
            url: The path or full URL to serve the OpenAPI spec from.

        Returns:
            None
        """

    @abstractmethod
    def set_openapi_tags(self, tags: Any) -> None:
        """
        Configure OpenAPI tags metadata.

        Args:
            tags: A list of tag objects as dictionaries, typically containing
                  'name' and 'description' keys used by OpenAPI.

        Returns:
            None
        """

    @abstractmethod
    def set_docs_url(self, url: str) -> None:
        """
        Set the URL where the interactive documentation (e.g., Swagger UI) will be available.

        Args:
            url: The path or full URL for the docs UI.

        Returns:
            None
        """

    @abstractmethod
    def set_redoc_url(self, url: str) -> None:
        """
        Set the URL where ReDoc documentation will be available.

        Args:
            url: The path or full URL for the ReDoc UI.

        Returns:
            None
        """

    @abstractmethod
    def set_swagger_ui_oauth2_redirect_url(self, url: str) -> None:
        """
        Configure the OAuth2 redirect URL used by Swagger UI when performing OAuth flows.

        Args:
            url: The redirect URL for OAuth2 authorization responses.

        Returns:
            None
        """

    @abstractmethod
    def set_swagger_ui_init_oauth(self, config: Any) -> None:
        """
        Provide the initial OAuth configuration for Swagger UI.

        Args:
            config: A configuration object or mapping accepted by Swagger UI's initOAuth.

        Returns:
            None
        """

    @abstractmethod
    def set_swagger_ui_parameters(self, params: Any) -> None:
        """
        Set additional parameters for Swagger UI initialization.

        Args:
            params: Any of Swagger UI parameter names to values.

        Returns:
            None
        """

    @abstractmethod
    def set_swagger_ui_url(self, url: str) -> None:
        """
        Set the URL of the Swagger UI static assets or UI entry point.

        Args:
            url: The path or full URL to the Swagger UI.

        Returns:
            None
        """

    @abstractmethod
    def set_swagger_ui_path(self, path: str) -> None:
        """
        Set the path within the application where Swagger UI should be mounted.

        Args:
            path: The application-relative path for Swagger UI.

        Returns:
            None
        """

    @abstractmethod
    def set_open_api_version(self, version: str) -> None:
        """
        Specify the OpenAPI version to report in the generated spec.

        Args:
            version: A string indicating the OpenAPI version (e.g., '3.0.0').

        Returns:
            None
        """

    @abstractmethod
    def set_api_spec_options(self, spect: Any) -> None:
        """
        Set additional options for the API specification generation.

        Args:
            spect: Any specification options (string keys and values)
                   that may influence generation or metadata.

        Returns:
            None
        """

    @abstractmethod
    def set_openapi_external_docs(self, external_docs: Any) -> None:
        """
        Set external documentation references for the OpenAPI spec.

        Args:
            external_docs: An object or mapping defining external documentation
                           references (e.g., description and URL).

        Returns:
            None
        """

    @abstractmethod
    def set_include_in_schema(self, include: bool) -> None:
        """
        Set whether the documentation endpoints should be included in the OpenAPI schema.

        Args:
            include: A boolean indicating whether to include (True) or exclude (False)
                     the documentation endpoints from the OpenAPI schema.

        Returns:
            None
        """
