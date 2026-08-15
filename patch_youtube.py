import os
import re

folder_path = "."

def auto_patch_html_file(content):
    # 1. 精确抓取原始 watch?v= 链接并转换为标准的无 Cookie 增强隐私嵌入链接
    # 使用 youtube-nocookie.com 可以极大程度避免由于用户端 Cookie 导致的播放器初始化失败
    pattern_youtube = r'(?:https?:)?\/\/(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]{11})(?:[^\s"\'>]*)'
    replacement_youtube = r'https://www.youtube-nocookie.com/embed/\1?wmode=opaque'
    content = re.sub(pattern_youtube, replacement_youtube, content)
    
    # 2. 全局注入安全来源凭证（Meta 标签策略）
    # 检查网页头部是否已经有引荐策略，如果没有，就在 <head> 标签最前方插入
    referrer_meta = '<meta name="referrer" content="strict-origin-when-cross-origin">'
    
    if 'name="referrer"' not in content and '<head>' in content:
        # 直接把安全 Meta 标签注入到 <head> 的正下方，对整个页面的所有视频全局生效
        content = content.replace('<head>', f'<head>\n    {referrer_meta}')
        
    return content

if __name__ == "__main__":
    modified_count = 0
    print("🚀 正在对全站几百条视频启动一键批量安全越狱及格式修复...")
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    old_content = f.read()
                
                new_content = auto_patch_html_file(old_content)
                
                if old_content != new_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"✅ 全局注入并修复成功: {file}")
                    modified_count += 1
                    
    print(f"\n✨ 批量大清洗完成！已为 {modified_count} 个网页注入全局授权凭证。")