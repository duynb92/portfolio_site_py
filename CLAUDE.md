# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

All Django management commands run from `portfolio_pj/`:

```bash
cd portfolio_pj

# Run development server
python manage.py runserver

# Apply migrations
python manage.py migrate

# Create migrations after model changes
python manage.py makemigrations

# Collect static files
python manage.py collectstatic --noinput

# Run all tests
python manage.py test portfolio_app -v 2

# Run a specific test module
python manage.py test portfolio_app.tests.test_facade -v 2
python manage.py test portfolio_app.tests.test_models -v 2
python manage.py test portfolio_app.tests.test_views -v 2
```

Docker-based deployment:

```bash
docker-compose up -d --build   # Build and start all services
docker-compose down            # Stop services
docker-compose logs -f web     # Follow Django app logs
```

## Architecture

**Django 2.1.7 / Python 3.10** portfolio site with function-based views.

### Data layer — two distinct patterns

1. **Facade pattern** (`portfolio_app/models/facade.py`): Portfolio data (projects, skills, profile, hobbies, services) is hardcoded as static methods on `Facade`. There is no database backing for this data — to update it, edit the Python file directly.

2. **ORM models** (`portfolio_app/models/blog.py`): The blog system (Blog, Tag, Category, BlogComment) uses Django ORM with SQLite in development and PostgreSQL in production. All models use UUID primary keys.

### Request flow

`urls.py` → function-based view (`views.py`) → calls `Facade` static methods + ORM queries → populates a Context DTO → renders a template.

Context objects live in `portfolio_app/models/context/`. Each page has a dedicated context class inheriting from `BaseContext`. They are passed to templates as `{"context": context_object}`.

### Blog-specific helpers (views.py)

`getCategories()`, `getTags()`, `getRecentBlogs()`, `getArchives()`, and `getBlogsWithPaging()` (5 items/page) are module-level functions in `views.py` used by multiple blog views.

### Static files & deployment

- WhiteNoise serves static files in production.
- Nginx proxies to Gunicorn on port 5201 (see `nginx/portfolio_site.conf`).
- `docker-compose.yml` orchestrates `db` (Postgres 11.1), `web` (Django + Gunicorn), and `nginx`.
- `SECRET_KEY` and `DEBUG` are read from environment variables in `portfolio_pj/settings.py`.

### Key paths

| Path | Purpose |
|---|---|
| `portfolio_pj/portfolio_pj/settings.py` | Django settings |
| `portfolio_pj/portfolio_pj/urls.py` | URL routing |
| `portfolio_pj/portfolio_app/views.py` | All view functions |
| `portfolio_pj/portfolio_app/models/facade.py` | Hardcoded portfolio data |
| `portfolio_pj/portfolio_app/models/blog.py` | Blog ORM models |
| `portfolio_pj/portfolio_app/template/` | Django HTML templates |
| `portfolio_pj/portfolio_app/static/` | CSS, JS, images |
