#!/usr/bin/env python3
"""
KEY LEVELS DASHBOARD FLOW DEBUG
===============================

Targeted debug script to trace the exact data flow for key levels
in the dashboard context vs test context to identify the root cause
of the table not displaying.
"""

import asyncio
import logging
import pandas as pd
from datetime import datetime
from typing import Dict, Any

# Configure detailed logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def debug_dashboard_key_levels_flow():
    """Debug the exact key levels flow as it happens in the dashboard"""
    logger.info("🔍 DEBUGGING: Key Levels Dashboard Flow")
    
    try:
        from core_analytics_engine.its_orchestrator_v2_5 import ITSOrchestratorV2_5
        from utils.config_manager_v2_5 import ConfigManagerV2_5
        from dashboard_application.modes.structure_mode_display_v2_5 import _generate_key_level_table
        from data_models import KeyLevelsDataV2_5
        
        # Initialize components exactly as dashboard does
        config = ConfigManagerV2_5()
        orchestrator = ITSOrchestratorV2_5(config)
        
        # Run analysis with same parameters as dashboard (DTE 0-5, price range 3%)
        logger.info("🔄 Running analysis with dashboard parameters...")
        result = await orchestrator.run_full_analysis_cycle('SPX', dte_min=0, dte_max=5, price_range_percent=3)
        
        # Step 1: Check if bundle exists
        if not result:
            logger.error("❌ CRITICAL: No result bundle returned from orchestrator")
            return False
        
        logger.info(f"✅ Bundle created: {type(result)}")
        
        # Step 2: Check if key_levels_data_v2_5 exists in bundle
        key_levels_data = getattr(result, 'key_levels_data_v2_5', None)
        logger.info(f"🔍 key_levels_data_v2_5 in bundle: {key_levels_data is not None}")
        
        if not key_levels_data:
            logger.error("❌ CRITICAL: key_levels_data_v2_5 is None in bundle")
            
            # Debug: Check what attributes the bundle actually has
            bundle_attrs = [attr for attr in dir(result) if not attr.startswith('_')]
            logger.info(f"📊 Bundle attributes: {bundle_attrs}")
            
            # Check if it's under a different name
            for attr in bundle_attrs:
                attr_value = getattr(result, attr, None)
                if isinstance(attr_value, KeyLevelsDataV2_5):
                    logger.info(f"🔍 Found KeyLevelsDataV2_5 under attribute: {attr}")
                elif attr_value and hasattr(attr_value, 'supports'):
                    logger.info(f"🔍 Found object with 'supports' attribute: {attr} = {type(attr_value)}")
            
            return False
        
        logger.info(f"✅ key_levels_data_v2_5 type: {type(key_levels_data)}")
        
        # Step 3: Check individual level lists
        supports = getattr(key_levels_data, 'supports', [])
        resistances = getattr(key_levels_data, 'resistances', [])
        pin_zones = getattr(key_levels_data, 'pin_zones', [])
        vol_triggers = getattr(key_levels_data, 'vol_triggers', [])
        major_walls = getattr(key_levels_data, 'major_walls', [])
        
        logger.info(f"📊 Key Levels Breakdown:")
        logger.info(f"   Supports: {len(supports)}")
        logger.info(f"   Resistances: {len(resistances)}")
        logger.info(f"   Pin Zones: {len(pin_zones)}")
        logger.info(f"   Vol Triggers: {len(vol_triggers)}")
        logger.info(f"   Major Walls: {len(major_walls)}")
        
        total_levels = len(supports) + len(resistances) + len(pin_zones) + len(vol_triggers) + len(major_walls)
        logger.info(f"   Total Levels: {total_levels}")
        
        if total_levels == 0:
            logger.warning("⚠️ No key levels found - debugging data pipeline...")
            
            # Debug: Check strike data
            strike_data = result.processed_data_bundle.strike_level_data_with_metrics
            if not strike_data:
                logger.error("❌ No strike data available")
                return False
            
            logger.info(f"📊 Strike data count: {len(strike_data)}")
            
            # Convert to DataFrame and check SGDHP scores
            df_strike = pd.DataFrame([s.model_dump() for s in strike_data])
            logger.info(f"📊 Strike DataFrame shape: {df_strike.shape}")
            logger.info(f"📊 Available columns: {list(df_strike.columns)}")
            
            # Check SGDHP scores specifically
            if 'sgdhp_score_strike' in df_strike.columns:
                sgdhp_values = df_strike['sgdhp_score_strike'].fillna(0)
                non_zero_sgdhp = (sgdhp_values != 0).sum()
                logger.info(f"📊 SGDHP scores: {non_zero_sgdhp}/{len(df_strike)} non-zero")
                logger.info(f"📊 SGDHP range: {sgdhp_values.min():.4f} to {sgdhp_values.max():.4f}")
                
                # Show top SGDHP scores
                top_sgdhp = df_strike.nlargest(5, 'sgdhp_score_strike')[['strike', 'sgdhp_score_strike']]
                logger.info(f"📊 Top 5 SGDHP scores:\n{top_sgdhp}")
            else:
                logger.error("❌ sgdhp_score_strike column missing")
            
            return False
        
        # Step 4: Test the table generation function directly
        logger.info("🔄 Testing _generate_key_level_table function...")
        try:
            table_component = _generate_key_level_table(result, config)
            if table_component is None:
                logger.error("❌ _generate_key_level_table returned None")
                return False
            
            logger.info(f"✅ Table component generated: {type(table_component)}")
            
            # Check if it's the "no data" case
            if hasattr(table_component, 'children'):
                children = table_component.children
                logger.info(f"📊 Table component children count: {len(children) if children else 0}")
                
                # Look for warning alerts (indicates no data case)
                for child in children:
                    if hasattr(child, 'color') and child.color == 'warning':
                        logger.warning("⚠️ Table shows 'No key levels identified' warning")
                        return False
            
            logger.info("✅ Table component appears to have data")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error in _generate_key_level_table: {e}", exc_info=True)
            return False
        
    except Exception as e:
        logger.error(f"❌ Debug flow error: {e}", exc_info=True)
        return False

