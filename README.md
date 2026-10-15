# GOLDY CAB SERVICES — Django Cab Booking Website

A responsive cab-service website with an online booking enquiry form, WhatsApp handoff, and Django admin dashboard.

## Included
- Yellow + black responsive design
- Home, Services, About, Contact pages
- Online booking form saved in MySQL
- After successful submission, opens WhatsApp with the booking summary
- Django admin to search, filter, and update booking status
- CSRF protection and basic phone validation

> This is a starter implementation. It does not process payments, calculate a guaranteed fare, dispatch drivers, or send SMS/email notifications. Confirm availability and final pricing manually with customers.

## Requirements
- Python 3.10+
- MySQL Server 8+
- pip and virtualenv

## 1. Create database
Log in to MySQL and run:

```sql
CREATE DATABASE goldycab_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Create a database user if needed and grant it access to this database.

## 2. Configure environment
Copy `.env.example` to `.env` and set your database password and a secure Django secret key.

Windows PowerShell:
```powershell
Copy-Item .env.example .env
```

macOS/Linux:
```bash
cp .env.example .env
```

## 3. Install and run
Windows:
```powershell
py -m venv .venv
.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` for the website and `http://127.0.0.1:8000/admin/` for the admin panel.

## Booking workflow
1. Customer fills in the booking form.
2. The booking is saved to the database.
3. The browser redirects to WhatsApp (`+91 6307542965`) with a prefilled booking summary.
4. The business confirms vehicle availability and final fare directly.
5. Admin can update booking status in `/admin/`.

If you want to change the WhatsApp number, update `BUSINESS_PHONE` in `bookings/views.py` and the matching number in `templates/base.html` context usage.

## Production checklist
- Set `DEBUG=False`, a strong `SECRET_KEY`, and production `ALLOWED_HOSTS`.
- Use HTTPS and secure cookies.
- Configure a production WSGI server (e.g. Gunicorn) behind Nginx, or a managed Django host.
- Run `python manage.py collectstatic`.
- Configure database backups, logging, and error monitoring.
- Add privacy policy, terms, cancellation/refund policy, and consent language before collecting real customer data.
- Replace the demo external hero image with a licensed/owned image and verify all business details.
- Do not expose `/admin/` credentials; use strong passwords and restrict access where possible.

## Project layout
- `goldycab/` — Django settings and entry points
- `bookings/` — booking model, form, views, and admin
- `templates/` — page templates
- `static/` — CSS and JavaScript


## 👨‍💻 Author

**Rohit Singh**

MCA Student

Aspiring Data Analyst | Python Developer | Machine Learning Enthusiast
  
