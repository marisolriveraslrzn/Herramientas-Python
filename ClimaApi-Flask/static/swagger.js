{
  "swagger": "2.0",
  "info": {
    "title": "ClimaAPI-Flask",
    "version": "1.0.0"
  },
  "paths": {
    "/weather/{city}": {
      "get": {
        "summary": "Get weather by city",
        "parameters": [
          {
            "name": "city",
            "in": "path",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "Weather data"
          },
          "404": {
            "description": "City not found"
          }
        }
      },
      "post": {
        "summary": "Add weather data for a city",
        "parameters": [
          {
            "name": "city",
            "in": "path",
            "required": true,
            "type": "string"
          },
          {
            "name": "body",
            "in": "body",
            "required": true,
            "schema": {
              "type": "object",
              "properties": {
                "temperature": {
                  "type": "integer"
                },
                "condition": {
                  "type": "string"
                }
              }
            }
          }
        ],
        "responses": {
          "201": {
            "description": "City added successfully"
          },
          "400": {
            "description": "City already exists"
          }
        }
      }
    }
  }
}