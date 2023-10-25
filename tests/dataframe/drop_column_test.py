from __future__ import annotations

from typing import Any, Callable

import pandas as pd
import pytest

from tests.utils import (
    convert_dataframe_to_pandas_numpy,
    integer_dataframe_1,
    interchange_to_pandas,
)


@pytest.mark.parametrize("relax", [lambda x: x, lambda x: x.collect()])
def test_drop_column(library: str, relax: Callable[[Any], Any]) -> None:
    df = relax(integer_dataframe_1(library))
    result = df.drop_columns("a")
    result_pd = interchange_to_pandas(result)
    result_pd = convert_dataframe_to_pandas_numpy(result_pd)
    expected = pd.DataFrame({"b": [4, 5, 6]})
    pd.testing.assert_frame_equal(result_pd, expected)
