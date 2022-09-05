import pytest
from github.GithubException import UnknownObjectException

from main import main
from pr_another_repo.settings import settings


def test_misconfigured_github_user():
    settings.action_inputs.destination_owner = "NotARealGithubUserLALLALALA"
    with pytest.raises(UnknownObjectException) as exc_info:
        main()

    assert exc_info.value.data.get("message") == "Not Found"


def test_misconfigured_github_repo():
    settings.action_inputs.destination_repo = "NotARealGithubRepoLALALALALALAL"
    with pytest.raises(UnknownObjectException) as exc_info:
        main()

    assert exc_info.value.data.get("message") == "Not Found"
