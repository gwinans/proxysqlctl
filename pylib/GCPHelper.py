import os, datetime

from google.cloud import secretmanager
from google.api_core.exceptions import NotFound
from google.cloud.asset_v1 import AssetServiceClient, SearchAllResourcesRequest


class GCPHelper:
    def project_exists(self, org_id, project_name):
        cache_dir = os.path.expanduser("~/.config/proxysql")
        cache_file = os.path.join(cache_dir, "project.cache")

        # Create an empty cache file.
        with open(cache_file, "a"):
            pass

        if os.path.exists(cache_file):
            today = datetime.datetime.today()
            modified_date = datetime.datetime.fromtimestamp(
                os.path.getmtime(cache_file)
            )
            age = today - modified_date

        if age.seconds < 30 or age.days > 7:
            request = SearchAllResourcesRequest(
                scope=f"organizations/{org_id}",
                asset_types=["cloudresourcemanager.googleapis.com/Project"],
                query="state:ACTIVE",
            )

            paged_results = AssetServiceClient().search_all_resources(request=request)

            for response in paged_results:
                projects.append(response.name.split("/")[4])

            self.cache_projects(cache_file, projects)

        else:
            projects = self.load_cached_projects(cache_file)

        if project_name in projects:
            return True

        return False

    def get_secret(project_name, secret_name, version="latest"):
        try:
            name = f"projects/{project_name}/secrets/{secret_name}/versions/{version}"
            response = secretmanager.SecretManagerServiceClient().access_secret_version(
                name=name
            )
            return response.payload.data.decode("UTF-8")
        except NotFound:
            return None

    def cache_projects(self, cache_file, projects):
        with open(cache_file, "w") as f:
            f.write("\n".join(projects))

    def load_cached_projects(cache_file):
        with open(cache_file, "r") as f:
            return f.read().split("\n")
