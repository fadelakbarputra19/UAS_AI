import googleapiclient.discovery
import pandas as pd

# Set your developer key here
DEVELOPER_KEY = "developerkeyy"
video_ids = ["i7V5sI7gVAw", "tAqzxb6VCqs"]

# Build the YouTube API client
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=DEVELOPER_KEY)


def get_comments(video_id):
    request = youtube.commentThreads().list(
        part="snippet", videoId=video_id, maxResults=5000
    )
    comments = []
    while request:
        response = request.execute()
        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]
            public = item["snippet"]["isPublic"]
            comments.append(
                {
                    "author": comment["authorDisplayName"],
                    "updated_at": comment["publishedAt"],
                    "like_count": comment["likeCount"],
                    "text": comment["textOriginal"],
                    "video_id": comment["videoId"],
                    "public": public,
                }
            )
        request = youtube.commentThreads().list_next(request, response)
    return pd.DataFrame(comments)


df = pd.concat([get_comments(video_id) for video_id in video_ids])

# Save to JSON
df.to_json("comments.json", orient="records")

# Save to CSV
df.to_csv("comments.csv", index=False)
