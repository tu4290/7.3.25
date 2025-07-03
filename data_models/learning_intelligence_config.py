"""
Learning & Intelligence Configuration Models for EOTS v2.5

This module contains learning system configurations, HuiHui AI settings,
and intelligence framework parameters.

Extracted from configuration_models.py for better modularity.
"""

# Standard library imports
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

# Third-party imports
from pydantic import BaseModel, Field, ConfigDict


# =============================================================================
# LEARNING SYSTEM CONFIGURATION
# =============================================================================

class MarketContextData(BaseModel):
    """Market conditions and context relevant to learning insights."""
    market_regime: Optional[str] = Field(None, description="Current market regime")
    volatility_level: Optional[float] = Field(None, description="Current volatility level")
    trend_direction: Optional[str] = Field(None, description="Current trend direction")
    volume_profile: Optional[str] = Field(None, description="Volume profile analysis")
    sector_rotation: Optional[str] = Field(None, description="Sector rotation pattern")
    economic_indicators: Dict[str, Union[str, int, float, bool]] = Field(default_factory=dict, description="Economic indicators")
    technical_indicators: Dict[str, float] = Field(default_factory=dict, description="Technical indicator values")
    sentiment_metrics: Dict[str, float] = Field(default_factory=dict, description="Market sentiment metrics")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for backward compatibility."""
        return self.model_dump()
    
    class Config:
        extra = 'forbid'

class AdaptationSuggestion(BaseModel):
    """Suggested adaptation parameters based on learning insights."""
    parameter_name: Optional[str] = Field(None, description="Name of parameter to adjust")
    current_value: Optional[Union[str, int, float, bool]] = Field(None, description="Current parameter value")
    suggested_value: Optional[Union[str, int, float, bool]] = Field(None, description="Suggested new value")
    adjustment_reason: Optional[str] = Field(None, description="Reason for the adjustment")
    expected_impact: Optional[str] = Field(None, description="Expected impact of the change")
    confidence_level: Optional[float] = Field(None, description="Confidence in the suggestion")
    risk_assessment: Optional[str] = Field(None, description="Risk assessment of the change")
    rollback_plan: Optional[str] = Field(None, description="Plan for rolling back if needed")
    custom_adaptations: Dict[str, Union[str, int, float, bool]] = Field(default_factory=dict, description="Custom adaptation parameters")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for backward compatibility."""
        return self.model_dump()
    
    class Config:
        extra = 'forbid'

class PerformanceMetricsSnapshot(BaseModel):
    """Performance metrics snapshot for before/after comparisons."""
    accuracy_pct: Optional[float] = Field(None, description="Accuracy percentage")
    precision_pct: Optional[float] = Field(None, description="Precision percentage")
    recall_pct: Optional[float] = Field(None, description="Recall percentage")
    f1_score: Optional[float] = Field(None, description="F1 score")
    sharpe_ratio: Optional[float] = Field(None, description="Sharpe ratio")
    max_drawdown_pct: Optional[float] = Field(None, description="Maximum drawdown percentage")
    win_rate_pct: Optional[float] = Field(None, description="Win rate percentage")
    profit_factor: Optional[float] = Field(None, description="Profit factor")
    avg_return_pct: Optional[float] = Field(None, description="Average return percentage")
    volatility_pct: Optional[float] = Field(None, description="Volatility percentage")
    execution_time_ms: Optional[float] = Field(None, description="Average execution time in milliseconds")
    resource_usage_pct: Optional[float] = Field(None, description="Resource usage percentage")
    custom_metrics: Dict[str, Union[str, int, float, bool]] = Field(default_factory=dict, description="Custom performance metrics")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for backward compatibility."""
        return self.model_dump()
    
    class Config:
        extra = 'forbid'

class LearningInsightData(BaseModel):
    """Summarized learning insights from analysis."""
    insight_type: Optional[str] = Field(None, description="Type of insight discovered")
    insight_description: Optional[str] = Field(None, description="Description of the insight")
    confidence_score: Optional[float] = Field(None, description="Confidence in the insight")
    supporting_evidence: List[str] = Field(default_factory=list, description="Evidence supporting the insight")
    potential_impact: Optional[str] = Field(None, description="Potential impact of applying the insight")
    recommended_actions: List[str] = Field(default_factory=list, description="Recommended actions based on insight")
    risk_factors: List[str] = Field(default_factory=list, description="Risk factors to consider")
    validation_criteria: List[str] = Field(default_factory=list, description="Criteria for validating the insight")
    custom_insights: Dict[str, Union[str, int, float, bool]] = Field(default_factory=dict, description="Custom insight data")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for backward compatibility."""
        return self.model_dump()
    
    class Config:
        extra = 'forbid'

