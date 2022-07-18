from pydantic import BaseSettings, SecretStr


class ActionInputs(BaseSettings):
    github_api_token: SecretStr

    class Config:
        # Github serves us action inputs as env vars like INPUT_{name}
        env_prefix = "input_"
        case_sensitive = False


class AppSettings(BaseSettings):
    action_inputs: ActionInputs = ActionInputs()


settings = AppSettings()
