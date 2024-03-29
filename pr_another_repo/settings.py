from typing import List

from pydantic import BaseSettings, EmailStr, SecretStr, validator, DirectoryPath


class ActionInputs(BaseSettings):
    github_api_token: SecretStr
    user_email: EmailStr = EmailStr("github-actions@users.noreply.github.com")
    user_name: str = "github-actions[bot]"
    source_folder: DirectoryPath
    destination_owner: str
    destination_repo: str
    destination_head_branch: str
    destination_base_branch: str = "main"
    destination_folder: str = ""
    pull_request_reviewers: List[str] = []
    pull_request_title = 'Automated PR'
    pull_request_body = ''

    @validator("destination_head_branch")
    def avoid_dangerous_branch_names(cls, v):
        if v in set(["main", "master"]):
            raise ValueError(
                "cannot push to main or master.  Push changes to different branch"
            )
        return v

    class Config:
        # Github serves us action inputs as env vars like INPUT_{name}
        env_prefix = "input_"
        case_sensitive = False


class AppSettings(BaseSettings):
    action_inputs: ActionInputs = ActionInputs()


settings = AppSettings()
