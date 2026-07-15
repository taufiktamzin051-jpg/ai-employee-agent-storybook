# 🎭 AI Employee Agent - Digital Storybook Anak-Anak

Platform digital storybook anak-anak dengan 5 AI Employee Agent yang mengotomasi seluruh operasi dari content ideation hingga monetization.

## 🏗️ Arsitektur
- Content Curator Agent (Ideasi, QA, Enrichment)
- Personalization Engine (Rekomendasi, Profiling)
- Analytics Officer (Metrics, Laporan)
- Support Manager (Customer Service 24/7)
- Growth Strategist (Optimasi Revenue, Churn)

## 🚀 Quick Start
```bash
cp .env.example .env
docker-compose up -d
docker exec storybook_api python scripts/init_db.py
docker exec storybook_api python scripts/load_agents.py
