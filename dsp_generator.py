#!/usr/bin/env python3
"""
DataStealth vs Competitors Comparison Generator
Reads deep_research.md and generates individual comparison files for each competitor
"""

import re
import os
from pathlib import Path

def read_research_file():
    """Read the deep_research.md file"""
    try:
        with open('deep_research.md', 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"✓ Successfully read deep_research.md ({len(content)} characters)")
        return content
    except FileNotFoundError:
        print("✗ Error: deep_research.md not found in current directory")
        return None
    except Exception as e:
        print(f"✗ Error reading file: {e}")
        return None

def parse_problems_and_competitors(content):
    """Parse the content to extract problems and competitor data"""
    # Define competitors
    competitors = {
        'BigID', 'DataSunrise', 'Fortanix', 'Netwrix', 'Privacera', 
        'Protegrity', 'Securiti', 'Sentra', 'Cyera', 'Varonis'
    }
    
    # Extract competitor data for each problem
    competitor_data = {}
    
    # Find all numbered problems
    problem_pattern = r'(\d+)\.\s+([^\n]+)'
    problems = re.findall(problem_pattern, content)
    print(f"✓ Found {len(problems)} problems")
    
    # Split content by problems
    problem_sections = re.split(r'(\d+)\.\s+([^\n]+)', content)
    
    for i in range(1, len(problem_sections), 3):
        if i + 2 < len(problem_sections):
            problem_num = problem_sections[i]
            problem_title = problem_sections[i + 1]
            problem_content = problem_sections[i + 2]
            
            # Look for tab-separated table rows in this section
            lines = problem_content.split('\n')
            for line in lines:
                line = line.strip()
                # Check if line contains tabs and a competitor name
                if '\t' in line and any(comp in line for comp in competitors):
                    parts = line.split('\t')
                    if len(parts) >= 3:
                        competitor = parts[0].strip()
                        how_solves = parts[1].strip()
                        why_datastealth_wins = parts[2].strip()
                        
                        # Check if this is a valid competitor
                        if competitor in competitors:
                            if competitor not in competitor_data:
                                competitor_data[competitor] = {}
                            
                            feature_key = f"{problem_num}. {problem_title}"
                            competitor_data[competitor][feature_key] = {
                                'competitor_approach': how_solves,
                                'datastealth_advantage': why_datastealth_wins
                            }
                            print(f"  Found data for {competitor} in {feature_key}")
    
    print(f"✓ Found data for {len(competitor_data)} competitors: {', '.join(competitor_data.keys())}")
    return competitor_data

def generate_markdown_comparison(competitor, data):
    """Generate markdown content for a specific competitor"""
    markdown = f"# DataStealth vs. {competitor}\n\n"
    markdown += "## Feature Comparison\n\n"
    markdown += "This document provides a detailed comparison between DataStealth and "
    markdown += f"{competitor} across key data security and privacy challenges.\n\n"
    
    for feature, details in data.items():
        markdown += f"### {feature}\n\n"
        markdown += "| Aspect | DataStealth | " + competitor + " |\n"
        markdown += "|--------|-------------|" + "-" * len(competitor) + "|\n"
        ds_advantage = details['datastealth_advantage']
        comp_approach = details['competitor_approach']
        markdown += f"| Approach | {ds_advantage} | {comp_approach} |\n\n"
    
    return markdown

def create_comparison_files(competitor_data):
    """Create individual markdown files for each competitor"""
    # Create reports directory
    reports_dir = Path('reports')
    reports_dir.mkdir(exist_ok=True)
    print(f"✓ Created output directory: {reports_dir}")
    
    # Generate files for each competitor
    for competitor, data in competitor_data.items():
        try:
            # Generate markdown content
            markdown = generate_markdown_comparison(competitor, data)
            
            # Create filename
            filename = f"datastealth_vs_{competitor.lower().replace(' ', '_').replace('.', '_')}.md"
            filepath = reports_dir / filename
            
            # Write file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown)
            
            print(f"✓ Generated: {filepath}")
            
        except Exception as e:
            print(f"✗ Error generating file for {competitor}: {e}")

def main():
    """Main function"""
    print("🚀 DataStealth vs Competitors Comparison Generator")
    print("=" * 50)
    
    # Read the research file
    content = read_research_file()
    if not content:
        return
    
    # Parse problems and competitors
    competitor_data = parse_problems_and_competitors(content)
    if not competitor_data:
        print("✗ No competitor data found")
        return
    
    # Create comparison files
    create_comparison_files(competitor_data)
    
    print("\n" + "=" * 50)
    print("✅ All comparison files generated successfully!")
    print(f"📁 Files saved in: {Path('reports').absolute()}")

if __name__ == "__main__":
    main() 