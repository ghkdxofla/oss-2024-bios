# oss-2024-bios
공개SW 개발자대회 2024 지원 프로젝트 입니다.

## Bios란?
Bios는 Bio-Informatics Open-source Software의 약자로, 생물정보학 분야에서 사용되는 워크플로우를 관리하고 실행하는 엔진입니다. Bios는 사용자가 작성한 WDL(Workflow Description Language) 스크립트를 해석하고 실행하여 워크플로우를 관리합니다. 또한, FastAPI를 사용하여 RESTful API를 제공하여 워크플로우를 관리할 수 있습니다.

## Project 구조
```
Bios
├── api/
│   ├── __init__.py
│   ├── main.py          # FastAPI application entry point
│   ├── routes.py        # API routes for workflow management
│   ├── models.py        # Pydantic models for request/response schemas
├── core/
│   ├── __init__.py
│   ├── workflow_engine.py  # Workflow execution logic (WDL parsing and running)
├── tests/
│   ├── __init__.py
│   ├── test_workflow.py   # Test code for workflows
│   ├── test_api.py        # Test code for API endpoints
├── wdls/
│   ├── covid_analysis.wdl  # Example WDL script for COVID-19 data analysis
├── Dockerfile              # Dockerfile for containerization
├── Pipfile                 # Pipenv Pipfile for dependency management
├── Pipfile.lock            # Pipenv Pipfile.lock for reproducible environments
└── README.md               # Project documentation
```
