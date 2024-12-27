
# Django Base API

This is a base Django project configured for rapid development and deployment. It serves as a starting point for building Django-based applications.

---

## **Features**
- Django 5.1.4
- User authentication system with roles (Superuser, Staffuser, User)
- CSRF protection and trusted origins
- Configured for deployment using Podman and Nginx
- SQLite as the default database (can be switched to PostgreSQL/MySQL)
- Modular and clean project structure

---

## **Getting Started**

### **1. Prerequisites**
- Python 3.10+
- Podman (or Docker)
- Nginx (for deployment)
- Optional: Certbot (for SSL)

### **2. Clone the Repository**
```bash
git clone https://github.com/alexandruRobert1989/django-boilerplate.git
cd django-base-api
```

### **3. Install Dependencies**
Create a virtual environment and install the required packages:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## **Development**

### **Run the Development Server**
Start the Django development server:
```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000`.

---

## **Deployment**

### **1. Build and Deploy with Podman**
Build the Docker image using Podman:
```bash
podman build -t django-base-api .
```

Run the container:
```bash
podman run -d -p 8081:8000 --name django-base-api-container django-base-api
```

---

### **2. Configure Nginx as a Reverse Proxy**
To deploy with Nginx, create a configuration file like `/etc/nginx/conf.d/django-base-api.conf`:

```nginx
server {
    server_name django.example.com;

    location / {
        proxy_pass http://127.0.0.1:8081;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    listen 80;
    access_log /var/log/nginx/django-base-api.access.log;
    error_log /var/log/nginx/django-base-api.error.log;
}
```

Reload Nginx:
```bash
sudo systemctl reload nginx
```

---

### **3. Auto-Restart the Container**
Set up a Systemd service for automatic restarts:
1. Create a `~/.config/systemd/user/django-base-api.service` file:
   ```ini
   [Unit]
   Description=Podman Container for Django Base API
   After=network.target

   [Service]
   ExecStart=/usr/bin/podman start -a django-base-api-container
   ExecStop=/usr/bin/podman stop -t 10 django-base-api-container
   Restart=always
   RestartSec=10

   [Install]
   WantedBy=default.target
   ```

2. Enable and start the service:
   ```bash
   systemctl --user daemon-reload
   systemctl --user enable django-base-api.service
   systemctl --user start django-base-api.service
   ```

---

---

## **Default Users**
### Available Roles:
- **Superuser**: `superuser@superuser.com / superuser`
- **Staffuser**: `staffuser@staffuser.com / staffuser`
- **User**: `user@user.com / user`

## **Default Users**

## **Default Users**

| Role       | Username    | Password  |
|------------|-------------|-----------|
| Superuser  | superuser   | superuser |
| Staffuser  | staffuser   | staffuser |
| User       | user        | user      |

---

---



## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
