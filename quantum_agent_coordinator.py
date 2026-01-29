"""
quantum_agent_coordinator.py

Agent coordinator module for the QuantumAI system that enables multiple
specialized agents to work together as a cohesive team.

This module implements the Mixture of Agents (MoA) architecture, allowing
agents to collaborate on complex tasks while maintaining phi-harmonic principles.
"""

import os
import json
import time
import hashlib
import logging
import uuid
from typing import Dict, List, Tuple, Any, Optional, Union, Set

# Import agent factory
from quantum_agent_factory import PhiHarmonicAgentFactory, PhiHarmonicAgent

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("PhiAgentCoordinator")

class AgentTeam:
    """
    A team of phi-harmonic agents working together on a task.
    
    Teams maintain phi-harmonic coherence across member agents and
    coordinate their activities to achieve complex goals.
    """
    
    def __init__(self, 
                team_id: str, 
                team_name: str, 
                phi: float = 1.618033988749895):
        """
        Initialize an agent team.
        
        Args:
            team_id: Unique team ID
            team_name: Human-readable team name
            phi: Golden ratio value
        """
        self.team_id = team_id
        self.team_name = team_name
        self.phi = phi
        self.members = {}  # agent_id -> agent
        self.roles = {}    # agent_id -> role
        self.task_assignments = {}  # task_id -> agent_id
        self.task_results = {}      # task_id -> result
        self.team_metrics = {
            "creation_time": time.time(),
            "last_active_time": time.time(),
            "completed_tasks": 0,
            "success_rate": 0.0,
            "phi_coherence": 0.991800  # Starting coherence value
        }
        
        # Generate unique quantum fingerprint for this team
        self.quantum_fingerprint = self._generate_team_fingerprint()
        
        logger.info(f"Created agent team '{team_name}' with ID {team_id}")
    
    def add_member(self, agent: PhiHarmonicAgent, role: str) -> None:
        """
        Add a member to the team.
        
        Args:
            agent: PhiHarmonicAgent to add
            role: Role of the agent in the team
        """
        self.members[agent.agent_id] = agent
        self.roles[agent.agent_id] = role
        
        logger.info(f"Added {agent.agent_type} agent to team '{self.team_name}' as {role}")
    
    def remove_member(self, agent_id: str) -> bool:
        """
        Remove a member from the team.
        
        Args:
            agent_id: ID of the agent to remove
            
        Returns:
            True if agent was removed, False if not found
        """
        if agent_id not in self.members:
            return False
        
        # Remove agent
        agent = self.members.pop(agent_id)
        role = self.roles.pop(agent_id)
        
        logger.info(f"Removed {agent.agent_type} agent from team '{self.team_name}'")
        
        return True
    
    def assign_task(self, task: Dict[str, Any], agent_id: str) -> str:
        """
        Assign a task to a team member.
        
        Args:
            task: Task description and parameters
            agent_id: ID of the agent to assign the task to
            
        Returns:
            Task ID
            
        Raises:
            ValueError: If agent is not a team member
        """
        if agent_id not in self.members:
            raise ValueError(f"Agent {agent_id} is not a member of team '{self.team_name}'")
        
        # Generate task ID if not provided
        if "task_id" not in task:
            task["task_id"] = f"task_{str(uuid.uuid4())[:8]}"
        
        # Assign task
        self.task_assignments[task["task_id"]] = agent_id
        
        logger.info(f"Assigned task {task['task_id']} to agent {agent_id} in team '{self.team_name}'")
        
        return task["task_id"]
    
    def execute_task(self, task_id: str) -> Dict[str, Any]:
        """
        Execute a previously assigned task.
        
        Args:
            task_id: ID of the task to execute
            
        Returns:
            Task result
            
        Raises:
            ValueError: If task is not assigned
        """
        if task_id not in self.task_assignments:
            raise ValueError(f"Task {task_id} is not assigned in team '{self.team_name}'")
        
        # Get assigned agent
        agent_id = self.task_assignments[task_id]
        agent = self.members[agent_id]
        
        # Update team last active time
        self.team_metrics["last_active_time"] = time.time()
        
        # Execute task
        task = self.task_results.get(task_id, {})
        result = agent.process_task(task)
        
        # Store result
        self.task_results[task_id] = result
        
        # Update team metrics
        self._update_team_metrics(result.get("success", False))
        
        logger.info(f"Executed task {task_id} with agent {agent_id} in team '{self.team_name}'")
        
        return result
    
    def get_team_report(self) -> Dict[str, Any]:
        """
        Get a report of the team's current state.
        
        Returns:
            Team state report
        """
        # Calculate active time
        active_time = time.time() - self.team_metrics["creation_time"]
        
        # Get member reports
        member_reports = {}
        for agent_id, agent in self.members.items():
            member_reports[agent_id] = {
                "agent_type": agent.agent_type,
                "specialization": agent.specialization,
                "role": self.roles[agent_id],
                "status": agent.state["status"]
            }
        
        return {
            "team_id": self.team_id,
            "team_name": self.team_name,
            "quantum_fingerprint": self.quantum_fingerprint,
            "member_count": len(self.members),
            "members": member_reports,
            "active_time": active_time,
            "completed_tasks": self.team_metrics["completed_tasks"],
            "success_rate": self.team_metrics["success_rate"],
            "phi_coherence": self.team_metrics["phi_coherence"],
            "coherence_quality": self._evaluate_coherence_quality()
        }
    
    def _generate_team_fingerprint(self) -> str:
        """
        Generate a quantum fingerprint for this team.
        
        Returns:
            Quantum fingerprint string
        """
        # Create a unique identifier for this team
        team_id = f"{self.team_name}_{self.team_id}_{time.time()}"
        
        # Generate hash
        team_hash = hashlib.sha256(team_id.encode()).hexdigest()[:16]
        
        # Use φ⁷·⁵ notation for consistency
        return f"φ⁷·⁵-{team_hash}"
    
    def _update_team_metrics(self, success: bool) -> None:
        """
        Update team metrics based on task success.
        
        Args:
            success: Whether the task was successful
        """
        # Increment completed tasks
        self.team_metrics["completed_tasks"] += 1
        
        # Update success rate with exponential moving average
        alpha = 1 / self.phi  # Learning rate based on phi
        current_success_rate = self.team_metrics["success_rate"]
        self.team_metrics["success_rate"] = (
            (1 - alpha) * current_success_rate + 
            alpha * (1.0 if success else 0.0)
        )
        
        # Update phi coherence
        self._update_phi_coherence(success)
    
    def _update_phi_coherence(self, success: bool) -> None:
        """
        Update phi coherence based on task success.
        
        Args:
            success: Whether the task was successful
        """
        # Current coherence
        current_coherence = self.team_metrics["phi_coherence"]
        
        # Calculate adjustment factor
        adjustment = 0.0001 * (1 if success else -1)
        
        # Apply adjustment
        new_coherence = current_coherence + adjustment
        
        # Ensure coherence stays in valid range (0.9-1.0)
        new_coherence = max(0.9, min(0.999, new_coherence))
        
        # Update stored coherence
        self.team_metrics["phi_coherence"] = new_coherence
    
    def _evaluate_coherence_quality(self) -> str:
        """
        Evaluate the quality of phi-coherence.
        
        Returns:
            Quality description
        """
        coherence = self.team_metrics["phi_coherence"]
        if coherence >= 0.995:
            return "Perfect"
        elif coherence >= 0.99:
            return "Excellent"
        elif coherence >= 0.98:
            return "Good"
        elif coherence >= 0.95:
            return "Moderate"
        else:
            return "Weak"


