import requests, os
from util import CustomLogger

logger = CustomLogger("HealthCheck")

def health_check():
    data = [
        {
            "name": "Authentication Service",
            "url": os.getenv('AUTH_SERVICE_URL')
        },
        {
            "name": "Stay Service",
            "url": os.getenv('STAY_SERVICE_URL')
        },
        {
            "name": "Booking Service",
            "url": os.getenv('BOOKING_SERVICE_URL')
        },
        {
            "name": "Payment Service",
            "url": os.getenv('PAYMENT_SERVICE_URL')
        },
        {
            "name": "Invoice Service",
            "url": os.getenv('INVOICE_SERVICE_URL')
        },
        {
            "name": "Rating Service",
            "url": os.getenv('RATING_SERVICE_URL')
        }
    ]

    for service_idx in range(len(data)):
        service = data[service_idx]
        try:
            response = requests.get(service['url'])
            if response.status_code == 200:
                logger.success(f"{service['name']} is healthy")
                data[service_idx]['status'] = "healthy"
            else:
                logger.warning(f"{service['name']} is unhealthy")
                data[service_idx]['status'] = "unhealthy"
        except:
            logger.critical(f"{service['name']} is unhealthy")
            data[service_idx]['status'] = "critical"
    
    return data

