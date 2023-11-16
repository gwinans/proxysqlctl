from google.cloud import secretmanager
from google.api_core.exceptions import NotFound


class GCPHelper:
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
