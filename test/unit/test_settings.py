import pytest
from pydantic import ValidationError
from pytest import MonkeyPatch

from pr_another_repo.settings import ActionInputs


def test_it_prevents_bad_branch_names(monkeypatch: MonkeyPatch):
    with monkeypatch.context() as m:
        for name in ["main", "master"]:
            m.setenv("INPUT_DESTINATION_HEAD_BRANCH", name)
            with pytest.raises(ValidationError) as exc_info:
                ActionInputs()
            assert (
                exc_info.value.errors()[0]["msg"]
                == "cannot push to main or master.  Push changes to different branch"
            )
