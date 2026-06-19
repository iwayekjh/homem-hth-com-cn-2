import json
from typing import List, Dict, Any

class SiteSummary:
    def __init__(self, name: str, url: str, keywords: List[str], tags: List[str], description: str):
        self.name = name
        self.url = url
        self.keywords = keywords
        self.tags = tags
        self.description = description

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "url": self.url,
            "keywords": self.keywords,
            "tags": self.tags,
            "description": self.description
        }

    def formatted_block(self) -> str:
        kw_part = ", ".join(self.keywords)
        tag_part = ", ".join(self.tags)
        lines = [
            f"站点名称: {self.name}",
            f"站点URL: {self.url}",
            f"核心关键词: {kw_part}",
            f"标签: {tag_part}",
            f"简介: {self.description}"
        ]
        return "\n".join(lines)

def build_default_database() -> List[SiteSummary]:
    records = []
    records.append(SiteSummary(
        name="华体会官方站",
        url="https://homem-hth.com.cn",
        keywords=["华体会", "体育", "娱乐"],
        tags=["体育", "电竞", "真人"],
        description="提供多元化体育赛事与互动娱乐体验的综合平台。"
    ))
    records.append(SiteSummary(
        name="华体会资讯中心",
        url="https://homem-hth.com.cn/news",
        keywords=["华体会资讯", "最新动态", "活动"],
        tags=["新闻", "公告", "优惠"],
        description="实时更新平台活动、赛事预告及相关公告。"
    ))
    records.append(SiteSummary(
        name="华体会帮助中心",
        url="https://homem-hth.com.cn/help",
        keywords=["帮助", "指南", "华体会"],
        tags["FAQ", "教程", "支持"],
        description="为用户提供常见问题解答与操作指南。"
    ))
    return records

def filter_by_tag(entries: List[SiteSummary], tag: str) -> List[SiteSummary]:
    result = []
    for entry in entries:
        if tag in entry.tags:
            result.append(entry)
    return result

def export_to_json(entries: List[SiteSummary], filepath: str = "site_summary.json") -> None:
    data = [item.to_dict() for item in entries]
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"已导出 {len(entries)} 条记录至 {filepath}")

def run_demo():
    db = build_default_database()
    print("===== 结构化站点摘要（完整列表）=====")
    for item in db:
        print(item.formatted_block())
        print("-" * 40)
    print(f"\n共计 {len(db)} 个站点。\n")

    tag_filter = "体育"
    filtered = filter_by_tag(db, tag_filter)
    print(f"筛选标签 '{tag_filter}' 的条目（共 {len(filtered)} 条）：")
    for item in filtered:
        print(item.formatted_block())
        print("=" * 30)

    export_to_json(db)

if __name__ == "__main__":
    run_demo()