async def debug_key_level_generation_step():
    """Debug the key level generation step specifically"""
    logger.info("🔍 DEBUGGING: Key Level Generation Step")
    
    try:
        from core_analytics_engine.its_orchestrator_v2_5 import ITSOrchestratorV2_5
        from core_analytics_engine.key_level_identifier_v2_5 import KeyLevelIdentifierV2_5
        from utils.config_manager_v2_5 import ConfigManagerV2_5
        
        # Initialize components
        config = ConfigManagerV2_5()
        orchestrator = ITSOrchestratorV2_5(config)
        
        # Run just the data processing part
        logger.info("🔄 Running data processing...")
        
        # Get live data
        live_data = await orchestrator.data_fetcher.fetch_live_data('SPX', dte_min=0, dte_max=5, price_range_percent=3)
        if not live_data:
            logger.error("❌ No live data fetched")
            return False
        
        # Process the data
        processed_bundle = await orchestrator.metrics_calculator.calculate_all_metrics(live_data, 'SPX')
        if not processed_bundle:
            logger.error("❌ No processed bundle created")
            return False
        
        logger.info("✅ Processed bundle created")
        
        # Now test key level generation directly
        logger.info("🔄 Testing key level generation directly...")
        key_level_identifier = KeyLevelIdentifierV2_5(config)
        
        # Call the key level identification method directly
        key_levels = await key_level_identifier.identify_and_score_key_levels(
            processed_bundle.strike_level_data_with_metrics,
            processed_bundle.underlying_data_with_metrics,
            datetime.now()
        )
        
        if not key_levels:
            logger.error("❌ Key level identification returned None")
            return False
        
        logger.info(f"✅ Key levels generated: {type(key_levels)}")
        
        # Check the contents
        supports = getattr(key_levels, 'supports', [])
        resistances = getattr(key_levels, 'resistances', [])
        pin_zones = getattr(key_levels, 'pin_zones', [])
        vol_triggers = getattr(key_levels, 'vol_triggers', [])
        major_walls = getattr(key_levels, 'major_walls', [])
        
        total_levels = len(supports) + len(resistances) + len(pin_zones) + len(vol_triggers) + len(major_walls)
        
        logger.info(f"📊 Direct Key Level Generation Results:")
        logger.info(f"   Supports: {len(supports)}")
        logger.info(f"   Resistances: {len(resistances)}")
        logger.info(f"   Pin Zones: {len(pin_zones)}")
        logger.info(f"   Vol Triggers: {len(vol_triggers)}")
        logger.info(f"   Major Walls: {len(major_walls)}")
        logger.info(f"   Total: {total_levels}")
        
        if total_levels > 0:
            logger.info("✅ Key levels generated successfully in direct test")
            
            # Show sample level
            if resistances:
                sample = resistances[0]
                logger.info(f"📊 Sample resistance: {sample.level_price} (conviction: {sample.conviction_score})")
        else:
            logger.warning("⚠️ No key levels generated in direct test")
        
        return total_levels > 0
        
    except Exception as e:
        logger.error(f"❌ Key level generation debug error: {e}", exc_info=True)
        return False

async def main():
    """Run all debug tests"""
    logger.info("🚀 KEY LEVELS DASHBOARD FLOW DEBUG SUITE")
    logger.info("=" * 60)
    
    # Test 1: Dashboard flow
    dashboard_flow_success = await debug_dashboard_key_levels_flow()
    
    logger.info("=" * 60)
    
    # Test 2: Direct key level generation
    direct_generation_success = await debug_key_level_generation_step()
    
    # Summary
    logger.info("=" * 60)
    logger.info("📊 DEBUG RESULTS SUMMARY:")
    logger.info(f"✅ Dashboard Flow: {'PASS' if dashboard_flow_success else 'FAIL'}")
    logger.info(f"✅ Direct Generation: {'PASS' if direct_generation_success else 'FAIL'}")
    
    if dashboard_flow_success:
        logger.info("🎉 Key levels are working in dashboard context!")
    elif direct_generation_success:
        logger.warning("⚠️ Key levels generate directly but fail in dashboard context")
    else:
        logger.error("💥 Key levels failing at generation level")

if __name__ == "__main__":
    asyncio.run(main())
