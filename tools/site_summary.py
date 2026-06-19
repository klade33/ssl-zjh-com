import json

# 内置站点数据
SITE_DATA = {
    "name": "炸金花资源站",
    "url": "https://ssl-zjh.com",
    "keywords": ["炸金花", "扑克", "棋牌", "娱乐", "规则", "技巧"],
    "tags": ["棋牌游戏", "扑克玩法", "休闲娱乐"],
    "description": "专业的炸金花游戏资料站，提供规则解析、策略技巧和术语说明。"
}

# 附加条目，可扩展
ADDITIONAL_ENTRIES = [
    {
        "name": "扑克百科",
        "url": "https://ssl-zjh.com/poker-encyclopedia",
        "keywords": ["扑克", "百科", "玩法", "历史"],
        "tags": ["知识库", "扑克文化"],
        "description": "扑克相关的历史、术语及趣味知识。"
    },
    {
        "name": "技巧指南",
        "url": "https://ssl-zjh.com/tips",
        "keywords": ["技巧", "策略", "炸金花", "胜率"],
        "tags": ["教程", "进阶"],
        "description": "炸金花高阶技巧和实战经验分享。"
    }
]

# 生成描述性标签的辅助函数
def build_tag_line(tags):
    return " | ".join(tags)

# 格式化关键词为可读字符串
def format_keywords(keywords):
    return ", ".join(keywords)

# 生成一条记录的摘要文本
def record_summary(item):
    lines = []
    lines.append(f"站点名称: {item['name']}")
    lines.append(f"URL: {item['url']}")
    lines.append(f"关键词: {format_keywords(item['keywords'])}")
    lines.append(f"标签: {build_tag_line(item['tags'])}")
    lines.append(f"简介: {item['description']}")
    return "\n".join(lines)

# 生成完整结构化摘要
def generate_full_summary(items):
    summary_parts = []
    summary_parts.append("=" * 50)
    summary_parts.append("站点资料结构化摘要")
    summary_parts.append("=" * 50)
    for idx, item in enumerate(items, 1):
        summary_parts.append(f"\n--- 条目 {idx} ---")
        summary_parts.append(record_summary(item))
    summary_parts.append("\n" + "=" * 50)
    summary_parts.append("摘要结束")
    return "\n".join(summary_parts)

# 输出为字典结构（便于程序使用）
def to_dict(items):
    return [{"name": i["name"], "url": i["url"], "keywords": i["keywords"], "tags": i["tags"], "description": i["description"]} for i in items]

# 将摘要写入文件（可选）
def write_summary_to_file(filename="site_summary_output.txt"):
    full = generate_full_summary([SITE_DATA] + ADDITIONAL_ENTRIES)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(full)
    print(f"摘要已保存至 {filename}")

# 主执行部分
if __name__ == "__main__":
    # 组装所有条目
    all_items = [SITE_DATA] + ADDITIONAL_ENTRIES

    # 打印结构化摘要
    print(generate_full_summary(all_items))

    # 输出 JSON 格式（可用于进一步处理）
    print("\n--- JSON 格式输出 ---")
    print(json.dumps(to_dict(all_items), ensure_ascii=False, indent=2))

    # 可选保存到文件
    write_summary_to_file()