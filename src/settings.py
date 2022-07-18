from pydantic import BaseSettings


class AppSettings(BaseSettings):
    # The requester’s name (typically a GitHub username or project name).
    # https://gidgethub.readthedocs.io/en/latest/abc.html?highlight=requester#gidgethub.abc.GitHubAPI.requester
    requester: str
    oauth_token: str


app_settings = AppSettings()
