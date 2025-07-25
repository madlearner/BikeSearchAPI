from typing import List, Any, Dict
import base64
from datetime import datetime
from urllib.request import urlopen 


class Utills:

    def get_stolen_bikes_details(data: Dict) -> List[Dict[str, Any]]:
        """To get the details of stolen bikes with required attributes for user"""
        bikes = []
        for bike in data['bikes']:
            if bike['date_stolen'] is not None:
                date_stolen = datetime.fromtimestamp(bike['date_stolen'])
            if bike['thumb'] is not None:
                bike['thumb'] = base64.b64encode(urlopen(bike['thumb']).read())
            bikes.append({
                'title': bike['title'],
                'manufacturer_name': bike['manufacturer_name'],
                'frame_model': bike['frame_model'],
                'date_stolen': date_stolen,
                'year': bike['year'],
                'location_found': bike['location_found'],
                'stolen_location': bike['stolen_location'],
                'thumb': bike['thumb'],
                'is_stolen': bike['stolen']}
            )
        return bikes
