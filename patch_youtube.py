import os

folder_path = "."

def inject_security_meta(content):
    # 核心：只注入这一行全局高级引荐来源凭证（彻底绕过浏览器的跨域 JS 拦截限制，解决 153 报错）
    referrer_meta = '<meta name="referrer" content="strict-origin-when-cross-origin">'
    
    # 如果网页里没有这句话，且有 <head> 标签，就把它塞进去
    if 'name="referrer"' not in content and '<head>' in content:
        content = content.replace('<head>', f'<head>\n    {referrer_meta}')
        
    return content

if __name__ == "__main__":
    modified_count = 0
    print("🚀 正在为全站原始网页一键注入安全越狱通行证...")
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    old_content = f.read()
                
                new_content = inject_security_meta(old_content)
                
                if old_content != new_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"🔒 安全越狱成功: {file}")
                    modified_count += 1
                    
    print(f"\n✨ 注入完毕！共为 {modified_count} 个网页升级了安全策略。")