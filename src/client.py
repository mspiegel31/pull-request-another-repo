from gidgethub.httpx import GitHubAPI
from httpx import AsyncClient

from src.settings import app_settings


def get_github_client(client: AsyncClient) -> GitHubAPI:
    return GitHubAPI(
        client, app_settings.requester, oauth_token=app_settings.github_api_token
    )
