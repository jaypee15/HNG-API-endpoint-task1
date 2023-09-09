from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
import pytz

class GetInfo(APIView):

    def get(self, request):
        # get the query parametres from the url
        slack_name = request.query_params.get("slack_name")
        track = request.query_params.get("track")

        # get current day of the week
        current_day_of_week = datetime.now(pytz.utc).strftime("%A")

        # Get the current UTC time
        current_utc_time = datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        # GitHub URL for the file being run and the full source code
        github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
        github_repo_url = "https://github.com/username/repo"

        # JSON response
        response_data = {
            "slack_name": slack_name,
            "current_day_of_week": current_day_of_week,
            "current_utc_time": current_utc_time,
            "track": track,
            "github_file_url": github_file_url,
            "github_repo_url": github_repo_url,
            "status_code": 200
        }

        return Response(response_data, status=status.HTTP_200_OK)