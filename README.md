# LIAFE — London International Academy for Excellence

Full Django website with Jazzmin-powered admin dashboard. Everything is editable from the admin — no code needed.

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure environment
cp .env.example .env
# Edit .env — set SECRET_KEY at minimum

# 3. Apply migrations
python manage.py migrate

# 4. Seed all content
python manage.py seed_site

# 5. Create admin user
python manage.py createsuperuser

# 6. Run
python manage.py runserver
```

Website: **http://127.0.0.1:8000**  
Admin: **http://127.0.0.1:8000/admin/**

---

## Admin Credentials (dev)

| Username | Password |
|----------|----------|
| `admin`  | `liafe2024!` |

**Change these in production.**

---

## Pages

| URL | Page |
|-----|------|
| `/` | Home |
| `/services/shariah-advisory/` | Shariah Advisory |
| `/services/academy/` | Academy |
| `/services/research-house/` | Research House |
| `/services/publication/` | Publication |
| `/contact/` | Contact Us |

---

## Admin Dashboard — What You Can Edit

Log in at `/admin/` with the Jazzmin-powered dashboard. The homepage shows:
- Live stats (services, publications, messages, inquiries)
- Unread message alerts
- Recent contact messages
- Recent publications
- Quick action buttons

### Site Settings
Edit everything in one place: company name, logo, favicon, phone, email, address, social links, hero section, about section, CTA section, contact page text, footer, SEO defaults.

### Services (4 pages)
Each service has: hero title/subtitle, full description, icon, image, CTA, SEO fields.  
Inline feature/card editing per service.

### Shariah Advisory Items
Two types managed separately:
- **Process Steps** — the numbered 8-step workflow
- **Advisory Cards** — the specialisation grid

### Academy
- **Course Categories** — 4 programme areas with delivery method, duration, level
- **Courses** — add real courses with pricing, start dates, registration links

### Research House
- **Research Categories** — 3 focus areas
- **Research Projects** — individual projects with status, client, year, report upload

### Publications
Full management: type, author, cover image, PDF upload, external link, ISBN, DOI, tags, featured flag, ordering.

### Messages & Inquiries
- Read/unread status with visual indicators
- Search and filter
- Admin notes field on inquiries
- Cannot be accidentally created via admin

---

## Switch to PostgreSQL

In `.env`:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=liafe_db
DB_USER=liafe_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

Then `python manage.py migrate`.
