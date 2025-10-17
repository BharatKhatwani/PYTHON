import sqlite3

# Connect to the database (creates file if not exists)
conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
)
''')

# ---------------- Functions ----------------
def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

# ---------------- Main Program ----------------
def main():
    while True:
        print("\nYouTube Manager App with DB")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)

        elif choice == '3':
            video_id = input("Enter the video ID to update: ")
            new_name = input("Enter the new video name: ")
            new_time = input("Enter the new video time: ")
            update_video(video_id, new_name, new_time)

        elif choice == '4':
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
