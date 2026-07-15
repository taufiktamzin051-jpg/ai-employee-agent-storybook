```python
from .base_agent import BaseAgent, AgentType
from datetime import datetime

class SupportManager(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="support_001",
            agent_type=AgentType.SUPPORT,
            name="Support Manager",
            description="Customer support, moderation, FAQ"
        )
        self.faq = [
            {"q": "How to download?", "a": "Go to Library > Download"},
            {"q": "Parental controls?", "a": "Enable in Settings"}
        ]

    async def execute(self, task):
        t = task["data"].get("task_type")
        if t == "ticket":
            return await self._ticket(task)
        elif t == "feedback":
            return await self._feedback(task)
        elif t == "moderate":
            return await self._moderate(task)
        elif t == "faq":
            return await self._faq(task)
        else:
            raise ValueError("Unknown task")

    async def validate_input(self, data): return "task_type" in data
    async def post_process(self, result):
        result["processed_at"] = datetime.utcnow().isoformat()
        return result

    async def _ticket(self, task):
        ticket_id = f"ticket_{int(datetime.utcnow().timestamp())}"
        return {
            "ticket_id": ticket_id,
            "user_id": task["data"].get("user_id"),
            "status": "open",
            "ai_response": "Thank you, we'll respond shortly."
        }

    async def _feedback(self, task):
        rating = task["data"].get("rating", 0)
        return {
            "rating": rating,
            "sentiment": "positive" if rating >= 4 else "neutral",
            "action_required": rating < 3
        }

    async def _moderate(self, task):
        return {"is_safe": True, "safety_score": 0.98, "action": "approved"}

    async def _faq(self, task):
        query = task["data"].get("query", "")
        matches = [f for f in self.faq if query.lower() in f["q"].lower()]
        return {"faqs": matches[:3]}
```