class ExpertAdaptationSummary(BaseModel):
    """Summary of adaptations for expert systems."""
    expert_type: Optional[str] = Field(None, description="Type of expert system")
    adaptations_applied: List[str] = Field(default_factory=list, description="List of adaptations applied")
    performance_before: Optional[PerformanceMetricsSnapshot] = Field(None, description="Performance before adaptations")
    performance_after: Optional[PerformanceMetricsSnapshot] = Field(None, description="Performance after adaptations")
    adaptation_effectiveness: Optional[float] = Field(None, description="Effectiveness of adaptations")
    rollback_required: Optional[bool] = Field(None, description="Whether rollback is required")
    next_review_date: Optional[datetime] = Field(None, description="Next review date for adaptations")
    custom_summary: Dict[str, Union[str, int, float, bool]] = Field(default_factory=dict, description="Custom summary data")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for backward compatibility."""
        return self.model_dump()
    
    class Config:
        extra = 'forbid'

class ConfidenceUpdateData(BaseModel):
    """Data for updating confidence scores."""
    component_name: Optional[str] = Field(None, description="Name of component being updated")
    old_confidence: Optional[float] = Field(None, description="Previous confidence score")
    new_confidence: Optional[float] = Field(None, description="New confidence score")
    update_reason: Optional[str] = Field(None, description="Reason for confidence update")
    supporting_data: Dict[str, Union[str, int, float, bool]] = Field(default_factory=dict, description="Data supporting the update")
    validation_results: Dict[str, Union[str, int, float, bool]] = Field(default_factory=dict, description="Validation results")
    impact_assessment: Optional[str] = Field(None, description="Assessment of update impact")
    custom_updates: Dict[str, Union[str, int, float, bool]] = Field(default_factory=dict, description="Custom update data")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for backward compatibility."""
        return self.model_dump()
    
    class Config:
        extra = 'forbid'

class LearningSystemConfig(BaseModel):
    """Configuration for the learning system."""
    enabled: bool = Field(True, description="Enable/disable learning system.")
    learning_rate: float = Field(0.01, ge=0.001, le=0.1, description="Learning rate for adaptations.")
    adaptation_threshold: float = Field(0.7, ge=0.0, le=1.0, description="Threshold for applying adaptations.")
    validation_window_days: int = Field(30, ge=7, description="Window for validating learning insights.")
    max_adaptations_per_cycle: int = Field(5, ge=1, description="Maximum adaptations per learning cycle.")
    rollback_threshold: float = Field(0.5, ge=0.0, le=1.0, description="Threshold for rolling back adaptations.")
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'enabled': self.enabled,
            'learning_rate': self.learning_rate,
            'adaptation_threshold': self.adaptation_threshold,
            'validation_window_days': self.validation_window_days,
            'max_adaptations_per_cycle': self.max_adaptations_per_cycle,
            'rollback_threshold': self.rollback_threshold
        }
    
    class Config:
        extra = 'forbid'


# =============================================================================
# HUIHUI AI SYSTEM CONFIGURATION
# =============================================================================

class AnalysisContext(BaseModel):
    """Context data for HuiHui analysis requests."""
    market_conditions: str = Field(default="normal", description="Current market conditions")
    recent_news: List[str] = Field(default_factory=list, description="Recent news items")
    volatility_regime: str = Field(default="normal", description="Current volatility regime")
    market_sentiment: str = Field(default="neutral", description="Market sentiment")
    time_of_day: str = Field(default="market_hours", description="Time context")
    custom_context: Dict[str, Union[str, int, float, bool]] = Field(default_factory=dict, description="Custom context fields")
    
    def to_dict(self) -> Dict[str, Any]:
        return self.model_dump()
    
    class Config:
        extra = 'forbid'

class RequestMetadata(BaseModel):
    """Metadata for HuiHui analysis requests."""
    request_id: str = Field(default="", description="Unique request identifier")
    user_id: str = Field(default="", description="User identifier")
    session_id: str = Field(default="", description="Session identifier")
    priority: str = Field(default="normal", description="Request priority")
    source: str = Field(default="api", description="Request source")
    custom_metadata: Dict[str, Union[str, int, float, bool]] = Field(default_factory=dict, description="Custom metadata fields")
    
    def to_dict(self) -> Dict[str, Any]:
        return self.model_dump()
    
    class Config:
        extra = 'forbid'

