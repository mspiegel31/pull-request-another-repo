import gidgethub.httpx
from httpx import AsyncClient

from settings import app_settings


def get_github_client(client: AsyncClient) -> gidgethub.httpx.GitHubAPI:
    return gidgethub.httpx.GitHubAPI(
        client, app_settings.requester, oauth_token=app_settings.oauth_token
    )
