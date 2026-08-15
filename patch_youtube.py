import os

folder_path = "."

def force_fix_missing_slash(content):
    # 核心：直接在全站把这一串没有斜杠的错误开头，强制替换为带有 /embed/ 的绝对正确标准开头！
    # 这样不管后面连着什么视频 ID，都能被完美修正回来
    wrong_str = 'src="https://youtube-nocookie.com'
    correct_str = 'src="https://www.youtube-nocookie.com/embed/'
    
    if wrong_str in content:
        content = content.replace(wrong_str, correct_str)
        
    return content

if __name__ == "__main__":
    modified_count = 0
    print("🚀 正在全站无差别强制纠正粘连网址（补齐 www. 和 /embed/ 斜杠）...")
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    old_content = f.read()
                
                new_content = force_fix_missing_slash(old_content)
                
                if old_content != new_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"✅ 纯文本强制扶正成功: {file}")
                    modified_count += 1
                    
    print(f"\n✨ 终极收官！共强制校正了 {modified_count} 个网页文件的视频路径。")