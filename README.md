# í°± Backend Wizards Stage 0: Dynamic Profile API

This project implements a RESTful **GET /me** endpoint that returns my profile information (name, email, stack) along with a **dynamic cat fact** fetched from the [Cat Facts API](https://catfact.ninja/fact). Built with **Python/FastAPI**, deployed on **Railway**, and designed to meet all HNG13 Stage 0 requirements.

## íº€ Live Demo
í´— **[GET /me](https://backend-wizards-stage0-production-290b.up.railway.app/me)**  
í´— **Swagger Docs**: [https://backend-wizards-stage0-production-290b.up.railway.app/docs](https://backend-wizards-stage0-production-290b.up.railway.app/docs)

## í³‹ API Response Format
```json
{
  "status": "success",
  "user": {
    "email": "zacchdipo@gmail.com",
    "name": "Zacchaeus Ayanniran",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-21T14:57:23.123Z",
  "fact": "Cats can jump up to 5 times their height!"
}

