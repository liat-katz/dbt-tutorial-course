"""Generated client library for appengine version v1alpha."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.appengine.v1alpha import appengine_v1alpha_messages as messages


class AppengineV1alpha(base_api.BaseApiClient):
  """Generated client library for service appengine version v1alpha."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://appengine.googleapis.com/'
  MTLS_BASE_URL = 'https://appengine.mtls.googleapis.com/'

  _PACKAGE = 'appengine'
  _SCOPES = ['https://www.googleapis.com/auth/appengine.admin', 'https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/cloud-platform.read-only']
  _VERSION = 'v1alpha'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'AppengineV1alpha'
  _URL_VERSION = 'v1alpha'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new appengine handle."""
    url = url or self.BASE_URL
    super(AppengineV1alpha, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.apps_authorizedCertificates = self.AppsAuthorizedCertificatesService(self)
    self.apps_authorizedDomains = self.AppsAuthorizedDomainsService(self)
    self.apps_domainMappings = self.AppsDomainMappingsService(self)
    self.apps_locations = self.AppsLocationsService(self)
    self.apps_operations = self.AppsOperationsService(self)
    self.apps_services_migration = self.AppsServicesMigrationService(self)
    self.apps_services = self.AppsServicesService(self)
    self.apps = self.AppsService(self)
    self.projects_locations_applications_authorizedDomains = self.ProjectsLocationsApplicationsAuthorizedDomainsService(self)
    self.projects_locations_applications_services_migration = self.ProjectsLocationsApplicationsServicesMigrationService(self)
    self.projects_locations_applications_services = self.ProjectsLocationsApplicationsServicesService(self)
    self.projects_locations_applications = self.ProjectsLocationsApplicationsService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class AppsAuthorizedCertificatesService(base_api.BaseApiService):
    """Service class for the apps_authorizedCertificates resource."""

    _NAME = 'apps_authorizedCertificates'

    def __init__(self, client):
      super(AppengineV1alpha.AppsAuthorizedCertificatesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Uploads the specified SSL certificate.

      Args:
        request: (AppengineAppsAuthorizedCertificatesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AuthorizedCertificate) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/authorizedCertificates',
        http_method='POST',
        method_id='appengine.apps.authorizedCertificates.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha/{+parent}/authorizedCertificates',
        request_field='authorizedCertificate',
        request_type_name='AppengineAppsAuthorizedCertificatesCreateRequest',
        response_type_name='AuthorizedCertificate',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes the specified SSL certificate.

      Args:
        request: (AppengineAppsAuthorizedCertificatesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/authorizedCertificates/{authorizedCertificatesId}',
        http_method='DELETE',
        method_id='appengine.apps.authorizedCertificates.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='AppengineAppsAuthorizedCertificatesDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the specified SSL certificate.

      Args:
        request: (AppengineAppsAuthorizedCertificatesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AuthorizedCertificate) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/authorizedCertificates/{authorizedCertificatesId}',
        http_method='GET',
        method_id='appengine.apps.authorizedCertificates.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['view'],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='AppengineAppsAuthorizedCertificatesGetRequest',
        response_type_name='AuthorizedCertificate',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all SSL certificates the user is authorized to administer.

      Args:
        request: (AppengineAppsAuthorizedCertificatesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAuthorizedCertificatesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/authorizedCertificates',
        http_method='GET',
        method_id='appengine.apps.authorizedCertificates.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken', 'view'],
        relative_path='v1alpha/{+parent}/authorizedCertificates',
        request_field='',
        request_type_name='AppengineAppsAuthorizedCertificatesListRequest',
        response_type_name='ListAuthorizedCertificatesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the specified SSL certificate. To renew a certificate and maintain its existing domain mappings, update certificate_data with a new certificate. The new certificate must be applicable to the same domains as the original certificate. The certificate display_name may also be updated.

      Args:
        request: (AppengineAppsAuthorizedCertificatesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AuthorizedCertificate) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/authorizedCertificates/{authorizedCertificatesId}',
        http_method='PATCH',
        method_id='appengine.apps.authorizedCertificates.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1alpha/{+name}',
        request_field='authorizedCertificate',
        request_type_name='AppengineAppsAuthorizedCertificatesPatchRequest',
        response_type_name='AuthorizedCertificate',
        supports_download=False,
    )

  class AppsAuthorizedDomainsService(base_api.BaseApiService):
    """Service class for the apps_authorizedDomains resource."""

    _NAME = 'apps_authorizedDomains'

    def __init__(self, client):
      super(AppengineV1alpha.AppsAuthorizedDomainsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists all domains the user is authorized to administer.

      Args:
        request: (AppengineAppsAuthorizedDomainsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAuthorizedDomainsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/authorizedDomains',
        http_method='GET',
        method_id='appengine.apps.authorizedDomains.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/authorizedDomains',
        request_field='',
        request_type_name='AppengineAppsAuthorizedDomainsListRequest',
        response_type_name='ListAuthorizedDomainsResponse',
        supports_download=False,
    )

  class AppsDomainMappingsService(base_api.BaseApiService):
    """Service class for the apps_domainMappings resource."""

    _NAME = 'apps_domainMappings'

    def __init__(self, client):
      super(AppengineV1alpha.AppsDomainMappingsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Maps a domain to an application. A user must be authorized to administer a domain in order to map it to an application. For a list of available authorized domains, see AuthorizedDomains.ListAuthorizedDomains.

      Args:
        request: (AppengineAppsDomainMappingsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/domainMappings',
        http_method='POST',
        method_id='appengine.apps.domainMappings.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['noManagedCertificate', 'overrideStrategy'],
        relative_path='v1alpha/{+parent}/domainMappings',
        request_field='domainMapping',
        request_type_name='AppengineAppsDomainMappingsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes the specified domain mapping. A user must be authorized to administer the associated domain in order to delete a DomainMapping resource.

      Args:
        request: (AppengineAppsDomainMappingsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/domainMappings/{domainMappingsId}',
        http_method='DELETE',
        method_id='appengine.apps.domainMappings.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='AppengineAppsDomainMappingsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the specified domain mapping.

      Args:
        request: (AppengineAppsDomainMappingsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DomainMapping) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/domainMappings/{domainMappingsId}',
        http_method='GET',
        method_id='appengine.apps.domainMappings.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='AppengineAppsDomainMappingsGetRequest',
        response_type_name='DomainMapping',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists the domain mappings on an application.

      Args:
        request: (AppengineAppsDomainMappingsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDomainMappingsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/domainMappings',
        http_method='GET',
        method_id='appengine.apps.domainMappings.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/domainMappings',
        request_field='',
        request_type_name='AppengineAppsDomainMappingsListRequest',
        response_type_name='ListDomainMappingsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the specified domain mapping. To map an SSL certificate to a domain mapping, update certificate_id to point to an AuthorizedCertificate resource. A user must be authorized to administer the associated domain in order to update a DomainMapping resource.

      Args:
        request: (AppengineAppsDomainMappingsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/domainMappings/{domainMappingsId}',
        http_method='PATCH',
        method_id='appengine.apps.domainMappings.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['noManagedCertificate', 'updateMask'],
        relative_path='v1alpha/{+name}',
        request_field='domainMapping',
        request_type_name='AppengineAppsDomainMappingsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class AppsLocationsService(base_api.BaseApiService):
    """Service class for the apps_locations resource."""

    _NAME = 'apps_locations'

    def __init__(self, client):
      super(AppengineV1alpha.AppsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (AppengineAppsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/locations/{locationsId}',
        http_method='GET',
        method_id='appengine.apps.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='AppengineAppsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (AppengineAppsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/locations',
        http_method='GET',
        method_id='appengine.apps.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+name}/locations',
        request_field='',
        request_type_name='AppengineAppsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class AppsOperationsService(base_api.BaseApiService):
    """Service class for the apps_operations resource."""

    _NAME = 'apps_operations'

    def __init__(self, client):
      super(AppengineV1alpha.AppsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (AppengineAppsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/operations/{operationsId}',
        http_method='GET',
        method_id='appengine.apps.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='AppengineAppsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns UNIMPLEMENTED.

      Args:
        request: (AppengineAppsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/operations',
        http_method='GET',
        method_id='appengine.apps.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+name}/operations',
        request_field='',
        request_type_name='AppengineAppsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class AppsServicesMigrationService(base_api.BaseApiService):
    """Service class for the apps_services_migration resource."""

    _NAME = 'apps_services_migration'

    def __init__(self, client):
      super(AppengineV1alpha.AppsServicesMigrationService, self).__init__(client)
      self._upload_configs = {
          }

    def CheckGen1appId(self, request, global_params=None):
      r"""rpc to check if a given app_id exists in App Engine Gen1.

      Args:
        request: (AppengineAppsServicesMigrationCheckGen1appIdRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CheckGen1AppIdResponse) The response message.
      """
      config = self.GetMethodConfig('CheckGen1appId')
      return self._RunMethod(
          config, request, global_params=global_params)

    CheckGen1appId.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/services/{servicesId}/migration/checkGen1appId',
        http_method='POST',
        method_id='appengine.apps.services.migration.checkGen1appId',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}/migration/checkGen1appId',
        request_field='checkGen1AppIdRequest',
        request_type_name='AppengineAppsServicesMigrationCheckGen1appIdRequest',
        response_type_name='CheckGen1AppIdResponse',
        supports_download=False,
    )

    def MigrateCodeFile(self, request, global_params=None):
      r"""rpc to migrate a code file. Eg. app.py.

      Args:
        request: (AppengineAppsServicesMigrationMigrateCodeFileRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('MigrateCodeFile')
      return self._RunMethod(
          config, request, global_params=global_params)

    MigrateCodeFile.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/services/{servicesId}/migration/migrateCodeFile',
        http_method='POST',
        method_id='appengine.apps.services.migration.migrateCodeFile',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}/migration/migrateCodeFile',
        request_field='migrateCodeFileRequest',
        request_type_name='AppengineAppsServicesMigrationMigrateCodeFileRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def MigrateConfigYaml(self, request, global_params=None):
      r"""rpc to migrate the config yaml file eg. app.yaml.

      Args:
        request: (AppengineAppsServicesMigrationMigrateConfigYamlRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (MigrateConfigYamlResponse) The response message.
      """
      config = self.GetMethodConfig('MigrateConfigYaml')
      return self._RunMethod(
          config, request, global_params=global_params)

    MigrateConfigYaml.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/apps/{appsId}/services/{servicesId}/migration/migrateConfigYaml',
        http_method='POST',
        method_id='appengine.apps.services.migration.migrateConfigYaml',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}/migration/migrateConfigYaml',
        request_field='migrateConfigYamlRequest',
        request_type_name='AppengineAppsServicesMigrationMigrateConfigYamlRequest',
        response_type_name='MigrateConfigYamlResponse',
        supports_download=False,
    )

  class AppsServicesService(base_api.BaseApiService):
    """Service class for the apps_services resource."""

    _NAME = 'apps_services'

    def __init__(self, client):
      super(AppengineV1alpha.AppsServicesService, self).__init__(client)
      self._upload_configs = {
          }

  class AppsService(base_api.BaseApiService):
    """Service class for the apps resource."""

    _NAME = 'apps'

    def __init__(self, client):
      super(AppengineV1alpha.AppsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationsApplicationsAuthorizedDomainsService(base_api.BaseApiService):
    """Service class for the projects_locations_applications_authorizedDomains resource."""

    _NAME = 'projects_locations_applications_authorizedDomains'

    def __init__(self, client):
      super(AppengineV1alpha.ProjectsLocationsApplicationsAuthorizedDomainsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists all domains the user is authorized to administer.

      Args:
        request: (AppengineProjectsLocationsApplicationsAuthorizedDomainsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAuthorizedDomainsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/applications/{applicationsId}/authorizedDomains',
        http_method='GET',
        method_id='appengine.projects.locations.applications.authorizedDomains.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/authorizedDomains',
        request_field='',
        request_type_name='AppengineProjectsLocationsApplicationsAuthorizedDomainsListRequest',
        response_type_name='ListAuthorizedDomainsResponse',
        supports_download=False,
    )

  class ProjectsLocationsApplicationsServicesMigrationService(base_api.BaseApiService):
    """Service class for the projects_locations_applications_services_migration resource."""

    _NAME = 'projects_locations_applications_services_migration'

    def __init__(self, client):
      super(AppengineV1alpha.ProjectsLocationsApplicationsServicesMigrationService, self).__init__(client)
      self._upload_configs = {
          }

    def CheckGen1appId(self, request, global_params=None):
      r"""rpc to check if a given app_id exists in App Engine Gen1.

      Args:
        request: (AppengineProjectsLocationsApplicationsServicesMigrationCheckGen1appIdRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CheckGen1AppIdResponse) The response message.
      """
      config = self.GetMethodConfig('CheckGen1appId')
      return self._RunMethod(
          config, request, global_params=global_params)

    CheckGen1appId.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/applications/{applicationsId}/services/{servicesId}/migration/checkGen1appId',
        http_method='POST',
        method_id='appengine.projects.locations.applications.services.migration.checkGen1appId',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='checkGen1AppIdRequest',
        request_type_name='AppengineProjectsLocationsApplicationsServicesMigrationCheckGen1appIdRequest',
        response_type_name='CheckGen1AppIdResponse',
        supports_download=False,
    )

    def MigrateCodeFile(self, request, global_params=None):
      r"""rpc to migrate a code file. Eg. app.py.

      Args:
        request: (AppengineProjectsLocationsApplicationsServicesMigrationMigrateCodeFileRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('MigrateCodeFile')
      return self._RunMethod(
          config, request, global_params=global_params)

    MigrateCodeFile.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/applications/{applicationsId}/services/{servicesId}/migration/migrateCodeFile',
        http_method='POST',
        method_id='appengine.projects.locations.applications.services.migration.migrateCodeFile',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='migrateCodeFileRequest',
        request_type_name='AppengineProjectsLocationsApplicationsServicesMigrationMigrateCodeFileRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def MigrateConfigYaml(self, request, global_params=None):
      r"""rpc to migrate the config yaml file eg. app.yaml.

      Args:
        request: (AppengineProjectsLocationsApplicationsServicesMigrationMigrateConfigYamlRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (MigrateConfigYamlResponse) The response message.
      """
      config = self.GetMethodConfig('MigrateConfigYaml')
      return self._RunMethod(
          config, request, global_params=global_params)

    MigrateConfigYaml.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/applications/{applicationsId}/services/{servicesId}/migration/migrateConfigYaml',
        http_method='POST',
        method_id='appengine.projects.locations.applications.services.migration.migrateConfigYaml',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='migrateConfigYamlRequest',
        request_type_name='AppengineProjectsLocationsApplicationsServicesMigrationMigrateConfigYamlRequest',
        response_type_name='MigrateConfigYamlResponse',
        supports_download=False,
    )

  class ProjectsLocationsApplicationsServicesService(base_api.BaseApiService):
    """Service class for the projects_locations_applications_services resource."""

    _NAME = 'projects_locations_applications_services'

    def __init__(self, client):
      super(AppengineV1alpha.ProjectsLocationsApplicationsServicesService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationsApplicationsService(base_api.BaseApiService):
    """Service class for the projects_locations_applications resource."""

    _NAME = 'projects_locations_applications'

    def __init__(self, client):
      super(AppengineV1alpha.ProjectsLocationsApplicationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(AppengineV1alpha.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (AppengineProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='appengine.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='AppengineProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns UNIMPLEMENTED.

      Args:
        request: (AppengineProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='appengine.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+name}/operations',
        request_field='',
        request_type_name='AppengineProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(AppengineV1alpha.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (AppengineProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='appengine.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='AppengineProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (AppengineProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations',
        http_method='GET',
        method_id='appengine.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+name}/locations',
        request_field='',
        request_type_name='AppengineProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(AppengineV1alpha.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
