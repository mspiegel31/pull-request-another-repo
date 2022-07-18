import gidgethub.httpx
import httpx
from app_settings import app_settings

http_client = httpx.AsyncClient()

gh = gidgethub.httpx.GitHubAPI(
    http_client, app_settings.requester, oauth_token=app_settings.oauth_token
)
