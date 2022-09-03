from unittest.mock import Mock, patch
from main import main
import pytest

@patch('main.gh', autospec=True)
def test_fails_if_bad_repo(mock_gh):
    mock_gh.get_repo.side_effect = Exception()
    with pytest.raises(Exception) as err:
        main()