class PhiHarmonicCoordinator:
    """
    Coordinates multiple agent teams working on complex tasks.
    
    This coordinator implements the Mixture of Agents (MoA) architecture,
    enabling dynamic team formation, task distribution, and result aggregation
    while maintaining phi-harmonic principles.
    """
    
    def __init__(self, phi: float = 1.618033988749895):
        """
        Initialize the phi-harmonic coordinator.
        
        Args:
            phi: Golden ratio value
        """
        self.phi = phi
        self.agent_factory = PhiHarmonicAgentFactory(phi=phi)
        self.teams = {}  # team_id -> AgentTeam
        self.task_registry = {}  # task_id -> team_id
        self.coordination_metrics = {
            "total_tasks": 0,
            "completed_tasks": 0,
            "success_rate": 0.0,
            "phi_coherence": 0.991800  # Starting coherence value
        }
        
        logger.info(f"Initialized PhiHarmonicCoordinator")
    
    def create_team(self, team_name: str, team_composition: Dict[str, str]) -> str:
        """
        Create a new agent team.
        
        Args:
            team_name: Human-readable team name
            team_composition: Dict mapping agent types to roles
            
        Returns:
            Team ID
        """
        # Generate team ID
        team_id = f"team_{str(uuid.uuid4())[:8]}"
        
        # Create team
        team = AgentTeam(team_id, team_name, phi=self.phi)
        
        # Create and add agents
        for agent_type, role in team_composition.items():
            agent = self.agent_factory.create_agent(agent_type)
            team.add_member(agent, role)
        
        # Register team
        self.teams[team_id] = team
        
        logger.info(f"Created team '{team_name}' with ID {team_id}")
        
        return team_id
    
    def get_team(self, team_id: str) -> Optional[AgentTeam]:
        """
        Get a team by ID.
        
        Args:
            team_id: Team ID
            
        Returns:
            AgentTeam instance or None if not found
        """
        return self.teams.get(team_id)
    
    def list_teams(self) -> List[Dict[str, Any]]:
        """
        List all teams.
        
        Returns:
            List of team reports
        """
        return [team.get_team_report() for team in self.teams.values()]
    
    def submit_task(self, 
                   team_id: str, 
                   task: Dict[str, Any], 
                   auto_execute: bool = False) -> Dict[str, Any]:
        """
        Submit a task to a team.
        
        Args:
            team_id: ID of the team to submit the task to
            task: Task description and parameters
            auto_execute: Whether to execute the task immediately
            
        Returns:
            Task submission result
            
        Raises:
            ValueError: If team is not found
        """
        team = self.get_team(team_id)
        if not team:
            raise ValueError(f"Team {team_id} not found")
        
        # Select appropriate agent for the task
        selected_agent_id = self._select_agent_for_task(team, task)
        
        # Assign task
        task_id = team.assign_task(task, selected_agent_id)
        
        # Register task
        self.task_registry[task_id] = team_id
        
        # Update coordination metrics
        self.coordination_metrics["total_tasks"] += 1
        
        result = {
            "task_id": task_id,
            "team_id": team_id,
            "agent_id": selected_agent_id,
            "status": "assigned"
        }
        
        # Execute task if requested
        if auto_execute:
            execution_result = team.execute_task(task_id)
            result["status"] = "executed"
            result["execution_result"] = execution_result
            
            # Update coordination metrics
            self._update_coordination_metrics(execution_result.get("success", False))
        
        logger.info(f"Submitted task {task_id} to team {team_id}")
        
        return result
    
    def execute_task(self, task_id: str) -> Dict[str, Any]:
        """
        Execute a previously submitted task.
        
        Args:
            task_id: ID of the task to execute
            
        Returns:
            Task execution result
            
        Raises:
            ValueError: If task is not registered
        """
        if task_id not in self.task_registry:
            raise ValueError(f"Task {task_id} not registered")
        
        # Get team
        team_id = self.task_registry[task_id]
        team = self.teams[team_id]
        
        # Execute task
        result = team.execute_task(task_id)
        
        # Update coordination metrics
        self._update_coordination_metrics(result.get("success", False))
        
        logger.info(f"Executed task {task_id} in team {team_id}")
        
        return result
    
    def get_task_result(self, task_id: str) -> Dict[str, Any]:
        """
        Get the result of a task.
        
        Args:
            task_id: ID of the task
            
        Returns:
            Task result or status
            
        Raises:
            ValueError: If task is not registered
        """
        if task_id not in self.task_registry:
            raise ValueError(f"Task {task_id} not registered")
        
        # Get team
        team_id = self.task_registry[task_id]
        team = self.teams[team_id]
        
        # Get result if available
        if task_id in team.task_results:
            return team.task_results[task_id]
        else:
            return {
                "task_id": task_id,
                "team_id": team_id,
                "agent_id": team.task_assignments.get(task_id),
                "status": "assigned"
            }
    
    def get_coordination_statistics(self) -> Dict[str, Any]:
        """
        Get statistics about the coordinator's performance.
        
        Returns:
            Coordination statistics
        """
        # Calculate success rate
        success_rate = 0.0
        if self.coordination_metrics["total_tasks"] > 0:
            success_rate = (
                self.coordination_metrics["completed_tasks"] / 
                self.coordination_metrics["total_tasks"]
            )
        
        return {
            "total_tasks": self.coordination_metrics["total_tasks"],
            "completed_tasks": self.coordination_metrics["completed_tasks"],
            "success_rate": success_rate,
            "phi_coherence": self.coordination_metrics["phi_coherence"],
            "coherence_quality": self._evaluate_coherence_quality(),
            "team_count": len(self.teams),
            "active_teams": sum(1 for team in self.teams.values() if team.members)
        }
    
    def _select_agent_for_task(self, team: AgentTeam, task: Dict[str, Any]) -> str:
        """
        Select the most appropriate agent for a task.
        
        Args:
            team: AgentTeam instance
            task: Task description and parameters
            
        Returns:
            ID of the selected agent
            
        Raises:
            ValueError: If no suitable agent is found
        """
        # Extract task type
        task_type = task.get("task_type", "default")
        
        # Find agents that can handle this task type
        suitable_agents = []
        for agent_id, agent in team.members.items():
            if task_type in agent.get_capabilities() or "default" in agent.get_capabilities():
                suitable_agents.append((agent_id, agent))
        
        if not suitable_agents:
            raise ValueError(f"No suitable agent found for task type '{task_type}'")
        
        # Select agent with highest success rate
        selected_agent_id, selected_agent = max(
            suitable_agents,
            key=lambda x: x[1].state["success_rate"]
        )
        
        return selected_agent_id
    
    def _update_coordination_metrics(self, success: bool) -> None:
        """
        Update coordination metrics based on task success.
        
        Args:
            success: Whether the task was successful
        """
        # Increment completed tasks
        self.coordination_metrics["completed_tasks"] += 1
        
        # Update success rate with exponential moving average
        if self.coordination_metrics["total_tasks"] > 0:
            self.coordination_metrics["success_rate"] = (
                self.coordination_metrics["completed_tasks"] / 
                self.coordination_metrics["total_tasks"]
            )
        
        # Update phi coherence
        self._update_phi_coherence(success)
    
    def _update_phi_coherence(self, success: bool) -> None:
        """
        Update phi coherence based on task success.
        
        Args:
            success: Whether the task was successful
        """
        # Current coherence
        current_coherence = self.coordination_metrics["phi_coherence"]
        
        # Calculate adjustment factor
        adjustment = 0.0001 * (1 if success else -1)
        
        # Apply adjustment
        new_coherence = current_coherence + adjustment
        
        # Ensure coherence stays in valid range (0.9-1.0)
        new_coherence = max(0.9, min(0.999, new_coherence))
        
        # Update stored coherence
        self.coordination_metrics["phi_coherence"] = new_coherence
    
    def _evaluate_coherence_quality(self) -> str:
        """
        Evaluate the quality of phi-coherence.
        
        Returns:
            Quality description
        """
        coherence = self.coordination_metrics["phi_coherence"]
        if coherence >= 0.995:
            return "Perfect"
        elif coherence >= 0.99:
            return "Excellent"
        elif coherence >= 0.98:
            return "Good"
        elif coherence >= 0.95:
            return "Moderate"
        else:
            return "Weak"


