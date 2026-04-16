# -*- coding: utf-8 -*-
"""三国狼人杀游戏的结构化输出模型"""
from typing import Optional, List, ClassVar
from pydantic import BaseModel, Field
from agentscope.agent import AgentBase


class DiscussionModelCN(BaseModel):
    """中文版讨论输出格式"""
    model_config = {"extra": "ignore", "str_strip_whitespace": True}

    reach_agreement: Optional[bool] = Field(
        description="是否已达成一致意见",
        default=None,
    )
    confidence_level: Optional[int] = Field(
        description="对当前推理的信心程度(1-10)",
        ge=1, le=10,
        default=None,
    )
    key_evidence: Optional[str] = Field(
        description="支持你观点的关键证据",
        default=None,
    )


def get_vote_model_cn(agents: list[AgentBase]) -> type[BaseModel]:
    """获取中文版投票模型"""

    class VoteModelCN(BaseModel):
        """中文版投票输出格式"""
        model_config = {"extra": "ignore", "str_strip_whitespace": True}

        agent_names: ClassVar = [agent.name for agent in agents]
        agent_names_str: ClassVar = ", ".join(agent_names)
        vote: Optional[str] = Field(
            description="你要投票淘汰的玩家姓名",
            default=None,
        )
        reason: Optional[str] = Field(
            description="投票理由，简要说明为什么选择此人",
            default=None,
        )
        suspicion_level: Optional[int] = Field(
            description="对被投票者的怀疑程度(1-10)",
            ge=1, le=10,
            default=None,
        )

    return VoteModelCN


class WitchActionModelCN(BaseModel):
    """中文版女巫行动模型"""
    model_config = {"extra": "ignore", "str_strip_whitespace": True}

    use_antidote: Optional[bool] = Field(
        description="是否使用解药救人",
        default=None,
    )
    use_poison: Optional[bool] = Field(
        description="是否使用毒药杀人",
        default=None,
    )
    target_name: Optional[str] = Field(
        description="目标玩家姓名（救人或毒杀的对象）",
        default=None,
    )
    action_reason: Optional[str] = Field(
        description="行动理由",
        default=None,
    )


def get_seer_model_cn(agents: list[AgentBase]) -> type[BaseModel]:
    """获取中文版预言家模型"""
    agent_names = tuple(agent.name for agent in agents)

    class SeerModelCN(BaseModel):
        """中文版预言家查验格式"""
        model_config = {"extra": "ignore", "str_strip_whitespace": True}

        target: Optional[str] = Field(
            description="要查验的玩家姓名",
            default=None,
        )
        check_reason: Optional[str] = Field(
            description="查验此人的原因",
            default=None,
        )
        priority_level: Optional[int] = Field(
            description="查验优先级(1-10)",
            ge=1, le=10,
            default=None,
        )

        @property
        def valid_targets(self) -> tuple:
            return agent_names

        @property
        def valid_targets_list(self) -> List[str]:
            return list(agent_names)

    return SeerModelCN


def get_hunter_model_cn(agents: list[AgentBase]) -> type[BaseModel]:
    """获取中文版猎人模型"""
    agent_names = tuple(agent.name for agent in agents)

    class HunterModelCN(BaseModel):
        """中文版猎人开枪格式"""
        model_config = {"extra": "ignore", "str_strip_whitespace": True}

        shoot: Optional[bool] = Field(
            description="是否使用开枪技能",
            default=None,
        )
        target: Optional[str] = Field(
            description="开枪目标玩家姓名",
            default=None,
        )
        shoot_reason: Optional[str] = Field(
            description="开枪理由",
            default=None,
        )

        @property
        def valid_targets(self) -> tuple:
            return agent_names

        @property
        def valid_targets_list(self) -> List[str]:
            return list(agent_names)

    return HunterModelCN


class WerewolfKillModelCN(BaseModel):
    """中文版狼人击杀模型"""
    model_config = {"extra": "ignore", "str_strip_whitespace": True}

    target: Optional[str] = Field(
        description="要击杀的玩家姓名",
        default=None,
    )
    kill_strategy: Optional[str] = Field(
        description="击杀策略说明",
        default=None,
    )
    team_coordination: Optional[str] = Field(
        description="与狼队友的配合计划",
        default=None,
    )


class GameAnalysisModelCN(BaseModel):
    """中文版游戏分析模型"""
    model_config = {"extra": "ignore", "str_strip_whitespace": True}

    suspected_werewolves: Optional[List[str]] = Field(
        description="怀疑的狼人名单",
        default_factory=list,
    )
    trusted_players: Optional[List[str]] = Field(
        description="信任的玩家名单",
        default_factory=list,
    )
    key_clues: Optional[List[str]] = Field(
        description="关键线索列表",
        default_factory=list,
    )
    next_strategy: Optional[str] = Field(
        description="下一步策略",
        default=None,
    )