from fastapi import APIRouter
from datetime import datetime, timezone
from app.schemas.incident import Create_Incident, Incident_Report, Incident_Status
from app.services.incident_manager import create_a_inc, get_list_inc, get_a_inc
from typing import List

router = APIRouter()


# Returns all incidents
@router.get("/incidents", response_model = list[Incident_Report])
def get_end_list():
    list_of_inc = get_list_inc()
    return list_of_inc



# Returns a specfic incident according to ID
@router.get("/incidents/{id}", response_model = Incident_Report)
def get_single_inc(id : int):
    inc = get_a_inc(id)
    return inc



# Creates a incident
@router.post("/incidents", response_model = Incident_Report)
def create(skeleton : Create_Incident):
    new_inc = create_a_inc(skeleton)
    return new_inc




# Updates a incident
#@router.put()
