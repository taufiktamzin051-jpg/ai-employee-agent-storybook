```python
from .base_agent import BaseAgent, AgentType
from datetime import datetime

class GrowthStrategist(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="growth_001",
            agent_type=AgentType.GROWTH,
            name="Growth Strategist",
            description="Revenue, churn, segmentation"
        )

    async def execute(self, task):
        t = task["data"].get("task_type")
        if t == "churn":
            return await self._churn(task)
        elif t == "revenue":
            return await self._revenue(task)
        elif t == "segment":
            return await self._segment(task)
        elif t == "strategy":
            return await self._strategy(task)
        else:
            raise ValueError("Unknown task")

    async def validate_input(self, data): return "task_type" in data
    async def post_process(self, result):
        result["processed_at"] = datetime.utcnow().isoformat()
        return result

    async def _churn(self, task):
        return {
            "user_id": task["data"].get("user_id"),
            "risk": "low",
            "probability": 0.15,
            "actions": ["Send email", "Offer discount"]
        }

    async def _revenue(self, task):
        return {
            "current_price": 9.99,
            "recommended_price": 11.99,
            "impact": "+8.5% revenue"
        }

    async def _segment(self, task):
        return {
            "high_value": {"count": 1500, "avg_ltv": 250},
            "growth": {"count": 5000, "avg_ltv": 120},
            "at_risk": {"count": 2000, "avg_ltv": 45}
        }

    async def _strategy(self, task):
        return {
            "objectives": ["Increase MRR 25%", "Reduce churn <4%"],
            "initiatives": [
                {"name": "Retention Campaign", "cost": 5000},
                {"name": "Premium Tier", "cost": 8000}
            ]
        }
```
