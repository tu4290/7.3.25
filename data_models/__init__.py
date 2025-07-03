"""
Data Models for EOTS v2.5

This package contains all Pydantic models used throughout the system,
now organized into 6 consolidated modules for better maintainability.

CONSOLIDATED STRUCTURE:
- core_models: Base types, system state, raw/processed data, bundles, advanced metrics
- configuration_models: All configuration schemas and settings
- ai_ml_models: AI/ML, MOE, learning, and performance models  
- trading_market_models: Trading, market context, signals, recommendations
- dashboard_ui_models: Dashboard and UI component models
- validation_utils: Validation utilities and helper functions
"""

# Import all models from consolidated files to maintain backward compatibility
from .core_models import *
from .configuration_models import *
from .core_system_config import *
from .ai_ml_models import *
from .trading_market_models import *
from .dashboard_ui_models import *
from .validation_utils import *

# Maintain the original __all__ list for backward compatibility
__all__ = [
    # From core_models (base_types, system_schemas, raw_data, processed_data, bundle_schemas, advanced_metrics)
    "DataFrameSchema", "PandasDataFrame", "SystemStateV2_5", "AISystemHealthV2_5",
    "RawOptionsContractV2_5", "RawUnderlyingDataV2_5", "RawUnderlyingDataCombinedV2_5", "UnprocessedDataBundleV2_5",
    "ProcessedContractMetricsV2_5", "ProcessedStrikeLevelMetricsV2_5", "ProcessedUnderlyingAggregatesV2_5", "ProcessedDataBundleV2_5",
    "FinalAnalysisBundleV2_5", "UnifiedIntelligenceAnalysis", "AdvancedOptionsMetricsV2_5",

    # From configuration_models (all config schemas)
    "EOTSConfigV2_5", "AnalyticsEngineConfigV2_5", "AdaptiveLearningConfigV2_5", "MarketRegimeEngineSettings", "IntradayCollectorSettings",

    # From core_system_config (dashboard and visualization models)
    "DashboardModeSettings", "DashboardModeCollection", "VisualizationSettings",

    # From ai_ml_models
    "AIAdaptationV2_5", "AIAdaptationPerformanceV2_5", "AIPredictionV2_5", "AIPredictionPerformanceV2_5", "AIPredictionRequestV2_5",
    "ExpertStatus", "RoutingStrategy", "ConsensusStrategy", "AgreementLevel", "HealthStatus",
    "MOEExpertRegistryV2_5", "MOEGatingNetworkV2_5", "MOEExpertResponseV2_5", "MOEUnifiedResponseV2_5",
    "LearningInsightV2_5", "UnifiedLearningResult", "MarketPattern", "PatternThresholds", "PerformanceInterval", "PerformanceMetricType", "PerformanceMetricV2_5",
    "SystemPerformanceV2_5", "BacktestPerformanceV2_5", "ExecutionMetricsV2_5", "PerformanceReportV2_5",
    "HuiHuiExpertType", "HuiHuiModelConfigV2_5", "HuiHuiExpertConfigV2_5", "HuiHuiAnalysisRequestV2_5",
    "HuiHuiAnalysisResponseV2_5", "HuiHuiUsageRecordV2_5", "HuiHuiPerformanceMetricsV2_5", "HuiHuiEnsembleConfigV2_5", "HuiHuiUserFeedbackV2_5",
    "MarketIntelligencePattern", "MCPIntelligenceResultV2_5", "MCPToolResultV2_5", "AdaptiveLearningResult", "RecursiveIntelligenceResult",
    
    # From trading_market_models
    "TickerContextDictV2_5", "MarketRegimeState", "TimeOfDayDefinitions", "SignalPayloadV2_5", "KeyLevelV2_5", "KeyLevelsDataV2_5", "DynamicThresholdsV2_5",
    "TradeParametersV2_5", "ActiveRecommendationPayloadV2_5", "ATIFSituationalAssessmentProfileV2_5", "ATIFStrategyDirectivePayloadV2_5", "ATIFManagementDirectiveV2_5",
    
    # From dashboard_ui_models
    "DashboardModeType", "ChartType", "DashboardModeUIDetail", "ChartLayoutConfigV2_5", "ControlPanelParametersV2_5",
    "DashboardConfigV2_5", "ComponentComplianceV2_5", "DashboardStateV2_5", "DashboardServerConfig",
]
