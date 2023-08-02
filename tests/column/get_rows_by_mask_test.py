from __future__ import annotations

import pandas as pd

from tests.utils import convert_series_to_pandas_numpy
from tests.utils import integer_series_1


def test_column_get_rows_by_mask(library: str) -> None:
    ser = integer_series_1(library)
    namespace = ser.__column_namespace__()
    mask = namespace.column_from_sequence([True, False, True], dtype=namespace.Bool())
    result = ser.get_rows_by_mask(mask)
    result_pd = pd.api.interchange.from_dataframe(
        namespace.dataframe_from_dict({"result": (result).rename("result")}).dataframe
    )["result"]
    result_pd = convert_series_to_pandas_numpy(result_pd)
    expected = pd.Series([1, 3], name="result")
    pd.testing.assert_series_equal(result_pd, expected)
