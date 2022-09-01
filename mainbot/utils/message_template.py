from django.conf import settings

def vocabulary_card(english_word, chinese_word, example):
    if len(example) == 0:
        example = "No Example"

    return {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": settings.MESSAGE_PICTURE_URL,
            "size": "full",
            "aspectRatio": "32:15",
            "aspectMode": "cover"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "text",
                            "text": "English : ",
                            "color": "#aaaaaa",
                            "size": "lg",
                            "flex": 6
                        },
                        {
                            "type": "text",
                            "text": english_word,
                            "color": "#666666",
                            "size": "lg",
                            "flex": 6
                        }
                    ],
                    "margin": "md"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Chinese : ",
                            "color": "#aaaaaa",
                            "size": "lg",
                            "flex": 6
                        },
                        {
                            "type": "text",
                            "text": chinese_word,
                            "color": "#666666",
                            "size": "lg",
                            "flex": 6
                        }
                    ],
                    "margin": "md"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Example : ",
                            "color": "#aaaaaa",
                            "size": "lg",
                        }
                    ],
                    "margin": "md"
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": example,
                    "size": "sm",
                    "align": "center",
                    "color": "#666666",
                }
            ]
        }
    }