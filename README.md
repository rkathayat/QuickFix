# QuickFix

QuickFix is a platform designed to act as a bridge between customers and mechanics, making it easy for users to find, connect, and interact with automotive service providers. Whether you need a quick repair or regular maintenance, QuickFix streamlines the process for both customers and mechanics.

## Features

- **Customer-Mechanic Matching:** Connects customers with nearby, qualified mechanics based on service needs.
- **Service Requests:** Customers can post repair or maintenance requests and receive responses from mechanics.
- **Booking & Scheduling:** Schedule appointments with mechanics at your convenience.
- **Reviews & Ratings:** Both customers and mechanics can leave feedback and ratings.
- **Notifications:** Real-time updates for service status and communication.

## Tech Stack

- **Backend:** [Django](https://www.djangoproject.com/)
- **Frontend:** (Django Templates, Bootstrap)
- **Database:** (SQLite)

## Getting Started

### Prerequisites

- Python 3.12
- Django (see `requirements.txt` for all dependencies)

### Installation

1. **Clone the repository:**
    ```bash
    git clone git@github.com:rkathayat/QuickFix.git
    cd QuickFix
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv .env
    source .env/bin/activate   # On Windows use `.env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the app:**
    - Visit [http://localhost:8000](http://localhost:8000) in your browser.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements or bug fixes.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or support, please open an issue or contact [your-email@example.com].

---

*QuickFix — Bridging the gap between customers and mechanics for seamless automotive service!*
