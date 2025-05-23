# CityStayNL Backend

**Live Website:** [citystaynl.com](https://citystaynl.com)

CityStayNL is a full-stack location-based real estate web application designed to address the growing need for rental and purchase properties in St. John’s, Newfoundland. With the **significant increase in immigrants, particularly international students, over the past few years**, CityStayNL aims to simplify the process of finding affordable and convenient housing for newcomers.

This repository contains the backend code for the application, built using **Django REST Framework (DRF)**, **GeoDjango**, and **PostGIS** for handling geographic data and spatial queries.

---

## Key Features
- **Interactive Maps**: Integrated with React-Leaflet and PostGIS for geographic data handling.
- **Nearby Places**: Displays nearby amenities (e.g., schools, hospitals, grocery stores) within a **3 km radius** of a particular listing, helping users evaluate the convenience of the location.
- **User Authentication**: Secure user authentication using Djoser for managing listings, messaging, and reviews.
- **Search Functionality**: Distance-based and voice-based search for rental listings.
- **Pagination**: Efficient browsing of rental listings with pagination.
- **Media Optimization**: Reduced media file size to 35% of the original size using Python libraries, improving performance and storage efficiency.
- **Secure Deployment**: 
  - SSL certificate integration for secure HTTPS connections.
  - **Nginx**: Used as a reverse proxy server to manage requests and improve performance.
  - **Gunicorn**: A WSGI server used for serving the Django backend.
  - **Firewall**: Configured to restrict unauthorized access and protect the server from external threats.

---

## Technologies Used
### Backend
- **Django REST Framework (DRF)**: For building the backend API.
- **GeoDjango**: For handling geographic data.
- **PostGIS & PostgreSQL**: For spatial queries and database management.
- **Boto3**: AWS SDK for Python to integrate with AWS services.
- **Django**: Python web framework for building web applications.
- **Django-Cors-Headers**: For handling Cross-Origin Resource Sharing (CORS) in Django.
- **Django-Storages**: For integrating with cloud storage backends such as AWS S3.
- **Django REST Framework (DRF)**: For creating and managing the API endpoints.
- **Django REST Framework GIS**: For spatial queries and geographic data management in DRF.
- **Djoser**: A lightweight REST framework for handling authentication-related tasks.
- **Pillow**: For image processing and management in Django.
- **Psycopg2**: PostgreSQL adapter for Python, used to interact with PostgreSQL databases.

### Frontend
- **React**: JavaScript library for building the user interface.
- **React-Router-Dom**: For handling routing and navigation in the application.
- **@mui/material, @emotion/react, @emotion/styled**: For building a modern and responsive UI using Material UI.
- **Leaflet**: For interactive maps and handling geographical data.
- **React-Leaflet**: For integrating Leaflet maps in the React environment.
- **Axios**: For making HTTP requests to the backend.
- **Immer**: For working with immutable data structures.
- **Use-Immer**: A hook for using Immer with React’s state management.
- **Other Dependencies**: Various other libraries for state management, styling, and performance optimization.

Find the frontend code here: [CityStay-Backend](https://github.com/sayyam44/CityStay-Frontend)

### Database
- **PostgreSQL**: The application uses PostgreSQL for database management, storing rental listings, user information, and other relevant data.
- **PostGIS**: An extension of PostgreSQL for handling geographic data, enabling spatial queries and geospatial data management.
- **Psycopg2**: PostgreSQL adapter for Python used to interact with the PostgreSQL database.

### Deployment
- **DigitalOcean**: The application is hosted on DigitalOcean for production use.
- **Nginx & Gunicorn**: Nginx is used as a reverse proxy, and Gunicorn is the WSGI server for serving the Django application.
- **DigitalOcean Spaces**: Leveraging Amazon S3 for cloud storage and media management.
- **SSL Certificate**: Secure connections with HTTPS using SSL certificates.
- **Firewall**: Configured to restrict unauthorized access and protect the server from external threats.

---

## Installation
To run the backend locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/citystaynl-backend.git
   cd citystaynl-backend
   
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Apply migrations**:
   ```bash
   python manage.py migrate

5. **Run the development server**:
   ```bash
   python manage.py runserver
   
The backend will be available at http://localhost:8000.

### Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository:
    Click the "Fork" button on the top right of the repository page.
   
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   
3. Stage and commit your changes:
   ```bash
   git add .
   git commit -m "Add your meaningful commit message"

4) Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   
5) Submit a pull request:
   - Go to the original repository and click "New Pull Request".
   - Select your branch and provide a detailed description of your changes.

## **Developed by**
Sayyam Kundra.

## **Live Website**
[citystaynl.com](https://citystaynl.com)

## **Frontend Repository**
[CityStay-Backend](https://github.com/sayyam44/CityStay-Frontend)

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.
