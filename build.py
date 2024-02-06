import requests

def download_file(url):
    response = requests.get(url,verify=False)
    response.raise_for_status()
    return response.text

def insert_content(original_file, start_marker, end_marker, new_content):
    with open(original_file, 'r', encoding='utf-8') as file:
        content = file.readlines()

    start_index = None
    end_index = None

    # 寻找开始和结束标记的位置
    for i, line in enumerate(content):
        if start_marker in line:
            start_index = i
        elif end_marker in line:
            end_index = i

    if start_index is not None and end_index is not None and start_index < end_index:
        # 在指定位置插入新内容
        content[start_index + 1:end_index] = [new_content + '\n']

    # 重新写入文件
    with open(original_file, 'w', encoding='utf-8') as file:
        file.writelines(content)

def update_files():
    # 更新 friends.md 和 index.md
    friends_content = download_file("https://raw.githubusercontent.com/ProbiusOfficial/helloCTF-CTFerlink/main/output/friends.md")
    with open("docs/Archive/friends.md", 'w', encoding='utf-8') as file:
        file.write(friends_content)
    with open("docs/Archive/index.md", 'w', encoding='utf-8') as file:
        file.write(friends_content)

    # 更新 events 相关文件
    for filename in ["Now_running.md", "Past_events.md", "Upcoming_events.md"]:
        content = download_file(f"https://raw.githubusercontent.com/ProbiusOfficial/Hello-CTFtime/main/Out/{filename}")
        with open(f"docs/Event/{filename}", 'w', encoding='utf-8') as file:
            file.write(content)

    events_html_content = download_file("https://raw.githubusercontent.com/ProbiusOfficial/Hello-CTFtime/main/Out/index.md")
    insert_content("docs/Event/index.md", "<!-- 赛事内容部分_开始 -->", "<!-- 赛事内容部分_结束 -->", events_html_content)

if __name__ == "__main__":
    update_files()