class EOTSPrediction(BaseModel):
    """EOTS prediction data structure."""
    prediction_type: str = Field(description="Type of prediction")
    symbol: str = Field(description="Symbol for prediction")
    confidence: float = Field(description="Prediction confidence")
    timeframe: str = Field(description="Prediction timeframe")
    direction: str = Field(description="Predicted direction")
    target_price: float = Field(default=0.0, description="Target price if applicable")
    probability: float = Field(default=0.0, description="Probability estimate")
    custom_data: Dict[str, Union[str, int, float, bool]] = Field(default_factory=dict, description="Custom prediction data")

    def to_dict(self) -> Dict[str, Any]:
        return self.model_dump()

    class Config:
        extra = 'forbid'

class TradingRecommendation(BaseModel):
    """Trading recommendation structure."""
    action: str = Field(description="Recommended action (buy/sell/hold)")
    symbol: str = Field(description="Symbol for recommendation")
    quantity: int = Field(default=0, description="Recommended quantity")
    price_target: float = Field(default=0.0, description="Price target")
    stop_loss: float = Field(default=0.0, description="Stop loss level")
    confidence: float = Field(description="Recommendation confidence")
    reasoning: str = Field(default="", description="Reasoning for recommendation")
    risk_level: str = Field(default="medium", description="Risk level")
    timeframe: str = Field(default="intraday", description="Recommendation timeframe")
    custom_attributes: Dict[str, Union[str, int, float, bool]] = Field(default_factory=dict, description="Custom recommendation attributes")

    def to_dict(self) -> Dict[str, Any]:
        return self.model_dump()

    class Config:
        extra = 'forbid'

class PerformanceByCondition(BaseModel):
    """Performance metrics by market condition."""
    success_rate: float = Field(default=0.0, description="Success rate for this condition")
    avg_processing_time: float = Field(default=0.0, description="Average processing time")
    total_requests: int = Field(default=0, description="Total requests in this condition")
    avg_confidence: float = Field(default=0.0, description="Average confidence score")
    error_rate: float = Field(default=0.0, description="Error rate for this condition")
    custom_metrics: Dict[str, float] = Field(default_factory=dict, description="Custom performance metrics")

    def to_dict(self) -> Dict[str, Any]:
        return self.model_dump()

    class Config:
        extra = 'forbid'

class HuiHuiSystemConfig(BaseModel):
    """Configuration for the HuiHui AI system."""
    enabled: bool = Field(True, description="Enable/disable HuiHui AI system.")
    model_provider: str = Field(default="openai", description="AI model provider for HuiHui.")
    model_name: str = Field(default="gpt-4", description="AI model name for HuiHui.")
    temperature: float = Field(default=0.1, ge=0.0, le=2.0, description="Model temperature for responses.")
    max_tokens: int = Field(default=4000, ge=100, description="Maximum tokens for responses.")
    timeout_seconds: int = Field(default=30, ge=5, description="Timeout for AI requests.")
    retry_attempts: int = Field(default=3, ge=1, description="Number of retry attempts for failed requests.")
    confidence_threshold: float = Field(default=0.7, ge=0.0, le=1.0, description="Minimum confidence threshold for responses.")

    def to_dict(self) -> Dict[str, Any]:
        return {
            'enabled': self.enabled,
            'model_provider': self.model_provider,
            'model_name': self.model_name,
            'temperature': self.temperature,
            'max_tokens': self.max_tokens,
            'timeout_seconds': self.timeout_seconds,
            'retry_attempts': self.retry_attempts,
            'confidence_threshold': self.confidence_threshold
        }

    class Config:
        extra = 'forbid'


# =============================================================================
# INTELLIGENCE FRAMEWORK CONFIGURATION
# =============================================================================

class IntelligenceFrameworkConfig(BaseModel):
    """Configuration for the overall intelligence framework."""
    enabled: bool = Field(True, description="Enable/disable intelligence framework.")
    learning_system: LearningSystemConfig = Field(default_factory=LearningSystemConfig, description="Learning system configuration.")
    huihui_system: HuiHuiSystemConfig = Field(default_factory=HuiHuiSystemConfig, description="HuiHui AI system configuration.")
    intelligence_update_interval_seconds: int = Field(300, ge=60, description="Interval for intelligence updates.")
    cross_system_learning: bool = Field(True, description="Enable learning across different systems.")
    knowledge_persistence: bool = Field(True, description="Enable persistence of learned knowledge.")

    def to_dict(self) -> Dict[str, Any]:
        return {
            'enabled': self.enabled,
            'learning_system': self.learning_system.to_dict(),
            'huihui_system': self.huihui_system.to_dict(),
            'intelligence_update_interval_seconds': self.intelligence_update_interval_seconds,
            'cross_system_learning': self.cross_system_learning,
            'knowledge_persistence': self.knowledge_persistence
        }

    # Additional config fields from config file
    learning_params: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Learning parameters configuration")

    model_config = ConfigDict(extra='allow')
