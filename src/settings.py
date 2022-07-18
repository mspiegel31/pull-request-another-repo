from pydantic import BaseSettings


class ActionInputs(BaseSettings):
    class Config:
        # Github serves us action inputs as env vars like INPUT_{name}
        env_prefix = "input_"
        case_sensitive = False


class AppSettings(BaseSettings):
    # The requester’s name (typically a GitHub username or project name).
    # https://gidgethub.readthedocs.io/en/latest/abc.html?highlight=requester#gidgethub.abc.GitHubAPI.requester
    requester: str
    github_api_token: str
    action_inputs: ActionInputs = ActionInputs()


app_settings = AppSettings()
