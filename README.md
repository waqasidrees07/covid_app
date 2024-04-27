# COVID-19 Data API

This project is a Django REST Framework (DRF) API for managing COVID-19 data stored in a CSV file. It provides CRUD (Create, Read, Update, Delete) operations and includes pagination for efficient data retrieval. The project is also documented using Swagger through the [drf-spectacular](https://drf-spectacular.readthedocs.io/) package.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- API to manage COVID-19 data in a CSV file.
- CRUD operations (Create, Read, Update, Delete) for COVID-19 data.
- Pagination support for efficient data retrieval.
- Swagger-based API documentation using `drf-spectacular`.
- Django-based backend with Django REST Framework.

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/waqasidrees07/covid_app.git
    cd covid_app
    ```

2. Create a virtual environment and activate it:

    ```shell
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```shell
    pip install -r requirements.txt
    ```

4. Ensure you have a CSV file located in the correct path as expected by your project. You can modify the path in your code if needed.

5. Run the Django development server:

    ```shell
    python manage.py runserver
    ```

## Usage

Once the development server is running, you can access the API at `http://127.0.0.1:8000/api/docs`.

### Endpoints

- **GET** `/api/covid-data/`: Retrieve paginated COVID-19 data from the CSV file.
- **GET** `/api/covid-data/<int:id>`: Retrieve paginated COVID-19 data from the CSV file.
- **GET** `/api/covid-data/filter/<str:key_column>/<str:key_value>/`: Retrieve paginated COVID-19 data from the CSV file.
- **POST** `/api/covid-data/`: Add new COVID-19 data to the CSV file.
- **PUT** `/api/covid-data/<int:id>/`: Update existing COVID-19 data in the CSV file by ID.
- **DELETE** `/api/covid-data/<int:id>/`: Delete existing COVID-19 data from the CSV file by ID.


## API Documentation

The API documentation can be found at `http://127.0.0.1:8000/api/docs/`, where you can explore the endpoints and their usage in detail.

## Configuration

- **Pagination**: Configure the pagination settings in `settings.py`.
- **CSV File Path**: Ensure the path to the CSV file is correctly configured in your code.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

Before contributing, please review the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
