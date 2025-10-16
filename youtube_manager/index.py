import json

# Load videos from file
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save videos to file
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

# List all videos
def list_all_videos(videos):
    if not videos:
        print("No videos found.")
        return
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Time: {video['time']}")

# Add a new video
def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print("Video added successfully!")

# Update an existing video
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
        print("Video updated successfully!")
    else:
        print("Invalid video number.")

# Delete a video
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete: "))
    if 1 <= index <= len(videos):
        deleted = videos.pop(index-1)
        save_data_helper(videos)
        print(f"Deleted video: {deleted['name']}")
    else:
        print("Invalid video number.")

# Main loop
def main():
    videos = load_data()

    while True:
        print("\nYouTube Manager | Choose an option")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                videos = load_data()
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Exiting YouTube Manager.")
                break
            case _:
                print("Invalid input. Try again!")

if __name__ == "__main__":
    main()
