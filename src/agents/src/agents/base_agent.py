```python
from abc import ABC, abstractmethod
from typing import Any, Dict
from datetime import datetime
from enum import Enum
import logging

logger = logging.getLogger(__name__)

class AgentStatus(Enum):
    IDLE = "idle"; RUNNING = "running"; PROCESSING = "processing"
    COMPLETED = "completed"; ERROR = "error"

class AgentType(Enum):
    CONTENT_CURATOR = "content_curator"
    PERSONALIZATION = "personalization"
    ANALYTICS = "analytics"
    SUPPORT = "support"
    GROWTH = "growth"

class BaseAgent(ABC):
    def __init__(self, agent_id, agent_type, name, description):
        self.agent_id = agent_id
        self.agent_type = agent_type
        self.name = name
        self.description = description
        self.status = AgentStatus.IDLE
        self.task_history = []
        self.last_activity = datetime.utcnow()

    @abstractmethod
    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]: pass

    @abstractmethod
    async def validate_input(self, input_data: Dict) -> bool: pass

    @abstractmethod
    async def post_process(self, result: Dict) -> Dict: pass

    async def run_task(self, task_type, task_data):
        try:
            self.status = AgentStatus.PROCESSING
            logger.info(f"[{self.name}] Running {task_type}")
            result = await self.execute({"data": task_data})
            result = await self.post_process(result)
            self.status = AgentStatus.COMPLETED
            return {"status": "completed", "result": result}
        except Exception as e:
            logger.error(f"[{self.name}] Error: {e}")
            self.status = AgentStatus.ERROR
            return {"status": "failed", "error": str(e)}

    def get_agent_info(self):
        return {
            "id": self.agent_id,
            "name": self.name,
            "type": self.agent_type.value,
            "status": self.status.value,
            "tasks_executed": len(self.task_history)
        }
```