# Module-level functions for direct use

def create_healing_team(phi: float = 1.618033988749895) -> Tuple[str, PhiHarmonicCoordinator]:
    """
    Create a standard healing team with logic error and optimization agents.
    
    Args:
        phi: Golden ratio value
        
    Returns:
        Tuple of (team_id, coordinator)
    """
    coordinator = PhiHarmonicCoordinator(phi=phi)
    team_id = coordinator.create_team("Healing Team", {
        "logic_error": "healer",
        "optimization": "optimizer"
    })
    
    return team_id, coordinator


if __name__ == "__main__":
    # Simple test of the module
    coordinator = PhiHarmonicCoordinator()
    
    # Create a healing team
    team_id = coordinator.create_team("Healing Team", {
        "logic_error": "healer",
        "optimization": "optimizer"
    })
    
    # Test function code with logic error
    test_code = """
def increment_values(numbers):
    # Logic error: incrementing by 2 instead of 1
    return [x + 2 for x in numbers]
"""
    
    # Submit task to team
    task = {
        "task_type": "logic_error_detection",
        "func_code": test_code,
        "func_name": "increment_values",
        "expected_behavior": {"increment": 1}
    }
    
    submission_result = coordinator.submit_task(team_id, task, auto_execute=True)
    print(f"Task submission result: {submission_result}")
    
    # Get task result
    task_id = submission_result["task_id"]
    task_result = coordinator.get_task_result(task_id)
    print(f"Task result: {task_result}")
    
    # List teams
    teams = coordinator.list_teams()
    print(f"Teams: {teams}")
    
    # Get coordination statistics
    stats = coordinator.get_coordination_statistics()
    print(f"Coordination statistics: {stats}")
