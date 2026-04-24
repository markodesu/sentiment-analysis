# Deployment Guide for Sentiment Analysis Web App

This guide covers multiple ways to deploy your Flask sentiment analyzer online.

---

## Option 1: Deploy on PythonAnywhere (Easiest - Free)

PythonAnywhere is specifically designed for Python web apps and requires minimal setup.

### Steps:

1. **Create Account**
   - Go to https://www.pythonanywhere.com
   - Sign up for a free account (beginner tier)
   - Verify your email

2. **Upload Your Code**
   - Click "New console" → "Bash"
   - Clone your GitHub repository:
   ```bash
   git clone https://github.com/markodesu/sentiment-analysis.git
   cd sentiment-analysis
   ```

3. **Create Virtual Environment**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 sentiment-env
   pip install -r requirements.txt
   ```

4. **Create Web App**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Flask"
   - Choose Python 3.10
   - Click "Next"

5. **Configure WSGI File**
   - PythonAnywhere creates a WSGI file automatically
   - Edit the WSGI file (go to Web tab, click on WSGI configuration file)
   - Replace content with:
   ```python
   import sys
   path = '/home/YOUR_USERNAME/sentiment-analysis'
   if path not in sys.path:
       sys.path.append(path)
   
   from app import app
   application = app
   ```
   - Replace `YOUR_USERNAME` with your PythonAnywhere username

6. **Set Working Directory**
   - In Web tab, scroll down to "Virtualenv"
   - Set to: `/home/YOUR_USERNAME/.virtualenvs/sentiment-env`

7. **Reload**
   - Click the green "Reload" button
   - Your app is now live at: `https://YOUR_USERNAME.pythonanywhere.com`

### URL Format:
```
https://YOUR_USERNAME.pythonanywhere.com
```

---

## Option 2: Deploy on Render (Modern - Free with Optional Premium)

Render is a modern cloud platform with automatic deployments from GitHub.

### Steps:

1. **Create Account**
   - Go to https://render.com
   - Sign up with GitHub
   - Authorize Render to access your repositories

2. **Create New Web Service**
   - Dashboard → New → Web Service
   - Connect your GitHub repository (markodesu/sentiment-analysis)
   - Choose your GitHub account and repository
   - Click "Connect"

3. **Configure Service**
   - **Name**: sentiment-analysis
   - **Environment**: Python 3
   - **Region**: Choose closest to you
   - **Build Command**: 
   ```bash
   pip install -r requirements.txt
   ```
   - **Start Command**: 
   ```bash
   gunicorn app:app
   ```

4. **Add Gunicorn**
   - Edit requirements.txt and add:
   ```
   gunicorn==21.2.0
   ```

5. **Deploy**
   - Click "Create Web Service"
   - Render automatically builds and deploys
   - URL will be: `https://sentiment-analysis.onrender.com` (or similar)

### Advantages:
- Automatic deployments when you push to GitHub
- Free tier available
- No credit card needed for free tier

### URL Format:
```
https://sentiment-analysis.onrender.com
```

---

## Option 3: Deploy Using Replit (Fastest - 5 minutes)

Replit is the fastest way to get your app online for presentations.

### Steps:

1. **Create Account**
   - Go to https://replit.com
   - Sign up with email or GitHub

2. **Import from GitHub**
   - Click "Create" → "Import from GitHub"
   - Paste: `https://github.com/markodesu/sentiment-analysis`
   - Click "Import from GitHub"

3. **Install Dependencies**
   - Open Terminal in Replit
   - Run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**
   - Click "Run" button
   - Replit automatically creates a public URL
   - Share the URL from the address bar

### URL Format:
```
https://sentiment-analysis.YOUR_REPLIT_USERNAME.repl.co
```

### Advantages:
- Fastest setup (< 5 minutes)
- Perfect for presentations
- Runs immediately in browser
- Free tier available

---

## Option 4: Deploy with Docker (Professional - Scalable)

Docker containerizes your app for deployment anywhere.

### Create Dockerfile

Create a file named `Dockerfile` in the project root:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

### Create .dockerignore

```
venv
__pycache__
*.pyc
.git
.gitignore
```

### Build and Run Locally

```bash
# Build image
docker build -t sentiment-analyzer:latest .

# Run container
docker run -p 5000:5000 sentiment-analyzer:latest

# Visit http://localhost:5000
```

### Deploy to Docker Hub

```bash
# Login to Docker
docker login

# Tag image
docker tag sentiment-analyzer:latest YOUR_DOCKERHUB_USERNAME/sentiment-analyzer:latest

# Push to Docker Hub
docker push YOUR_DOCKERHUB_USERNAME/sentiment-analyzer:latest
```

