Task Management APIA lightweight RESTful API built with FastAPI and Pydantic to manage tasks using an in-memory database.FeaturesCRUD Operations: Create, read, update, and delete tasks.Search & Filter: Filter tasks by completion status (done) or substring search in titles (search).Data Validation: Strict request/response validation using Pydantic models.Statistics & Management: View total, completed, and pending task counts, or reset the database to its initial state.Prerequisites & InstallationClone the repository (or save the code in main.py).Install dependencies:Bashpip install fastapi uvicorn
Run the application:Bashuvicorn main:app --reload
Interactive API Documentation:Once running, access Swagger UI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) or ReDoc at [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).API ReferenceSystem EndpointsMethodEndpointDescriptionGET/Returns API metadata and primary endpointsGET/healthHealth check endpoint returning {"status": "ok"}GET/statsReturns total, completed, and open task countsPOST/resetResets the in-memory database back to default seed dataTask Endpoints1. Get All TasksURL: /tasksMethod: GETQuery Parameters:done (optional, boolean): Filter by completion state (true or false).search (optional, string): Case-sensitive substring filter for task titles.Response (200 OK):JSON[
  {
    "id": 1,
    "title": "Learn CRUD operation",
    "done": true
  }
]
2. Get Task by IDURL: /tasks/{id}Method: GETResponse (200 OK):JSON{
  "id": 1,
  "title": "Learn CRUD operation",
  "done": true
}
Error Response (404 Not Found): If the ID doesn't exist.3. Create TaskURL: /tasksMethod: POSTRequest Body:JSON{
  "title": "Build a FastAPI project"
}
Response (201 Created):JSON{
  "id": 4,
  "title": "Build a FastAPI project",
  "done": false
}
4. Update TaskURL: /tasks/{id}Method: PATCHRequest Body (partial updates allowed):JSON{
  "done": true
}
Response (200 OK):JSON{
  "id": 1,
  "title": "Learn CRUD operation",
  "done": true
}
5. Delete TaskURL: /tasks/{id}Method: DELETEResponse (204 No Content)Project StructurePlaintext.
├── main.py          # Application entry point and API routes
└── README.md        # Project documentation