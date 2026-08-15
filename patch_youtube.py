import os
import re

folder_path = "."

def final_strict_youtube_patch(content):
    # 1. 终极匹配规则：抓取无论是 http、https 还是没有协议头的 Weebly 原始内嵌视频链接
    pattern_iframe = r'src=["\'](?:https?:)?\/\/www\.youtube\.com\/embed\/([a-zA-Z0-9_-]{11})(?:[^\s"\'>]*)["\']'
    
    # 强制将协议头锁死为安全的 https://，且换用对跨域最友好的增强隐私域名
    replacement_iframe = r'src="https://youtube-nocookie.com\1?wmode=opaque"'
    content = re.sub(pattern_iframe, replacement_iframe, content)
    
    # 2. 注入全局高级引荐来源凭证（彻底绕过浏览器的跨域 JS 拦截限制）
    referrer_meta = '<meta name="referrer" content="strict-origin-when-cross-origin">'
    if 'name="referrer"' not in content and '<head>' in content:
        content = content.replace('<head>', f'<head>\n    {referrer_meta}')
        
    return content

if __name__ == "__main__":
    modified_count = 0
    print("🚀 正在全面强制升级全站视频协议（HTTP ➔ HTTPS 安全重构）...")
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    old_content = f.read()
                
                new_content = final_strict_youtube_patch(old_content)
                
                if old_content != new_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"🔒 安全重构成功: {file}")
                    modified_count += 1
                    
    print(f"\n✨ 大清洗完成！共升级并安全越狱了 {modified_count} 个网页文件。")