### Then deploy on:
- **Railway.app** - Drag and drop Docker image
- **Fly.io** - Fast global deployment
- **AWS ECS** - Enterprise grade
- **DigitalOcean** - Simple VPS

---

## Option 5: Deploy on Railway.app (Docker-based - Easy)

### Steps:

1. **Create Account**
   - Go to https://railway.app
   - Sign up with GitHub

2. **Create Project from GitHub**
   - New Project → GitHub Repo
   - Select markodesu/sentiment-analysis
   - Authorize Railway

3. **Deploy**
   - Railway auto-detects Flask app
   - Build starts automatically
   - URL provided in Dashboard

### URL Format:
```
https://sentiment-analysis-production.up.railway.app
```

---

## Comparison Table

| Platform | Setup Time | Cost | Best For | Scale |
|----------|-----------|------|----------|-------|
| **PythonAnywhere** | 10 min | Free tier available | Beginners, small apps | Low-medium |
| **Render** | 10 min | Free tier available | Modern deployments | Medium |
| **Replit** | 5 min | Free tier available | **Quick demos/presentations** | Low-medium |
| **Railway** | 8 min | Free tier available | Docker users | Medium-high |
| **Docker** | 15 min | Self-hosted | Professional/scalable | Very high |
| **Heroku** | 10 min | Paid only | Legacy support | Medium |

---

## Quick Recommendation for Your Presentation (April 27)

**For the class presentation**, I recommend **Replit** because:
- ✅ Fastest setup (5 minutes)
- ✅ No credit card needed
- ✅ Automatic public URL
- ✅ Runs reliably during demo
- ✅ Can show live code execution
- ✅ Perfect for showing classmates

**For long-term hosting after presentation:**
- Render (best balance of ease + permanence)
- PythonAnywhere (most familiar for Python developers)
- Railway (modern and scalable)

---

## Additional Files Needed for Deployment

### Add `gunicorn` to requirements.txt

Update requirements.txt to include:
```
gunicorn==21.2.0
```

This is needed for cloud deployments (not for local `python3 app.py`).

### Create `Procfile` (for some platforms)

For platforms like Heroku or similar, create a `Procfile`:

```
web: gunicorn app:app
```

### Create `runtime.txt` (optional)

Specify Python version:

```
python-3.10.12
```

---

## Environment Variables

For cloud deployment, if you need to hide sensitive data:

1. **Create `.env` file locally** (NOT pushed to GitHub):
```
FLASK_ENV=production
DEBUG=False
```

2. **Use in app.py**:
```python
import os
from dotenv import load_dotenv

load_dotenv()
app.config['ENV'] = os.getenv('FLASK_ENV', 'development')
```

3. **On cloud platforms**, set environment variables in dashboard instead of `.env` file.

---

## Troubleshooting Deployment

**"ModuleNotFoundError: No module named 'app'"**
- Ensure `app.py` is in the root directory
- Check file name is exactly `app.py`

**"Port is already in use"**
- Cloud platforms automatically assign ports
- Don't hardcode port to 5000 in production
- Use: `port = os.getenv('PORT', 5000)`

**"Model file not found"**
- Ensure `outputs/sentiment_model.pkl` is in repository
- Or regenerate by running `python3 src/main.py` first

**"Static files not loading"**
- Create `static` folder in project root for CSS/JS
- Or use CDN links (like Bootstrap)

---

## Security for Production

Before deploying to public:

1. **Set DEBUG = False** in app.py:
```python
if __name__ == '__main__':
    app.run(debug=False, port=5000)
```

2. **Add CORS headers** (if needed):
```python
from flask_cors import CORS
CORS(app)
```

3. **Rate limiting** (prevent abuse):
```python
from flask_limiter import Limiter
limiter = Limiter(app)

@app.route('/predict', methods=['POST'])
@limiter.limit("100 per hour")
def predict():
    # ... your code
```

---

## Next Steps After Deployment

1. **Test the live URL** in multiple browsers
2. **Share with classmates** (get feedback)
3. **Monitor uptime** using free tools like UptimeRobot
4. **Keep README updated** with live URL
5. **Document any issues** for future reference

---

## Support & Additional Resources

- **PythonAnywhere docs**: https://www.pythonanywhere.com/help/
- **Render docs**: https://render.com/docs
- **Replit docs**: https://docs.replit.com
- **Railway docs**: https://docs.railway.app
- **Docker docs**: https://docs.docker.com
- **Flask deployment**: https://flask.palletsprojects.com/deployment/