from unittest.mock import patch

import pytest

from main import main


@patch("main.gh", autospec=True)
def test_fails_if_bad_repo(mock_gh):
    err_message = "whups bad url"
    mock_gh.get_repo.side_effect = Exception(err_message)
    with pytest.raises(Exception) as exc_info:
        main()

    assert exc_info.type == Exception
    assert exc_info.value.args[0] == err_message
