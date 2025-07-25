import unittest
from unittest.mock import patch, AsyncMock
from fastapi.testclient import TestClient
from app.main import app
from app.routers.search import get_http_service

client = TestClient(app)

class TestBikeSearchRoute(unittest.TestCase):
    @patch('app.routers.search.HttpService')
    async def test_read_item(self, mock_http_service):
        # Prepare mock data
        mock_data = {
            "bikes": [
                {
                    "date_stolen": "2023-04-01T12:00:00Z",
                    "location_found": "Mumbai",
                    "duration": 2,
                    "manufacturer": "Honda",
                    "thumb": "https://example.com/bike1.jpg"
                },
                {
                    "date_stolen": "2023-05-15T18:30:00Z",
                    "location_found": "Los Angeles",
                    "duration": 4,
                    "thumb": "https://example.com/bike2.jpg"
                }
            ]
        }

        # Mock HttpService.fetch_data
        mock_http_service.return_value.fetch_data = AsyncMock(return_value=mock_data)

        # Call the route
        response = client.get("/v1/search?location=Mumbai&duration=2&manufacturer=Honda")

        # Assert the response
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["manufacturer"] == "Honda"

    @patch('app.routers.search.HttpService')
    async def test_read_item_http_error(self, mock_http_service):
        # Mock HttpService.fetch_data to raise an HTTPStatusError
        mock_http_service.return_value.fetch_data = AsyncMock(side_effect=httpx.HTTPStatusError("Error", request=None, response=None))

        # Call route
        response = client.get("/v1/search?location=Mumbai&duration=2")

        # Assert response
        assert response.status_code == 500
        assert "Error" in response.json()["detail"]

if __name__ == '__main__':
    unittest.main()