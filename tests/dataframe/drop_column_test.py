from __future__ import annotations

import pandas as pd

from tests.utils import integer_dataframe_1
from tests.utils import interchange_to_pandas


def test_drop_column(library: str) -> None:
    df = integer_dataframe_1(library)
    result = df.drop("a")
    result_pd = interchange_to_pandas(result)
    expected = pd.DataFrame({"b": [4, 5, 6]})
    pd.testing.assert_frame_equal(result_pd, expected)
