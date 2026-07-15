```python
from .base_agent import BaseAgent, AgentType
from datetime import datetime

class AnalyticsOfficer(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="analytics_001",
            agent_type=AgentType.ANALYTICS,
            name="Analytics Officer",
            description="Metrics, reports, insights"
        )

    async def execute(self, task):
        t = task["data"].get("task_type")
        if t == "metrics":
            return await self._metrics(task)
        elif t == "report":
            return await self._report(task)
        elif t == "dashboard":
            return await self._dashboard(task)
        else:
            raise ValueError("Unknown task")

    async def validate_input(self, data): return "task_type" in data
    async def post_process(self, result):
        result["processed_at"] = datetime.utcnow().isoformat()
        return result

    async def _metrics(self, task):
        return {
            "dau": 2500,
            "mau": 15000,
            "retention_d7": 0.65,
            "avg_session_min": 12.5
        }

    async def _report(self, task):
        rtype = task["data"].get("report_type", "daily")
        return {
            "type": rtype,
            "total_users": 15000,
            "new_users_today": 150,
            "insights": ["Engagement up 12%", "Adventure stories most popular"]
        }

    async def _dashboard(self, task):
        return {
            "charts": {
                "dau": {"data": [2000, 2100, 2250, 2400, 2500]},
                "top_stories": {"data": [450, 380, 320]}
            }
        }
```
