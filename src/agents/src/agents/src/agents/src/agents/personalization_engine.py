```python
from .base_agent import BaseAgent, AgentType
from datetime import datetime

class PersonalizationAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="pers_001",
            agent_type=AgentType.PERSONALIZATION,
            name="Personalization Engine",
            description="User profiling, recommendations"
        )
        self.profiles = {}

    async def execute(self, task):
        t = task["data"].get("task_type")
        if t == "profile":
            return await self._profile(task)
        elif t == "recommend":
            return await self._recommend(task)
        elif t == "learning_path":
            return await self._learning_path(task)
        else:
            raise ValueError("Unknown task")

    async def validate_input(self, data): return "task_type" in data
    async def post_process(self, result):
        result["processed_at"] = datetime.utcnow().isoformat()
        return result

    async def _profile(self, task):
        user_id = task["data"].get("user_id")
        profile = {
            "user_id": user_id,
            "age": task["data"].get("age", 5),
            "interests": ["adventure", "animals"],
            "reading_level": "intermediate"
        }
        self.profiles[user_id] = profile
        return {"profile": profile}

    async def _recommend(self, task):
        user_id = task["data"].get("user_id")
        limit = task["data"].get("limit", 5)
        recs = [{"story_id": f"rec_{i}", "score": 0.95 - i*0.02} for i in range(1, limit+1)]
        return {"user_id": user_id, "recommendations": recs}

    async def _learning_path(self, task):
        user_id = task["data"].get("user_id")
        return {
            "user_id": user_id,
            "stages": [
                {"stage": 1, "stories": ["s1", "s2"], "duration": "1 week"},
                {"stage": 2, "stories": ["s3", "s4", "s5"], "duration": "2 weeks"}
            ]
        }
```
