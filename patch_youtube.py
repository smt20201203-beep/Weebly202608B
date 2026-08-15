import os
import re

folder_path = "."

def fix_weebly_iframe_youtube(content):
    # 1. 专门捕捉 Weebly 原始的畸形 iframe 链接变体
    # 兼容形如 //://youtube.com 
    # 或者 http:// / https:// 等各种没有写完整的 src 链接
    pattern_iframe = r'src=["\'](?:https?:)?\/\/www\.youtube\.com\/embed\/([a-zA-Z0-9_-]{11})(?:\?wmode=opaque)?["\']'
    
    # 统一替换为官方推荐的增强隐私、带安全凭证的安全链接
    replacement_iframe = r'src="https://youtube-nocookie.com\1?wmode=opaque"'
    content = re.sub(pattern_iframe, replacement_iframe, content)
    
    # 2. 全局注入高级安全引荐来源凭证（让浏览器强制带上跨域身份，解决 Error 153）
    referrer_meta = '<meta name="referrer" content="strict-origin-when-cross-origin">'
    if 'name="referrer"' not in content and '<head>' in content:
        content = content.replace('<head>', f'<head>\n    {referrer_meta}')
        
    return content

if __name__ == "__main__":
    modified_count = 0
    print("🚀 开始重新精准提取 Weebly 框架视频并注入安全通行证...")
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    old_content = f.read()
                
                new_content = fix_weebly_iframe_youtube(old_content)
                
                if old_content != new_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"✅ 精准修复并安全授权成功: {file}")
                    modified_count += 1
                    
    print(f"\n✨ 清洗完毕！共完美重构了 {modified_count} 个文件的内嵌视频。")