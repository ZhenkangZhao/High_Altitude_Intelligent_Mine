import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.src.models.vehicle import Vehicle, WorkStatus, Base


@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


def test_vehicle_creation(db_session):
    vehicle = Vehicle(
        vehicle_id="V001",
        current_lat=32.123,
        current_lon=98.456,
        current_speed=15.5,
        heading=90.0,
        work_status=WorkStatus.WORKING,
    )
    db_session.add(vehicle)
    db_session.commit()

    result = db_session.query(Vehicle).first()
    assert result.vehicle_id == "V001"
    assert result.current_lat == 32.123
    assert result.work_status == WorkStatus.WORKING