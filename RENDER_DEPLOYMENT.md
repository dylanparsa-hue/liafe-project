# 📘 LIAFE Project Deployment Guide for Render

## Step 1️⃣: Create a Render Account

1. Visit [render.com](https://render.com)
2. Sign up (you can use GitHub)
3. Log into the Dashboard

---

## Step 2️⃣: Connect GitHub Repository

1. In Render Dashboard, click **New +**
2. Select **Web Service**
3. Click **Connect a repository**
4. Select your repository (`liafe_project`)
5. Click **Connect**

---

## Step 3️⃣: Service Settings

### Basic Settings:
- **Name**: `liafe-project` (or any name you prefer)
- **Environment**: `Python 3`
- **Build Command**: 
  ```
  bash build.sh
  ```
- **Start Command**: 
  ```
  gunicorn liafe_project.wsgi --bind 0.0.0.0:$PORT --workers 2 --timeout 120
  ```
- **Plan**: Choose `Free` if you want to keep it free

---

## Step 4️⃣: Environment Variables

In the **Environment** section, add the following variables:

| Variable | Value | Description |
|----------|-------|-------------|
| `DEBUG` | `False` | Disable Debug Mode |
| `ALLOWED_HOSTS` | `*.onrender.com,localhost` | Allowed domains |
| `CSRF_TRUSTED_ORIGINS` | `https://*.onrender.com` | CSRF Protection |
| `SECRET_KEY` | `random-secret-key-here` | ⚠️ Use a strong random key |

---

## Step 5️⃣: Database (PostgreSQL)

### A) Create PostgreSQL Database:
1. Click **New +**
2. Select **PostgreSQL**
3. Settings:
   - **Name**: `liafe-db`
   - **Database Name**: `liafe_db`
   - **User**: `liafe_user`
   - **Plan**: `Free` (limited to 90 days)

### B) Connect Database to Web Service:
1. After creating the database, copy the full URL
2. In your Web Service, add:
   ```
   DATABASE_URL = postgresql://...
   ```
   (Render will configure this automatically)

---

## Step 6️⃣: Storage (Cloudinary)

### To Store Media Files:

1. Visit [cloudinary.com](https://cloudinary.com)
2. Sign up
3. Dashboard → Settings → API Keys
4. Copy:
   - `CLOUD_NAME`
   - `API_KEY`
   - `API_SECRET`

5. Add to Render Environment Variables:
   ```
   CLOUDINARY_CLOUD_NAME = your-cloud-name
   CLOUDINARY_API_KEY = your-api-key
   CLOUDINARY_API_SECRET = your-api-secret
   ```

---

## Step 7️⃣: Deploy! 🚀

1. Complete all settings
2. Click **Create Web Service**
3. Wait for deployment to complete (2-5 minutes)
4. Dashboard > Services > liafe-project to view your URL

---

## ✅ Verify Deployment

After completion:

```bash
# View Logs
Render Dashboard → Services → liafe-project → Logs

# Test URLs
https://liafe-project.onrender.com/
https://liafe-project.onrender.com/admin/
```

---

## 🔧 Troubleshooting

### Static Files Error:
```
✅ Solution: Render automatically runs `collectstatic`
```

### Database Connection Error:
```
✅ Verify that DATABASE_URL is configured correctly
```

### Import Errors:
```
✅ Ensure requirements.txt is complete and correct
```

---

## 📋 Final Checklist

- [ ] GitHub Repository pushed
- [ ] PostgreSQL Database created
- [ ] Cloudinary account setup
- [ ] All Environment Variables configured
- [ ] build.sh and render.yaml present
- [ ] Deployment completed
- [ ] Custom Domain configured (optional)

---

## 🎯 Custom Domain (Optional)

```
Render Dashboard → Services → liafe-project → Settings → Custom Domains
```

---

**Questions? 👇**
