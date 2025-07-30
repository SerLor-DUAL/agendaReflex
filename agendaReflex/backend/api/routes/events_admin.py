# app/backend/api/routes/events_admin.py

# Import necessary modules
from fastapi import APIRouter, HTTPException, status, Depends               # Importing FastAPI components for routing and error handling
from typing import Optional                                                 # Importing Optional for type hints
from backend.db.db_handler import get_session                               # Importing the get_session function to manage database sessions
from backend.api.routes.auth import api_auth_get_me_cookie                  # Importing the dependency to get the current user from the generated token
from sqlmodel.ext.asyncio.session import AsyncSession                       # Importing AsyncSession for asynchronous database operations
from backend.services.event_service import EventService as es               # Importing the event service for event-related operations                     
from backend.models.event.model import Event                                # Importing the DB Event model
from backend.models.user.model import User                                  # Importing the DB User model
from backend.models.event.DTOs import EventCreate, EventRead, EventUpdate   # Importing DTOs for user input/output validation and transformation                
from sqlalchemy.exc import IntegrityError, SQLAlchemyError                  # TODO: Cambiar por funciones SQLMODEL (Importing SQLAlchemy exceptions)

# Create a new API router for event-related endpoints for admin
event_admin_router = APIRouter(tags=["events_admin"])

# ---------------------------------------------------------------------------------------------------------------------------------------------------- #
# CREATE ENDPOINTS #

@event_admin_router.post("/admin/events/", response_model=EventRead)
async def api_create_event(event_to_create: EventCreate, user_id: int, session: AsyncSession = Depends(get_session)):
    """ API endpoint to create a new event, expects an EventCreate DTO and returns an EventRead DTO."""

    # Validates datetime fields
    if not event_to_create.start_date or not event_to_create.end_date:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Start date and end date are required.")

    if event_to_create.start_date >= event_to_create.end_date:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Start date cannot be after end date.")

    # Calls the EventService function to create the event
    event = await es.create_event(event_to_create, user_id, session)
    
    try:
        # Commits the changes to the database and refresh the event
        await session.commit()
        await session.refresh(event)    
        
    # If event creation failed, raise an error
    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Data integrity error (e.g., invalid user ID)")
    
    # TODO: Modificar por SQLModel error
    # Internal server error
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e._message() if hasattr(e, '_message') else "An error occurred while creating the event.")
    
    return EventRead.model_validate(event)

# ---------------------------------------------------------------------------------------------------------------------------------------------------- #
# READ ENDPOINTS #

@event_admin_router.get("/admin/events/", response_model=list[EventRead])
async def api_get_events(amount: Optional[int] = None, session: AsyncSession = Depends(get_session)):
    """ API endpoint to get all events from the database and returns a list of EventRead DTOs. """
    
    # Retrieves all events from the database.
    events: list[Event] | None = await es.read_all_events(session, maxAmount=amount)
    
    # If no events found, raise an error
    if not events or events == [] or events is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Events not found")
        
    # Convert each Event model instance to EventRead DTO for serialization
    return [EventRead.model_validate(event) for event in events[:amount]]


@event_admin_router.get("/admin/events/{event_id}", response_model=EventRead)
async def api_read_event_by_id(event_id: int, session: AsyncSession = Depends(get_session)):
    """ API endpoint to get an event by its ID from the database and returns an EventRead DTO. """

    # Calls the EventService function to get the event by its ID
    event: Event | None = await es.read_event_by_id(event_id, session)

    # If event not found, raise an error
    if not event or event is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    
    return EventRead.model_validate(event)


@event_admin_router.get("/admin/events/user/{user_id}", response_model=list[EventRead])
async def api_read_events_by_user_id(user_id: int, session: AsyncSession = Depends(get_session), current_user: User = Depends(api_auth_get_me_cookie)):
    """ API endpoint to get all events for a specific user by its ID from the database and returns a list of EventRead DTOs. """
    
    # Calls the EventSerice to get all events by user ID
    events: list[Event] | None = await es.read_all_events_by_user_id(user_id, session)
    
    # If no events found, raise an error
    if not events or events == [] or events is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Events not found for this user") 
    
    return [EventRead.model_validate(event) for event in events]


@event_admin_router.get("/admin/events/title/{title}", response_model=list[EventRead])
async def api_read_events_by_title(title: str, session: AsyncSession = Depends(get_session)):
    """ API endpoint to get all events by title from the database and returns a list of EventRead DTOs. """
    
    # Calls the EventService to get all events by title
    events: list[Event] | None = await es.read_all_events_by_title(title, session)
    
    # If no events found, raise an error
    if not events or events == [] or events is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Events not found with this title")
    
    return [EventRead.model_validate(event) for event in events]

# ---------------------------------------------------------------------------------------------------------------------------------------------------- #
# UPDATE ENDPOINTS #

@event_admin_router.put("/admin/events/{event_id}", response_model=EventRead)
async def api_update_event_by_id(event_id: int, event_to_update: EventUpdate, session: AsyncSession = Depends(get_session)):
    """ API endpoint to update an event by its ID in the database and returns an EventRead DTO. """

    # Calls the EventService function to update the event
    event = await es.update_event(event_id, event_to_update, session)

    # If event update failed, raise an error
    if not event:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Event update failed")
        
    # Commits the changes to the database and refresh the event
    await session.commit()
    await session.refresh(event)     
    
    return EventRead.model_validate(event)

# ---------------------------------------------------------------------------------------------------------------------------------------------------- #
# DELETE ENDPOINTS #

@event_admin_router.delete("/admin/events/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
async def api_delete_event_by_id(event_id: int, session: AsyncSession = Depends(get_session)):
    """ API endpoint to delete an event by its ID from the database and returns a success message. """

    # Calls the EventService function to delete the event
    was_deleted = await es.delete_event(event_id, session)

    # If event deletion failed, raise an error
    if not was_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found or deletion failed")
    
    # Commits the changes to the database
    await session.commit()
    
    return {"detail": "Event deleted successfully"}