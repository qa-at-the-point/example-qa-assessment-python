import pytest
from pylenium.driver import Pylenium
from veriff import VeriffUI


@pytest.fixture
def veriff(py: Pylenium) -> VeriffUI:
    return VeriffUI(py).visit()


VALID_EXAMPLES = [
    ("Carlos Kidman", "English", "United States of America", "Driver's license", "InContext"),
    ("张 Zhāng", "中文（简体)", "China", "Passport", "Redirect"),
    # ... add more examples including what we've documented in veriff.feature
]


@pytest.mark.parametrize("example", VALID_EXAMPLES)
def test_veriff_valid_flow(example, veriff: VeriffUI):
    veriff.launch_veriff_with(*example)
    assert veriff.find_QR_code(example[-1]).should().be_visible()


def test_veriff_with_missing_values(veriff: VeriffUI, py: Pylenium):
    """Veriff seems to work even if there are errors or missing data and defaults to English.

    This is a bug! What should we show the user instead?
    """
    veriff.launch_veriff()
    assert veriff.find_QR_code("incontext").is_displayed() is False, "QR code is found instead of an error"
