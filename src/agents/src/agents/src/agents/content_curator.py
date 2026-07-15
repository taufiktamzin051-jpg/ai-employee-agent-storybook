```python
from .base_agent import BaseAgent, AgentType
from datetime import datetime
import logging
logger = logging.getLogger(__name__)

class ContentCuratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="curator_001",
            agent_type=AgentType.CONTENT_CURATOR,
            name="Content Curator",
            description="Ideation, QA, Enrichment"
        )

    async def execute(self, task):
        task_type = task["data"].get("task_type")
        if task_type == "ideate":
            return await self._ideate(task)
        elif task_type == "qa":
            return await self._qa(task)
        elif task_type == "enrich":
            return await self._enrich(task)
        else:
            raise ValueError("Unknown task")

    async def validate_input(self, data): return "task_type" in data
    async def post_process(self, result):
        result["processed_at"] = datetime.utcnow().isoformat()
        return result

    async def _ideate(self, task):
        age = task["data"].get("age_group", "3-5")
        count = task["data"].get("count", 3)
        ideas = [{"id": f"story_{i}", "title": f"Story {i}", "age": age} for i in range(1, count+1)]
        return {"ideas": ideas, "total": count}

    async def _qa(self, task):
        content = task["data"].get("content", "")
        return {
            "grammar_score": 0.98,
            "safety_score": 0.95,
            "approved": True,
            "issues": []
        }

    async def _enrich(self, task):
        story_id = task["data"].get("story_id")
        return {
            "story_id": story_id,
            "tags": ["adventure", "learning"],
            "vocabulary": ["magic", "explore"],
            "read_time": "10 min"
        }
```
