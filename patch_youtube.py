import os

folder_path = "."

def force_https_upgrade(content):
    # 核心：直接在全站把不安全的 http://www.youtube.com 替换为安全的 https://youtube.com
    # 这样可以一键解除浏览器的 JavaScript 跨域拦截限制
    wrong_http = 'src="http://www.youtube.com/embed/'
    correct_https = 'src="https://youtube.com/embed/'
    
    if wrong_http in content:
        content = content.replace(wrong_http, correct_https)
        
    return content

if __name__ == "__main__":
    modified_count = 0
    print("🔒 正在对全站未显示的视频进行一键 HTTPS 安全协议升级...")
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    old_content = f.read()
                
                new_content = force_https_upgrade(old_content)
                
                if old_content != new_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"🔒 协议升级成功: {file}")
                    modified_count += 1
                    
    print(f"\n✨ 升级完毕！共安全复活了 {modified_count} 个网页文件的视频。")