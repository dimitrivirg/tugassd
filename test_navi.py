import logging
from navi import warn_user


def test_warn_user_emits_warning(caplog) -> None:
    # capture logs from our logger at WARNING level
    with caplog.at_level(logging.WARNING, logger="navi"):
        warn_user()

    # check that the warning message is really there
    assert "Danger ahead" in caplog.text
