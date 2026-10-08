import pytest
from config import settings

@pytest.fixture
def base_url():
    return settings.base_url