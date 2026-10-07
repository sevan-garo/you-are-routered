import os

import httpx
import pytest

BASE_URL = os.getenv("ROUTEDRAG_BASE_URL", "http://localhost:8000")


@pytest.mark.integration
def test_health_returns_ok() -> None:
    response = httpx.get(f"{BASE_URL}/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
