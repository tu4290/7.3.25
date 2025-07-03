#!/usr/bin/env python3
"""
TABLE RENDERING DEBUG
====================

Debug script to examine the exact table component structure
and identify why it's not visible in the dashboard.
"""

import asyncio
import logging
import pandas as pd
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def debug_table_component_structure():
    """Debug the exact structure of the table component"""
    logger.info("🔍 DEBUGGING: Table Component Structure")
    
    try:
        from core_analytics_engine.its_orchestrator_v2_5 import ITSOrchestratorV2_5
        from utils.config_manager_v2_5 import ConfigManagerV2_5
        from dashboard_application.modes.structure_mode_display_v2_5 import _generate_key_level_table
        import dash_bootstrap_components as dbc
        from dash import html, dash_table
        
        # Initialize and get data
        config = ConfigManagerV2_5()
        orchestrator = ITSOrchestratorV2_5(config)
        result = await orchestrator.run_full_analysis_cycle('SPX', dte_min=0, dte_max=5, price_range_percent=3)
        
        # Generate the table component
        table_component = _generate_key_level_table(result, config)
        
        logger.info(f"✅ Table component type: {type(table_component)}")
        logger.info(f"✅ Table component: {table_component}")
        
        # Examine the component structure
        if hasattr(table_component, 'children'):
            children = table_component.children
            logger.info(f"📊 Component has {len(children)} children")
            
            for i, child in enumerate(children):
                logger.info(f"📊 Child {i}: {type(child)}")
                
                # If it's a DataTable, examine its properties
                if isinstance(child, dash_table.DataTable):
                    logger.info(f"📊 DataTable found!")
                    logger.info(f"   Columns: {child.columns}")
                    logger.info(f"   Data rows: {len(child.data) if child.data else 0}")
                    logger.info(f"   Style cell: {child.style_cell}")
                    logger.info(f"   Style header: {child.style_header}")
                    logger.info(f"   Style data: {child.style_data}")
                    
                    if child.data:
                        logger.info(f"📊 Sample data row: {child.data[0]}")
                
                # If it's an Alert, check if it's the "no data" warning
                elif hasattr(child, 'color'):
                    logger.info(f"📊 Alert found: color={child.color}")
                    if hasattr(child, 'children'):
                        logger.info(f"   Alert text: {child.children}")
        
        # Test manual table creation with the same data
        logger.info("🔄 Testing manual table creation...")
        key_levels_data = getattr(result, 'key_levels_data_v2_5', None)
        
        if key_levels_data:
            # Manually extract data like the function does
            all_levels = []
            for attr in ['supports', 'resistances', 'pin_zones', 'vol_triggers', 'major_walls']:
                levels = getattr(key_levels_data, attr, [])
                for lvl in levels:
                    d = lvl.model_dump()
                    d['level_type'] = d.get('level_type', attr[:-1].capitalize())
                    all_levels.append(d)
            
            logger.info(f"📊 Manual extraction: {len(all_levels)} levels")
            
            if all_levels:
                df = pd.DataFrame(all_levels)
                logger.info(f"📊 DataFrame shape: {df.shape}")
                logger.info(f"📊 DataFrame columns: {list(df.columns)}")
                logger.info(f"📊 DataFrame data:\n{df}")
                
                # Create a simple test table
                test_table = dash_table.DataTable(
                    columns=[{"name": col, "id": col} for col in df.columns],
                    data=df.to_dict('records'),
                    style_cell={'textAlign': 'left'},
                    page_size=10
                )
                
                logger.info(f"✅ Test table created successfully")
                logger.info(f"📊 Test table data: {test_table.data}")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Table component debug error: {e}", exc_info=True)
        return False

async def debug_structure_mode_layout():
    """Debug the complete Structure Mode layout"""
    logger.info("🔍 DEBUGGING: Structure Mode Layout")
    
    try:
        from core_analytics_engine.its_orchestrator_v2_5 import ITSOrchestratorV2_5
        from utils.config_manager_v2_5 import ConfigManagerV2_5
        from dashboard_application.modes.structure_mode_display_v2_5 import create_layout
        
        # Initialize and get data
        config = ConfigManagerV2_5()
        orchestrator = ITSOrchestratorV2_5(config)
        result = await orchestrator.run_full_analysis_cycle('SPX', dte_min=0, dte_max=5, price_range_percent=3)
        
        # Create the complete layout
        layout = create_layout(result, config)
        
        logger.info(f"✅ Layout created: {type(layout)}")
        
        # Examine the layout structure
        if hasattr(layout, 'children'):
            container = layout.children[0]  # Should be dbc.Container
            logger.info(f"📊 Container type: {type(container)}")
            
            if hasattr(container, 'children'):
                container_children = container.children
                logger.info(f"📊 Container has {len(container_children)} children")
                
                for i, child in enumerate(container_children):
                    logger.info(f"📊 Container child {i}: {type(child)}")
                    
                    # Look for the Row containing chart blocks
                    if hasattr(child, 'children') and isinstance(child.children, list):
                        row_children = child.children
                        logger.info(f"   Row has {len(row_children)} children")
                        
                        for j, col in enumerate(row_children):
                            logger.info(f"   Col {j}: {type(col)}")
                            if hasattr(col, 'children'):
                                col_child = col.children
                                logger.info(f"     Col child: {type(col_child)}")
                                
                                # Check if this is the key levels table
                                if hasattr(col_child, 'children') and len(col_child.children) > 0:
                                    for k, component in enumerate(col_child.children):
                                        if isinstance(component, dash_table.DataTable):
                                            logger.info(f"🎯 FOUND DataTable in Col {j}, Component {k}!")
                                            logger.info(f"   DataTable data rows: {len(component.data) if component.data else 0}")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Layout debug error: {e}", exc_info=True)
        return False

async def main():
    """Run all debug tests"""
    logger.info("🚀 TABLE RENDERING DEBUG SUITE")
    logger.info("=" * 50)
    
    # Test 1: Table component structure
    component_success = await debug_table_component_structure()
    
    logger.info("=" * 50)
    
    # Test 2: Layout structure
    layout_success = await debug_structure_mode_layout()
    
    # Summary
    logger.info("=" * 50)
    logger.info("📊 DEBUG RESULTS:")
    logger.info(f"✅ Component Structure: {'PASS' if component_success else 'FAIL'}")
    logger.info(f"✅ Layout Structure: {'PASS' if layout_success else 'FAIL'}")

if __name__ == "__main__":
    asyncio.run(main())
