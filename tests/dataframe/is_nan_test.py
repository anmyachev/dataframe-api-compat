from __future__ import annotations

import pandas as pd

from tests.utils import nan_dataframe_1


def test_dataframe_is_nan(library: str) -> None:
    df = nan_dataframe_1(library)
    result = df.is_nan()
    result_pd = pd.api.interchange.from_dataframe(result.dataframe)
    expected = pd.DataFrame({"a": [False, False, True]})
    pd.testing.assert_frame_equal(result_pd, expected)
