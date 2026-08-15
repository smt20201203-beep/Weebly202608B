import os
import re

TARGET_DIR = '.'

# 100% 正确的标准自适应播放器 HTML
new_html = (
    f'<div class="video-container" style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden; max-width:800px; margin:10px auto;">'
    f'<iframe src="https://youtube.com" '
    f'style="position:absolute; top:0; left:0; width:100%; height:100%; border:0;" '
    f'allowfullscreen="true"></iframe>'
    f'</div>'
)

if __name__ == "__main__":
    print("🚀 正在自动搜索顽固页面 3d-printing-of-bistable-structures.html ...")
    found = False
    
    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            # 模糊匹配文件名，不管它在哪个子文件夹，不管路径斜杠是 / 还是 \
            if '3d-printing-of-bistable-structures' in file.lower() and file.endswith('.html'):
                file_path = os.path.join(root, file)
                found = True
                
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    html_content = f.read()
                
                # 强力刮除旧的破损模块
                if 'wsite-youtube' in html_content:
                    fixed_content = re.sub(r'<div[^>]*?class="[^"]*?wsite-youtube[^"]*?".*?</div>', new_html, html_content, flags=re.DOTALL | re.IGNORECASE)
                else:
                    # 兜底直接强修被污染的链接字符串
                    fixed_content = html_content.replace('src="https://www."', 'src="https://youtube.com"')
                    fixed_content = fixed_content.replace('src="//www."', 'src="https://youtube.com"')
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                    
                print(f"🎯 成功定位并强制清洗了该网页: {file_path}")
                break
                
    if not found:
        print("❌ 依然没有在所有文件夹中找到包含该名字的 HTML 文件，请确认网页文件名是否正确。")
    else:
        print("🏁 特效药注射完毕！请刷新浏览器页面检查。")