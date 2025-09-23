import io
import sys

from src.launch_common import print_banner


def test_print_banner():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print_banner("test", "test script")
    sys.stdout = sys.__stdout__
    assert "Mavryk Dynamics: info@mavryk.io" in capturedOutput.getvalue()
    assert (
        "MRD Organization: Copyright 2021-2024, see contributors.csv"
        in capturedOutput.getvalue()
    )
    assert (
        "Mavryk Reward Distributor (MRD)test script is Starting"
        in capturedOutput.getvalue()
    )
