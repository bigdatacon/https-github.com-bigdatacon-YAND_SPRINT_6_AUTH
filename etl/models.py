"""."""

from uuid import UUID

from pydantic import BaseModel


class FilmBase(BaseModel):
    """."""

    user: UUID
    film: UUID


class FilmView(FilmBase):
    """."""

    progress_time: int


MODELS = {'views': FilmView}
