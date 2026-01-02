from sqlalchemy import create_engine
from settings import POSTGRES

DATABASE_URL = (
    f"postgresql://{POSTGRES['USER']}:{POSTGRES['PASSWORD']}"
    f"@{POSTGRES['HOST']}:{POSTGRES['PORT']}/{POSTGRES['NAME']}"
)

engine = create_engine(DATABASE_URL, echo=False, future=True)