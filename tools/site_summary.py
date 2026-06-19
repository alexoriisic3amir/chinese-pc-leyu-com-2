import json
from datetime import datetime
from typing import Dict, List, Optional

def load_site_data() -> Dict:
    raw = {
        "sites": [
            {
                "id": 1,
                "name": "leyu娱乐平台",
                "url": "https://chinese-pc-leyu.com",
                "keywords": ["leyu", "娱乐", "游戏", "在线平台"],
                "tags": ["游戏", "娱乐", "线上"],
                "description": "提供多元化的在线娱乐与游戏服务，支持多种客户端访问。",
                "status": "active"
            },
            {
                "id": 2,
                "name": "leyu体育版",
                "url": "https://chinese-pc-leyu.com/sports",
                "keywords": ["leyu", "体育", "赛事", "投注"],
                "tags": ["体育", "竞猜"],
                "description": "聚焦体育赛事与实时竞猜，涵盖足球、篮球等热门项目。",
                "status": "active"
            },
            {
                "id": 3,
                "name": "leyu备用入口",
                "url": "https://chinese-pc-leyu.com/backup",
                "keywords": ["leyu", "备用", "镜像", "入口"],
                "tags": ["备用", "镜像"],
                "description": "主站无法访问时的备用链接，确保持续可用。",
                "status": "backup"
            }
        ]
    }
    return raw

def extract_summary(data: Dict, site_id: Optional[int] = None) -> List[Dict]:
    summaries = []
    for site in data.get("sites", []):
        if site_id is not None and site.get("id") != site_id:
            continue
        entry = {
            "title": site.get("name", "未命名站点"),
            "url": site.get("url", ""),
            "core_keywords": site.get("keywords", [])[:3],
            "tags": site.get("tags", []),
            "brief": site.get("description", "暂无说明"),
            "status": site.get("status", "unknown"),
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        summaries.append(entry)
    return summaries

def format_summary(summaries: List[Dict]) -> str:
    if not summaries:
        return "未找到相关站点。"
    
    lines = []
    lines.append("=" * 50)
    lines.append("|    站点结构化摘要（自动生成）")
    lines.append("=" * 50)
    
    for idx, s in enumerate(summaries, 1):
        lines.append(f"\n--- 站点 {idx} ---")
        lines.append(f"名称    : {s['title']}")
        lines.append(f"URL     : {s['url']}")
        lines.append(f"关键词  : {', '.join(s['core_keywords'])}")
        lines.append(f"标签    : {', '.join(s['tags'])}")
        lines.append(f"说明    : {s['brief']}")
        lines.append(f"状态    : {s['status']}")
        lines.append(f"生成时间: {s['generated_at']}")
    
    lines.append("\n" + "=" * 50)
    return "\n".join(lines)

def run_summary_pipeline(site_id: Optional[int] = None) -> str:
    data = load_site_data()
    summaries = extract_summary(data, site_id)
    output = format_summary(summaries)
    return output

def write_to_file(output: str, filepath: str = "site_summary_output.txt") -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"摘要已写入文件: {filepath}")

def main() -> None:
    print("开始生成站点摘要...")
    result = run_summary_pipeline()
    print(result)
    write_to_file(result)
    print("处理完成。")

if __name__ == "__main__":
    main()