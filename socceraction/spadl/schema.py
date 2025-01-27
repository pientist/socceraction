"""Schema for SPADL actions."""
from typing import Optional

import pandera as pa
from pandera.typing import Object, Series

from . import config as spadlconfig


class SPADLSchema(pa.SchemaModel):
    """Definition of a SPADL dataframe."""

    game_id: Series[Object] = pa.Field(coerce=True)
    original_event_id: Series[Object] = pa.Field(nullable=True)
    action_id: Series[int] = pa.Field(allow_duplicates=False)
    period_id: Series[int] = pa.Field(ge=1, le=5)
    time_seconds: Series[float] = pa.Field(ge=0, le=60 * 60)  # assuming overtime < 15 min
    team_id: Series[Object] = pa.Field(coerce=True)
    player_id: Series[Object] = pa.Field(coerce=True)
    start_x: Series[float] = pa.Field(ge=0, le=spadlconfig.field_length)
    start_y: Series[float] = pa.Field(ge=0, le=spadlconfig.field_width)
    end_x: Series[float] = pa.Field(ge=0, le=spadlconfig.field_length)
    end_y: Series[float] = pa.Field(ge=0, le=spadlconfig.field_width)
    bodypart_id: Series[int] = pa.Field(isin=spadlconfig.bodyparts_df().bodypart_id)
    bodypart_name: Optional[Series[str]] = pa.Field(isin=spadlconfig.bodyparts_df().bodypart_name)
    type_id: Series[int] = pa.Field(isin=spadlconfig.actiontypes_df().type_id)
    type_name: Optional[Series[str]] = pa.Field(isin=spadlconfig.actiontypes_df().type_name)
    result_id: Series[int] = pa.Field(isin=spadlconfig.results_df().result_id)
    result_name: Optional[Series[str]] = pa.Field(isin=spadlconfig.results_df().result_name)

    class Config:  # noqa: D106
        strict = True
