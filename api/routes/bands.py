from fastapi import APIRouter

router = APIRouter()

fake_db = [
    {"name": "Foo Fighters", "song": "My Hero"},
    {"name": "Metallica", "song": "Hero of the Day"},
]


@router.get("")
async def get_bands():
    return fake_db
