import pytest
from bots.stocks.candle import candle_command


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("period1", "MOCK_PERIOD_1"),
            ("period2", "MOCK_PERIOD_2"),
            ("date", "MOCK_DATE"),
        ],
    }


@pytest.mark.bots
@pytest.mark.vcr
def test_candle_command(recorder):
    value = candle_command("TSLA")

    value["imagefile"] = str(type(value["imagefile"]))
    recorder.capture(value)
