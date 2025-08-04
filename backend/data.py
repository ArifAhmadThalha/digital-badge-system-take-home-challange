from models import User, Badge, Achievement
import datetime

today = str(datetime.date.today())

users = {
    1: {
        "name": "Alex",
        "email": "alex@example.com",
        "role": "Developer",
        "achievements": [1, 2, 5],
        "avatar": "https://i.pravatar.cc/150?u=alice"
    },
}



achievements = [
    Achievement(id=1, title="First Login", description="Login once", icon_url="🔑", earned=True, earned_date=today),
    Achievement(id=2, title="Post 5 times", description="Submit 5 posts", icon_url="📝",
        earned=False,
        progress=2,
        required=5),
    Achievement(id=3, title="Change Avatar", description="Update your profile picture", icon_url="🎨", earned=True, earned_date=today),
    Achievement(id=4, title="Use Setting", description="Switch to dark or light theme", icon_url="🌑"),
    Achievement(id=5, title="Give Feedback", description="Submit feedback form", icon_url="💬"),
    Achievement(id=6, title="3-Day Login", description="Login 3 days in a row", icon_url="🔥"),
    Achievement(
        id=7,
        title="Visit Pages 8 times",
        description="Explore all sections",
        icon_url="🧭",
        earned=False,
        progress=2,
        required=8
    ),
    Achievement(id=8, title="Connect with users", description="Chat 3 times in chat page.", icon_url="🤝",
        earned=False,
        progress=0,
        required=3),
    Achievement(id=9, title="Late Night Visit", description="Use app after midnight", icon_url="🌙"),
    Achievement(id=10, title="Profile Completion", description="Complete your profile", icon_url="📄", earned=True, earned_date=today)
]


badges = [
    Badge(id=1, title="Contributor", description="Contribute actively", icon_url="https://images.pexels.com/photos/6120400/pexels-photo-6120400.jpeg", criteria=[2, 3]),
    Badge(id=2, title="Explorer", description="Explore everything", icon_url="https://images.pexels.com/photos/2330507/pexels-photo-2330507.jpeg", criteria=[7, 4]),
    Badge(id=3, title="Night Owl", description="Use app late at night", icon_url="https://images.pexels.com/photos/86596/owl-bird-eyes-eagle-owl-86596.jpeg", criteria=[9]),
    Badge(id=4, title="Engager", description="Engage with others", icon_url="https://images.pexels.com/photos/207983/pexels-photo-207983.jpeg", criteria=[5, 8]),
    Badge(id=5, title="Profile Pro", description="Setup your profile fully", icon_url="https://images.pexels.com/photos/771742/pexels-photo-771742.jpeg", criteria=[3, 10])
]
