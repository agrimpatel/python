import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS  videos(
                id INTEGER PRIMARY KEY,
                name VARCHAR(20) NOT NULL,
                time VARCHAR(20) NOT NULL
    )
''')

def list_videos(videos):
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name,time))
    conn.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name=?,time=? WHERE id = ?",(new_name,new_time,video_id))

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id=?",(vide_id,))
    conn.commit()
def main():
    while True:
        print("\n YouTube manager app with DB")
        print("1.List Videos")
        print("2.Add Videos")
        print("3.Update Videos")
        print("4.Delete Videos")
        print("5.Exit Loop")
        choice=input("Enter your choice:")
        
        if choice == '1':
            list_videos(videos)
        elif choice == '2':
            name=input("Enter the videos name:") 
            time=input("Enter the videos name:")
            add_video(name,time)
        elif choice == '3':
            input("Enter video ID to update:")
            name = input("Enter the video name:")
            time = input("Enter the video time:")
            update_video(video_id,name,time)
        elif choice == '4':
            input("Enter video ID to delete:")
            delete_video(video_id)
        elif choice == '5':
            break
        else :
            print("Enter valid input")
                
    conn.close()

if __name__=="__main__":
    main()