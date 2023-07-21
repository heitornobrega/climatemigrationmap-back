
# ClimateMigrationMap Backend (climatemigrationmap-back)
 
ClimateMigrationMap Backend is the server-side component of the Climate Migration Map application. It serves as the data provider for the front-end (climatemigrationmap-web), allowing users to access historical and projected migration data between 1950 and 2101 for different countries. This project is an open-source initiative developed and maintained by Heitor Nóbrega Tico and Guillaume Lelasseur.
 
## Features (Planned)
 
- **Data API**: Provides RESTful API endpoints to fetch historical migration data and climate change projections.
- **Data Processing**: Handles the logic to process and filter migration data based on user requests.
- **Secure Communication**: Ensures secure communication between the front-end and the backend using standard authentication and encryption mechanisms.
 
Our objective is to create an accessible and informative tool that raises awareness about climate migration and its global impact.
 
## Getting Started with Development
 
This project uses Flask, a micro web framework for Python, for building the backend. To get started with development, you'll need to have Python and the required dependencies installed on your machine. Follow these steps to set up the development environment:
 
1. Clone this repository:
 
    ```
    git clone https://github.com/heitor-nobrega/climatemigrationmap-back.git
    ```
 
2. Navigate to the project directory:
 
    ```
    cd climatemigrationmap-back
    ```
 
3. Create and activate a virtual environment (optional but recommended):
 
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
 
4. Install the project dependencies:
 
    ```
    pip install -r requirements.txt
    ```
 
5. Set up environment variables (if required):
 
   You may need to configure environment variables for any sensitive information, such as API keys or database credentials.
 
6. Start the development server:
 
    ```
    python app.py
    ```
 
This will start the backend server, and it will be accessible at `http://localhost:5000`.
 
## Contributing
 
We welcome contributions from the open-source community to make this project even more valuable and impactful. To contribute, please follow these steps:
 
1. Fork this repository to your GitHub account.
2. Create a new branch with a descriptive name for your feature/bugfix.
3. Make your changes and commit them with clear commit messages.
4. Push your branch to your forked repository.
5. Create a pull request (PR) to the main repository, explaining your changes.
 
## License
 
This project is licensed under the [MIT License](LICENSE.md). By contributing to this project, you agree to abide by the terms of the license.
 
## Contact
 
For any questions, issues, or inquiries related to this project, feel free to reach out to the development team. We value community feedback and appreciate your support!