```python
from src.agents import (
    ContentCuratorAgent, PersonalizationAgent,
    AnalyticsOfficer, SupportManager, GrowthStrategist
)

def load_agents():
    agents = {
        "curator": ContentCuratorAgent(),
        "personalization": PersonalizationAgent(),
        "analytics": AnalyticsOfficer(),
        "support": SupportManager(),
        "growth": GrowthStrategist()
    }
    for name, agent in agents.items():
        print(f"✅ Loaded {agent.name} ({agent.agent_id})")
    return agents

if __name__ == "__main__":
    load_agents()
```
