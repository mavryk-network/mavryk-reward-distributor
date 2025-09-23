import pytest
import vcr
from http import HTTPStatus
from unittest.mock import patch, MagicMock
from src.mvkt.mvkt_api import MvKTApi, MvKTApiError
from src.Constants import MVKT_PUBLIC_API_URL


class NoContentResponse:
    status_code = HTTPStatus.NO_CONTENT
    text = ""


@patch("mvkt.mvkt_api.requests.get", MagicMock(return_value=NoContentResponse()))
def test_request_no_content_response():
    """Test the handling of API calls which respond with no content (204).
    Issue:
    https://github.com/mavryk-network/mavryk-reward-distributor/issues/404
    """

    # The baker address exists **only** on the mainnet
    baker_address = "tz1NortRftucvAkD1J58L32EhSVrQEWJCEnB"
    base_url = ""
    timeout = 30
    cycle = 201
    mvkt = MvKTApi(base_url, timeout)
    request_path = f"rewards/split/{baker_address}/{cycle}"
    res = mvkt._request(request_path, offset=0, limit=10000)
    assert res is None


def test_request_dns_lookup_error():
    """Test the handling of API calls which respond with a DNS lookup error."""

    # The baker address exists **only** on the mainnet
    baker_address = "tz1NortRftucvAkD1J58L32EhSVrQEWJCEnB"
    base_url = "https://not_existent_domain_name.com"
    timeout = 30
    cycle = 201
    mvkt = MvKTApi(base_url, timeout)
    request_path = f"rewards/split/{baker_address}/{cycle}"
    with pytest.raises(MvKTApiError, match="DNS lookup failed"):
        _ = mvkt._request(request_path, offset=0, limit=10000)


@vcr.use_cassette(
    "tests/regression/cassettes/test_request_content_response.yaml",
    filter_headers=["X-API-Key", "authorization"],
    decode_compressed_response=True,
)
def test_request_content_response():
    """Test the handling of API calls which respond with a content (200)."""
    baker_address = "tz1NortRftucvAkD1J58L32EhSVrQEWJCEnB"
    base_url = MVKT_PUBLIC_API_URL["MAINNET"]
    timeout = 30
    cycle = 201
    mvkt = MvKTApi(base_url, timeout)
    request_path = f"rewards/split/{baker_address}/{cycle}"
    response = mvkt._request(request_path, offset=0, limit=10000)
    assert isinstance(response, dict)
    assert response["cycle"] == cycle
